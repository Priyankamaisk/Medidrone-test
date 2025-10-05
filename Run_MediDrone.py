import streamlit as st
import time
import random
import folium
from streamlit_folium import st_folium
import plotly.express as px
import numpy as np

st.set_page_config(page_title="MediDrone Dashboard", layout="wide")

# Title
st.title("🩺 MediDrone Control Center")

# Sidebar for navigation
menu = st.sidebar.radio("Select a Module", ["AI Triage & Drone Simulation",
                                             "Bird Avoidance",
                                             "Teleconsultation",
                                             "Vitals Monitoring",
                                             "Medicine Dispenser"])

# ---------------- AI Triage & Drone Simulation ----------------
if menu == "AI Triage & Drone Simulation":
    st.subheader("AI Triage System & Drone Simulation")

    # Patient Severity Selection
    severity = st.selectbox("Select patient severity:", ["Low", "Medium", "High"])
    priority = {"Low": "Normal Priority", "Medium": "High Priority", "High": "Critical Priority"}
    st.write(f"**Assigned Priority:** {priority[severity]}")

    # Drone Route Simulation
    st.markdown("**Drone Route Simulation:**")
    m = folium.Map(location=[12.9716, 77.5946], zoom_start=13)
    folium.Marker([12.9716, 77.5946], popup="Start Point").add_to(m)
    folium.Marker([12.9816, 77.6046], popup="Destination").add_to(m)
    folium.PolyLine([[12.9716, 77.5946], [12.9816, 77.6046]], color="blue", weight=3).add_to(m)
    st_folium(m, width=700, height=450)

    # Drone Flight Status Simulation
    st.markdown("**Drone Flight Status:**")
    flight_status = st.empty()
    drone_status_list = ["Taking off", "En route", "Delivered", "Returning", "Completed ✅"]
    for status in drone_status_list:
        flight_status.info(f"Drone Status: {status}")
        time.sleep(0.5)

# ---------------- Bird Avoidance ----------------
elif menu == "Bird Avoidance":
    st.subheader("🚁 Drone Bird Avoidance Simulation")

    # Drone Telemetry Log
    st.markdown("📋 **Drone Telemetry Log:**")
    for i in range(1, 6):
        st.write(f"Drone position {i}: Lat {12.97 + i*0.001}, Lon {77.59 + i*0.001}, Altitude {100+i*5}m")
        time.sleep(0.3)

    # Control Panel
    st.sidebar.markdown("### Control Panel")
    mode = st.sidebar.radio("Switch Mode:", ["AUTO", "REMOTE"])
    st.sidebar.checkbox("Ensure sound deterrent", value=True)

# ---------------- Teleconsultation ----------------
elif menu == "Teleconsultation":
    st.subheader("Telecommunication Module: Doctor–Patient Interaction")

    # Video Consultation Placeholder
    if st.button("Start Video Consultation"):
        st.success("Video Consultation Started!")

    # Chat Interface
    st.text_input("Type your message here:", key="chat_input")
    if st.button("Send Message"):
        st.success("Message sent! AI will prescribe accordingly.")

# ---------------- Vitals Monitoring ----------------
elif menu == "Vitals Monitoring":
    st.subheader("Vitals Monitoring Simulator — ECG, SpO₂, Body Temperature")

    # Simulated Vitals Inputs
    heart_rate = st.slider("Heart Rate (bpm)", 40, 140, 78)
    ecg_noise = st.slider("ECG Noise Level", 0.0, 0.05, 0.01)
    spo2 = st.slider("SpO₂ Baseline (%)", 85, 100, 98)
    temp = st.slider("Temperature Baseline (°C)", 35.0, 40.0, 36.7)

    st.markdown("**Live Vitals Simulation:**")
    t = np.linspace(0, 10, 100)
    ecg_signal = np.sin(2*np.pi*1*t) + np.random.normal(0, ecg_noise, t.shape)
    spo2_signal = spo2 + np.random.normal(0, 0.5, t.shape)
    temp_signal = temp + np.random.normal(0, 0.1, t.shape)

    fig = px.line(x=t, y=ecg_signal, labels={"x":"Time (s)", "y":"ECG Signal"}, title="ECG Signal")
    st.plotly_chart(fig, use_container_width=True)

# ---------------- Medicine Dispenser ----------------
elif menu == "Medicine Dispenser":
    st.subheader("💊 Smart Medicine Dispenser")

    # Medicine buttons in vertical layout
    medicines = ["Paracetamol", "Amoxicillin", "Ibuprofen", "Cetirizine", "Metformin"]
    for med in medicines:
        if st.button(med):
            st.success(f"{med} dispensed successfully! ✅")
            st.balloons()
