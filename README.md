# 🧠 Personality Predictor - Introvert vs Extrovert

A **Streamlit web app** that predicts whether a person is an **introvert or extrovert** based on behavioral traits using a **Random Forest Classifier**.

### 🔗 Live Demo

👉 [Click to Try the App](https://personality-predictorr.streamlit.app)

---

## 📌 Features

* Takes in 4 simple inputs:

  * Social event attendance
  * Frequency of going outside
  * Social media post frequency
  * Friends circle size
* Predicts personality type: **Introvert 🪫** or **Extrovert 🎉**
* Built with:

  * Python 🐍
  * Scikit-learn
  * Streamlit
  * Joblib

---

## 🧪 Dataset Info

* Source: [Kaggle Dataset](https://www.kaggle.com/datasets/rakeshkapilavai/extrovert-vs-introvert-behavior-data)
* 2900 rows × 8 columns
* Preprocessing steps:

  * Converted categorical variables to binary (Yes/No → 1/0)
  * Selected features with positive correlation to target
  * Imputed missing values using `SimpleImputer`
  * Used Random Forest for classification

---

## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/personality-predictor.git
cd personality-predictor
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run Streamlit App

```bash
streamlit run app.py
```

---

## 📁 File Structure

```
├── app.py                # Main Streamlit app
├── personality_model.pkl # Trained Random Forest model
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 📊 Model Performance

* ✅ Accuracy: **90.3%**
* 📈 R² Score: **0.62**
* ✔️ Trained using `RandomForestClassifier` from Scikit-learn

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙇‍♂️ Author

Developed by **Anik Chand**

🔗 [LinkedIn](https://linkedin.com/in/anikchand) | [GitHub](https://github.com/your-username)
