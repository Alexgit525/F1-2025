import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="🏎️ F1 2025 Live Dashboard", layout="wide")
st.title("🏎️ F1 2025 Live Dashboard")

# Fetch sessions for 2025
def fetch_sessions(year=2025):
    response = requests.get(f"https://api.openf1.org/v1/sessions?year={year}")
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    return pd.DataFrame()

# Fetch laps data for a given session
def fetch_laps(session_key):
    response = requests.get(f"https://api.openf1.org/v1/laps?session_key={session_key}")
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    return pd.DataFrame()

sessions = fetch_sessions()

if not sessions.empty:
    latest_session = sessions.sort_values("date_start", ascending=False).iloc[0]
    session_key = latest_session["session_key"]

    st.header(f"📅 Latest Session: {latest_session['session_name']} ({latest_session['circuit_short_name']})")
    st.markdown(f"**Session Type:** {latest_session['session_type']}  \n**Date:** {latest_session['date_start']}")

    laps = fetch_laps(session_key)

    if not laps.empty:
        st.subheader("⏱️ Live Lap Data")
        laps_display = laps[['driver_number', 'lap_number', 'lap_duration', 'st_speed', 'date_start']].sort_values(by='lap_number', ascending=False)
        st.dataframe(laps_display.reset_index(drop=True), use_container_width=True)
    else:
        st.info("Lap data is not available yet.")
else:
    st.info("Session data for the 2025 season is not available yet. Please revisit closer to race dates.")