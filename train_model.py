import pandas as pd
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
)

# Project paths
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "Balanced_Dataset.csv"
MODEL_DIR = BASE_DIR / "model"
MODEL_PATH = MODEL_DIR / "phishing_model.joblib"

MODEL_DIR.mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("       PHISHING EMAIL DETECTION - MODEL TRAINING")
print("=" * 60)

# 1. Load and prepare dataset
print("\n[1/5] Loading dataset...")

df = pd.read_csv(DATA_PATH, usecols=["body", "label"])
df = df.dropna(subset=["body", "label"]).copy()

df["body"] = df["body"].astype(str).str.strip()
df["label"] = pd.to_numeric(df["label"], errors="coerce")

df = df.dropna(subset=["label"])
df = df[df["label"].isin([0, 1])]
df = df[df["body"] != ""]

df["label"] = df["label"].astype(int)

X = df["body"]
y = df["label"]

print(f"Total valid emails: {len(df):,}")

# 2. Split data
print("\n[2/5] Splitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

print(f"Training emails: {len(X_train):,}")
print(f"Testing emails: {len(X_test):,}")

# 3. Build the ML pipeline
print("\n[3/5] Building TF-IDF + Logistic Regression model...")

model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=True,
            strip_accents="unicode",
            max_features=50000,
            ngram_range=(1, 2),
            sublinear_tf=True,
            min_df=2,
            max_df=0.98,
        ),
    ),
    (
        "classifier",
        LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
            random_state=42,
        ),
    ),
])

# 4. Train and evaluate
print("\n[4/5] Training model... Please wait!")

model.fit(X_train, y_train)

print("Training completed!")

print("\nEvaluating model...")
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

print("\n" + "=" * 60)
print("                 MODEL EVALUATION")
print("=" * 60)

print(f"Accuracy : {accuracy:.4f} ({accuracy * 100:.2f}%)")
print(f"Precision: {precision:.4f} ({precision * 100:.2f}%)")
print(f"Recall   : {recall:.4f} ({recall * 100:.2f}%)")
print(f"F1-score : {f1:.4f} ({f1 * 100:.2f}%)")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=["Safe Email", "Phishing Email"],
        zero_division=0,
    )
)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 5. Save model
print("\n[5/5] Saving trained model...")

joblib.dump(model, MODEL_PATH, compress=3)

print(f"\nModel saved successfully!")
print(f"Location: {MODEL_PATH}")

print("\n" + "=" * 60)
print("          MODEL TRAINING COMPLETED!")
print("=" * 60)
