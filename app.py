import joblib
import streamlit as st
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model" / "phishing_model.joblib"

# Page configuration
st.set_page_config(
    page_title="Phishing Email Detector",
    page_icon="🛡️",
    layout="centered",
)

# Professional styling
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #101827, #172554);
        color: #f8fafc;
    }

    h1, h2, h3, p, label {
        color: #f8fafc !important;
    }

    .subtitle {
        color: #cbd5e1;
        text-align: center;
        font-size: 17px;
    }

    .result-card {
        padding: 20px;
        border-radius: 14px;
        margin-top: 20px;
        text-align: center;
        color: white;
    }

    .safe {
        background-color: #166534;
        border: 1px solid #4ade80;
    }

    .phishing {
        background-color: #991b1b;
        border: 1px solid #f87171;
    }

    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


# Header
st.title("🛡️ Phishing Email Detector")

st.markdown(
    '<p class="subtitle">AI-powered email security analysis</p>',
    unsafe_allow_html=True,
)

st.write(
    "Analyze an email to check whether its content resembles "
    "safe or phishing emails learned by our machine learning model."
)

st.divider()

# Handle missing model
if not MODEL_PATH.exists():
    st.error(
        "Trained model not found. Please run "
        "`python train_model.py` first."
    )
    st.stop()

model = load_model()

# Email input
email_text = st.text_area(
    "📩 Paste your email content",
    height=250,
    placeholder=(
        "Paste the email subject and body here...\n\n"
        "Example: Your account requires verification..."
    ),
)

# Analyze email
if st.button("🔍 Analyze Email", use_container_width=True):
    if not email_text.strip():
        st.warning("Please enter an email before analyzing.")
    else:
        with st.spinner("Analyzing email content..."):
            prediction = int(model.predict([email_text])[0])
            probabilities = model.predict_proba([email_text])[0]
            phishing_index = list(model.classes_).index(1)
            phishing_probability = float(
                probabilities[phishing_index]
            )

        st.subheader("Analysis Result")

        if prediction == 1:
            st.markdown(
                """
                <div class="result-card phishing">
                    <h2>⚠️ Potential Phishing Email</h2>
                    <p>The model detected patterns associated with phishing.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
                <div class="result-card safe">
                    <h2>✅ Likely Safe Email</h2>
                    <p>The model classified this email as safe.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.write("### Phishing Prediction Score")

        st.progress(phishing_probability)

        st.metric(
            "Model score",
            f"{phishing_probability * 100:.2f}%",
        )

        st.caption(
            "This score reflects the model's estimated probability, "
            "not a guarantee that the email is malicious or safe."
        )

        st.info(
            "Security tip: Never share passwords or OTPs through email. "
            "Verify suspicious links and sender addresses independently."
        )

# Footer
st.divider()

st.caption(
    "Phishing Email Detection | Machine Learning Project"
)

st.caption(
    "Educational tool only. Do not rely on this model as your sole "
    "email security control."
)
