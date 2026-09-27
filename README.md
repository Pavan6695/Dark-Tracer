# 🔐 Dark-TRACER: Early Malware Detection Using Spatiotemporal Patterns

Dark-TRACER is a machine learning-based cybersecurity application designed to detect potentially malicious activities by analyzing patterns in darknet traffic.

The project combines multiple supervised machine learning algorithms with a Django-based web application to classify activity and provide malware detection results through an interactive interface.

## 🎯 Objectives

- Detect potentially malicious activity using machine learning.
- Analyze patterns in darknet traffic.
- Compare multiple classification algorithms.
- Provide an interactive web interface for users and administrators.
- Support early identification and analysis of malware-related activity.

## ✨ Features

- 🔍 Machine learning-based malware detection
- 🌐 Darknet traffic pattern analysis
- 📊 Comparison of multiple machine learning algorithms
- 👤 User registration and login
- 👨‍💼 Administrator dashboard
- 🔐 Service provider dashboard
- 📈 Malware prediction
- 📋 Dataset management
- 📊 Model performance comparison
- 📥 Prediction result management

## 🛠️ Technology Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| Web Framework | Django |
| Frontend | HTML, CSS, JavaScript |
| Machine Learning | Scikit-learn |
| Database | MySQL |
| Dataset | CSV |

## 🤖 Machine Learning Algorithms

The project implements and compares several supervised machine learning algorithms:

- Decision Tree
- K-Nearest Neighbors (KNN)
- Logistic Regression
- Naïve Bayes
- Random Forest
- Support Vector Machine (SVM)
- Gradient Boosting

### Model Comparison

| Algorithm | Type |
|---|---|
| Decision Tree | Classification |
| K-Nearest Neighbors (KNN) | Classification |
| Logistic Regression | Binary Classification |
| Naïve Bayes | Probability-based Classification |
| Random Forest | Ensemble Learning |
| Support Vector Machine (SVM) | Classification |
| Gradient Boosting | Ensemble Learning |

## 🏗️ Project Workflow

```text
Darknet Dataset
       ↓
Data Preprocessing
       ↓
Feature Extraction
       ↓
Machine Learning Models
       ↓
Prediction Engine
       ↓
Django Web Application
       ↓
Malware Detection Results
```

## 📂 Project Structure

```text
Dark-TRACER-Malware-Detection/
│
├── Dark_TRACER_Early_Detection/
├── Remote_User/
├── Service_Provider/
├── Template/
│
├── Labeled_Data.csv
├── Malware_Datasets.csv
├── manage.py
├── requirements.txt
├── runtime.txt
├── db.sqlite3
└── readme.md
```

## 🖥️ Application Modules

### 👤 Remote User

Users can:

- Register and log in.
- Access their dashboard.
- Provide data for malware prediction.
- View detection results.

### 👨‍💼 Administrator

The administrator can:

- Manage the application.
- Train and test datasets.
- Compare model performance.
- View prediction results.
- Manage registered users.

### 🔐 Service Provider

The service provider module supports the application's service-side operations and prediction workflow.

## 🔍 Malware Prediction

The prediction module accepts relevant input features, processes the data using the trained machine learning models, and produces a classification result indicating whether the analyzed activity is potentially malicious or legitimate.

## 📊 Results

The system supports comparison of multiple machine learning algorithms for malware classification.

The implemented models, including Random Forest and Gradient Boosting, are used as part of the model comparison and prediction workflow.

Actual accuracy values can be added when the final experimental results are available.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Karthisha25/Dark-TRACER-Malware-Detection.git
```

### 2. Open the Project Directory

```bash
cd Dark-TRACER-Malware-Detection
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Django Server

```bash
python manage.py runserver
```

### 5. Open the Application

Open the following address in your browser:

http://127.0.0.1:8000/

## 🚀 Future Enhancements

- Real-time malware monitoring
- Deep learning-based detection
- Zero-day malware detection
- Cloud deployment
- REST API integration
- Live network traffic analysis
- Improved visualization dashboards

## 👩‍💻 Contributors

- Karthisha
- Harshitha
- Pavan

## 📜 License

This project was developed for academic and educational purposes.

---

⭐ If you found this project interesting, consider giving the repository a star.
