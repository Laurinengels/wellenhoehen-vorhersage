import streamlit as st
import joblib
import numpy as np
import datetime

# Modell laden
model = joblib.load("modell.pkl")

st.set_page_config(page_title="Wellenhöhe Vorhersage", page_icon="🌊")
st.title("🌊 Wellenhöhen-Vorhersage")

st.markdown("Gib unten die Bedingungen ein, um die prognostizierte Wellenhöhe zu berechnen.")

wind = st.slider("Windgeschwindigkeit (km/h)", 0, 100, 20)
gezeiten = st.selectbox("Gezeitenstand", ["Ebbe", "Flut"])
datum = st.date_input("Datum", datetime.date.today())
monat = datum.month

# Umwandlung für Modell
gezeiten_flut = 1 if gezeiten == "Flut" else 0
eingabe = np.array([[wind, monat, gezeiten_flut]])

if st.button("Vorhersage starten"):
    vorhersage = model.predict(eingabe)[0]
    st.success(f"📏 Geschätzte Wellenhöhe: {vorhersage:.2f} Meter")
