# 🛡️ Phishing Email Detection Model

An intelligent machine learning application that analyzes email text and identifies potentially phishing emails to help users recognize suspicious messages.

## 📌 Project Overview

Phishing attacks use deceptive emails to trick people into revealing sensitive information, clicking malicious links, or sharing account credentials.

This project uses Natural Language Processing (NLP) and Machine Learning to classify email messages as **Potential Phishing** or **Likely Safe**.

## ✨ Features

* 🔍 Email phishing detection using Machine Learning.
* 🤖 TF-IDF text feature extraction.
* 📊 Logistic Regression classification.
* ⚡ Interactive Streamlit web application.
* 📈 Phishing probability score.
* 🛡️ Security tips for identifying suspicious emails.
* ⚠️ Error handling for empty inputs.
* 📋 Model evaluation using accuracy, precision, recall, and F1-score.

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* TF-IDF Vectorization
* Logistic Regression
* Streamlit
* Joblib

## 📂 Project Structure

```text
Phising-email-detection/
├── data/
│   └── Balanced_Dataset.csv
├── model/
│   └── phishing_model.joblib
├── app.py
├── train_model.py
├── requirements.txt
├── .gitignore
└── README.md
```

**Note:** The dataset is excluded from the GitHub repository because of its large file size.

## 📊 Model Performance

The model was evaluated using a held-out test dataset.

| Metric    | Result |
| --------- | -----: |
| Accuracy  | 98.14% |
| Precision | 97.81% |
| Recall    | 98.49% |
| F1-Score  | 98.15% |

These results represent performance on the project's test split. Real-world performance may differ.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/akchar1429/Phising-email-detection.git
```

### 2. Navigate to the Project Directory

```bash
cd Phising-email-detection
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🚀 Run the Application

If the trained model file is present in the `model` directory, run:

```bash
python -m streamlit run app.py
```

The application will open in your browser. If it does not open automatically, visit:

`http://localhost:8501`

## 🧠 Train the Model

To train the model from scratch:

1. Obtain the dataset and place `Balanced_Dataset.csv` inside the `data` directory.
2. Run the training script:

```bash
python train_model.py
```

The trained model will be saved to the `model` directory.

## 🔎 How It Works

1. The user enters an email message.
2. The application preprocesses the text using the trained TF-IDF pipeline.
3. The Logistic Regression model analyzes the text.
4. The application displays a classification result and phishing probability score.
5. Security tips help users understand common warning signs.

## ⚠️ Limitations

* The model may incorrectly classify legitimate or phishing emails.
* A high or low phishing score does not guarantee that an email is safe or malicious.
* The application should be used as an educational and preliminary screening tool, not as a replacement for security software or professional analysis.
* Avoid entering confidential emails, passwords, or sensitive personal information.

## 🎯 Project Objective

To demonstrate how Machine Learning and Natural Language Processing can be applied to email security through an interactive web application.

## 👩‍💻 Author

**AKCHAR V S**

GitHub: [akchar1429](https://github.com/akchar1429)

---

⭐ If you find this project useful, consider giving the repository a star!
