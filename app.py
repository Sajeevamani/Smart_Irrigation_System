import streamlit as st
import joblib
from visualization import show_visualizations
# --- 1. MODEL LOADING ---
@st.cache_resource
def load_assets():
    model = joblib.load("irrigation_model.pkl")
    crop_encoder = joblib.load("crop_encoder.pkl")
    soil_encoder = joblib.load("soil_encoder.pkl")
    stage_encoder = joblib.load("stage_encoder.pkl")
    return model, crop_encoder, soil_encoder, stage_encoder

model, crop_encoder, soil_encoder, stage_encoder = load_assets()

# --- 2. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Smart Irrigation Advisory System",
    page_icon="🌾",
    layout="centered"
)
# --- 3. STYLING ---
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 6px;
        height: 3em;
        background-color: #2e7d32;
        color: white;
        font-weight: bold;
    }
    .stNumberInput, .stSelectbox {
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. HEADER ---
st.title("🌾 Smart Irrigation Advisory System")
st.write("AI-Powered Early Warning and Irrigation Advisory System for Farmers")
st.markdown("---")

# --- 5. INPUT SECTION ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🌱 Field Profile")
    crop = st.selectbox("Select Crop", crop_encoder.classes_)
    soil_type = st.selectbox("Select Soil Type", soil_encoder.classes_)
    stage = st.selectbox("Select Growth Stage", stage_encoder.classes_)

with col2:
    st.subheader("📊 Live Metrics")
    moi = st.number_input("Moisture Index (MOI %)", 1, 100, 20)
    temp = st.number_input("Temperature (°C)", 0, 60, 25)
    humidity = st.number_input("Humidity (%)", 0.0, 100.0, 60.0)

st.markdown("---")

# --- 6. PREDICTION ---
if st.button("📊 Run Irrigation Risk Assessment"):

    #  inputs
    crop_encoded = crop_encoder.transform([crop])[0]
    soil_encoded = soil_encoder.transform([soil_type])[0]
    stage_encoded = stage_encoder.transform([stage])[0]

    # Prediction
    prediction = model.predict([[
        crop_encoded,
        soil_encoded,
        stage_encoded,
        moi,
        temp,
        humidity
    ]])[0]

    st.subheader("🤖 AI Prediction")

    if prediction == 0:
        st.success("🟢 NO IRRIGATION NEEDED")
        irrigation_needed = False

    elif prediction == 1:
        st.warning("🟡 IRRIGATION RECOMMENDED")
        irrigation_needed = True

    elif prediction == 2:
        st.error("🔴 IMMEDIATE IRRIGATION REQUIRED")
        irrigation_needed = True

    st.markdown("---")
    st.subheader("📢 Advisory Report")

    if irrigation_needed:

        if moi < 25:
            st.warning(f"⚠️ Low Moisture: {moi}% is insufficient for crop growth.")

        if temp > 35:
            st.warning(f"🔥 High Temperature: {temp}°C may increase water loss.")

        if humidity < 40:
            st.warning(f"🌬️ Low Humidity: {humidity}% increases dehydration risk.")

        st.info(
            f"💡 Action Plan: Irrigate the field using drip or controlled irrigation. "
            f"Crop '{crop}' at '{stage}' stage requires careful water management."
        )

    else:
        if humidity > 80:
            st.warning("🍄 High humidity may increase fungal risk.")

        st.info("💡 Field conditions are stable. No irrigation required at this time.")
st.markdown("---")
st.subheader("📊 Data Visualization")
show_visualizations(crop)
st.markdown("---")