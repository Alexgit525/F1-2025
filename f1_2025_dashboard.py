
import streamlit as st
import pandas as pd
from datetime import datetime

# Sample F1 2025 Race Calendar
calendar = [
    {"Round": 1, "Race": "Bahrain GP", "Country": "Bahrain", "Date": "2025-03-01", "Status": "Completed"},
    {"Round": 2, "Race": "Saudi Arabian GP", "Country": "Saudi Arabia", "Date": "2025-03-08", "Status": "Completed"},
    {"Round": 3, "Race": "Australian GP", "Country": "Australia", "Date": "2025-03-22", "Status": "Upcoming"},
    {"Round": 4, "Race": "Japanese GP", "Country": "Japan", "Date": "2025-04-06", "Status": "Upcoming"}
]
calendar_df = pd.DataFrame(calendar)

# Sample standings
driver_standings = [
    {"Driver": "Max Verstappen", "Team": "Red Bull", "Points": 50},
    {"Driver": "Charles Leclerc", "Team": "Ferrari", "Points": 36},
    {"Driver": "Lewis Hamilton", "Team": "Mercedes", "Points": 30}
]
drivers_df = pd.DataFrame(driver_standings)

team_standings = [
    {"Team": "Red Bull", "Points": 75},
    {"Team": "Ferrari", "Points": 58},
    {"Team": "Mercedes", "Points": 49}
]
teams_df = pd.DataFrame(team_standings)

# Streamlit Layout
st.set_page_config(page_title="🏎️ F1 2025 Dashboard", layout="wide")
st.title("🏎️ F1 2025 Season Dashboard")

tab1, tab2, tab3, tab4 = st.tabs(["📅 Race Calendar", "🏁 Race Results", "📊 Standings", "🏆 Title Scenarios"])

with tab1:
    st.subheader("📅 F1 2025 Race Calendar")
    st.dataframe(calendar_df)

with tab2:
    st.subheader("🏁 Latest Race Results (Manual Update)")
    st.markdown("Coming soon — You can update this manually after each race.")

with tab3:
    st.subheader("📊 Driver Standings")
    st.dataframe(drivers_df)

    st.subheader("🏢 Constructor Standings")
    st.dataframe(teams_df)

with tab4:
    st.subheader("🏆 Championship Win Scenarios")
    st.markdown("This section will calculate what each driver/team needs to win the title — coming soon.")
