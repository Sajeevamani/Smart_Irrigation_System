import streamlit as st
import pandas as pd

def show_visualizations(selected_crop):
    df = pd.read_csv("cropdata_updated.csv")

    # 🔥 FILTER BY SELECTED CROP
    df = df[df["crop ID"] == selected_crop]

    st.subheader(f"📊 Insights for {selected_crop}")

    st.bar_chart(df["result"].value_counts())

    st.subheader("🌡️ Temperature vs Irrigation Need")
    st.scatter_chart(df[["temp", "result"]])

    st.subheader("💧 Humidity vs Irrigation Need")
    st.scatter_chart(df[["humidity", "result"]])