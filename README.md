# 🌾 Smart Irrigation Advisory System (ML Project)

## 📌 Overview
This project is an AI-based Smart Irrigation Advisory System that predicts irrigation needs based on environmental and crop conditions using Machine Learning.

It helps farmers make better irrigation decisions and improves water usage efficiency.

---

## 🚀 Features
- Predicts irrigation requirement using ML
- Supports multiple crops, soil types, and growth stages
- Takes environmental inputs (MOI, temperature, humidity)
- Provides AI-based advisory messages
- Interactive Streamlit web application
- Data visualization for insights

---

## 🧠 Machine Learning Model
- Algorithm: Random Forest Classifier
- Accuracy: ~99%
- Output Classes:
  - 0 → No Irrigation Needed (Stable)
  - 1 → Irrigation Recommended (Alert)
  - 2 → Immediate Irrigation Required (Critical)

---

## 📊 Input Features
- Crop ID
- Soil Type
- Seedling Stage
- MOI (Moisture Index)
- Temperature
- Humidity

---

## 📂 Project Structure
Ensure your local workspace directory is organized exactly as shown below for the application to map the trained weights correctly:

```text
smart-irrigation-system/
│
├── app.py                 # Core Streamlit web application & UI logic
├── requirements.txt       # List of required Python dependencies
├── README.md              # Project documentation and setup guide
│
├── irrigation_model.pkl   # Trained Random Forest Classifier model
├── crop_encoder.pkl       # Label Encoder artifact for Crop classes
├── soil_encoder.pkl       # Label Encoder artifact for Soil types
└── stage_encoder.pkl      # Label Encoder artifact for Growth stage
