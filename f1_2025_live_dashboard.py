
import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="🏎️ F1 2025 Live Dashboard", layout="wide")
st.title("🏎️ F1 2025 Dashboard – Live from Ergast API")

# Base URL for Ergast API
API_BASE = "https://ergast.com/api/f1/2025"

# Helper to fetch and convert XML/JSON data to DataFrame
@st.cache_data
def get_json(url):
    res = requests.get(url, headers={"Accept": "application/json"})
    if res.status_code == 200:
        return res.json()
    return {}

# --- Tab Layout ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📅 Full Race Calendar",
    "🏁 Race Results (Top 5)",
    "📊 Standings (Top 5)",
    "🏆 Title Scenarios"
])

# 📅 Race Calendar
with tab1:
    st.subheader("2025 F1 Race Calendar (Tentative + Confirmed)")
    race_data = get_json(f"{API_BASE}.json")
    races = race_data.get("MRData", {}).get("RaceTable", {}).get("Races", [])
    if races:
        cal_data = []
        for race in races:
            cal_data.append({
                "Round": race.get("round"),
                "Race": race.get("raceName"),
                "Country": race.get("Circuit", {}).get("Location", {}).get("country"),
                "Date": race.get("date")
            })
        df_calendar = pd.DataFrame(cal_data)
        df_calendar["Date"] = pd.to_datetime(df_calendar["Date"])
        df_calendar = df_calendar.sort_values("Date")
        st.dataframe(df_calendar)
    else:
        st.warning("Race calendar not yet available.")

# 🏁 Race Results (Top 5)
with tab2:
    st.subheader("Latest Race Results – Top 5 Drivers and Teams")
    latest_round = len(races)
    result_data = get_json(f"{API_BASE}/{latest_round}/results.json")
    results = result_data.get("MRData", {}).get("RaceTable", {}).get("Races", [])
    if results:
        race_name = results[0].get("raceName", "")
        st.markdown(f"**Latest Completed Race: {race_name}**")
        top5 = results[0].get("Results", [])[:5]
        rows = []
        for r in top5:
            rows.append({
                "Position": r.get("position"),
                "Driver": f"{r['Driver']['givenName']} {r['Driver']['familyName']}",
                "Team": r.get("Constructor", {}).get("name"),
                "Time/Status": r.get("Time", {}).get("time", r.get("status"))
            })
        df_results = pd.DataFrame(rows)
        st.table(df_results)
    else:
        st.info("No race results yet for 2025.")

# 📊 Standings (Top 5)
with tab3:
    st.subheader("Driver Standings – Top 5")
    drivers_data = get_json(f"{API_BASE}/driverStandings.json")
    d_standings = drivers_data.get("MRData", {}).get("StandingsTable", {}).get("StandingsLists", [])
    if d_standings:
        top5_drivers = d_standings[0].get("DriverStandings", [])[:5]
        driver_rows = []
        for d in top5_drivers:
            driver_rows.append({
                "Position": d["position"],
                "Driver": f"{d['Driver']['givenName']} {d['Driver']['familyName']}",
                "Points": d["points"],
                "Team": d["Constructors"][0]["name"]
            })
        st.dataframe(pd.DataFrame(driver_rows))

    st.subheader("Constructor Standings – Top 5")
    teams_data = get_json(f"{API_BASE}/constructorStandings.json")
    c_standings = teams_data.get("MRData", {}).get("StandingsTable", {}).get("StandingsLists", [])
    if c_standings:
        top5_teams = c_standings[0].get("ConstructorStandings", [])[:5]
        team_rows = []
        for c in top5_teams:
            team_rows.append({
                "Position": c["position"],
                "Team": c["Constructor"]["name"],
                "Points": c["points"]
            })
        st.dataframe(pd.DataFrame(team_rows))

# 🏆 Title Scenarios (Mock logic for now)
with tab4:
    st.subheader("Who Can Still Win? – Mock Logic")
    if d_standings:
        remaining_races = 24 - int(d_standings[0]["round"])
        max_points_remaining = remaining_races * 25
        leader = d_standings[0]["DriverStandings"][0]
        st.markdown(f"👑 **Current Leader:** {leader['Driver']['givenName']} {leader['Driver']['familyName']} ({leader['points']} pts)")
        st.markdown(f"🏁 **Races Remaining:** {remaining_races}")
        st.info("Coming soon: exact points needed by each driver to win.")
    else:
        st.warning("Standings data not available yet.")
