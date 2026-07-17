# diabetes_risk_assessment
INTERNID - CITS6769
# 🩺 Diabetes Risk Assessment

A Machine Learning project that predicts whether a person is at risk of diabetes based on medical parameters. The project uses the Pima Indians Diabetes Dataset, trains a Logistic Regression model, and provides predictions through a Streamlit web application.

---

## 📌 Features

- Predicts diabetes risk from patient health data
- User-friendly Streamlit web interface
- Data preprocessing using StandardScaler
- Machine Learning model trained with Logistic Regression
- Model serialization using Joblib
- Simple and beginner-friendly project structure

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook
- VS Code

---

## 📂 Project Structure

```
Diabetes-Risk-Assessment
│
├── dataset/
│   └── diabetes.csv
│
├── model/
│   ├── diabetes_model.pkl
│   └── scaler.pkl
│
├── Diabetes_Risk_Assessment.ipynb
├── app.py
├── requirements.txt
```

---

## 📊 Dataset

The project uses the **Pima Indians Diabetes Dataset**.

### Input Features

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

### Target

- **0** → No Diabetes
- **1** → Diabetes

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Diabetes-Risk-Assessment.git
```

Move into the project folder:

```bash
cd Diabetes-Risk-Assessment
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Project

### Step 1: Train the Model

Run all cells in:

```
Diabetes_Risk_Assessment.ipynb
```

This generates:

- diabetes_model.pkl
- scaler.pkl

inside the **model** folder.

### Step 2: Run the Streamlit Application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## 🧠 Machine Learning Workflow

1. Load Dataset
2. Data Exploration
3. Data Preprocessing
4. Feature Selection
5. Train-Test Split
6. Feature Scaling
7. Model Training
8. Model Evaluation
9. Save Model
10. Deploy using Streamlit

---

## 📈 Model

Algorithm Used:

- Logistic Regression

Evaluation Metrics:

- Accuracy
- Confusion Matrix
- Classification Report

---

## 💻 User Interface

The Streamlit application allows users to:

- Enter patient health information
- Predict diabetes risk instantly
- Display prediction results in a simple interface

---

## 📷 Screenshots

Add screenshots of your Streamlit application here after running the project.

---

## 🔮 Future Improvements

- Add multiple Machine Learning algorithms
- Compare model performance
- Display prediction probability
- Add data visualization dashboard
- Deploy the application online
- Improve UI with custom styling

---

## 👩‍💻 Author

**Shailja Dixit**

---

## 📜 License

This project is developed for educational and learning purposes.
