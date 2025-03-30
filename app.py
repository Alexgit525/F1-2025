import streamlit as st
import requests
import pandas as pd
from bs4 import BeautifulSoup

st.set_page_config(page_title="🏎️ F1 2025 Dashboard", layout="wide")
st.title("🏎️ F1 2025 Dashboard")

def fetch_data(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'lxml') if response.status_code == 200 else None

def fetch_race_calendar():
    soup = fetch_data("https://www.formula1.com/en/racing/2025.html")
    if not soup:
        return pd.DataFrame()
    races = soup.select('.event-item-wrapper')
    data = [{
        "Date": f"{r.find('span',class_='start-date').text.strip()} {r.find('span',class_='month-wrapper').text.strip()}",
        "Country": r.find('span',class_='event-place').text.strip(),
        "Race": r.find('span',class_='event-title').text.strip(),
        "Status": "Upcoming" if r.find('a', class_='btn--default') else "Completed"
    } for r in races]
    return pd.DataFrame(data)

def fetch_results_standings(category):
    urls = {
        "races": "https://www.formula1.com/en/results.html/2025/races.html",
        "drivers": "https://www.formula1.com/en/results.html/2025/drivers.html",
        "teams": "https://www.formula1.com/en/results.html/2025/team.html"
    }
    soup = fetch_data(urls.get(category))
    if not soup:
        return pd.DataFrame()
    table = soup.find('table', class_='resultsarchive-table')
    headers = [th.get_text(strip=True) for th in table.find_all('th')]
    rows = [[td.get_text(strip=True) for td in tr.find_all('td')] for tr in table.find_all('tr')[1:]]
    return pd.DataFrame(rows, columns=headers)

# Tabs
tab1, tab2, tab3 = st.tabs(["📅 Race Calendar", "🏁 Results & Standings", "📊 Winning Scenarios"])

# Tab 1 - Race calendar
with tab1:
    st.subheader("Race Calendar 2025")
    calendar_df = fetch_race_calendar()
    if not calendar_df.empty:
        st.dataframe(calendar_df, use_container_width=True)
    else:
        st.warning("Race calendar data currently unavailable.")

# Tab 2 - Results and standings
with tab2:
    st.subheader("Race Results")
    results_df = fetch_results_standings("races")
    st.dataframe(results_df if not results_df.empty else pd.DataFrame(["No results available yet."]), use_container_width=True)

    st.subheader("Top 5 Driver Standings")
    drivers_df = fetch_results_standings("drivers").head(5)
    st.dataframe(drivers_df if not drivers_df.empty else pd.DataFrame(["No standings available yet."]), use_container_width=True)

    st.subheader("Top 5 Constructor Standings")
    teams_df = fetch_results_standings("teams").head(5)
    st.dataframe(teams_df if not teams_df.empty else pd.DataFrame(["No standings available yet."]), use_container_width=True)

# Tab 3 - Winning Scenarios
with tab3:
    st.subheader("Winning Scenarios")
    if not drivers_df.empty and not teams_df.empty:
        top_driver = drivers_df.iloc[0]
        top_team = teams_df.iloc[0]
        scenario_text = (
            f"Driver Scenario:\n"
            f"{top_driver[2]} currently leads with {top_driver[-1]} points.\n\n"
            f"Constructor Scenario:\n"
            f"{top_team[2]} currently leads with {top_team[-1]} points.\n\n"
            "(Detailed scenarios require additional season data and custom calculations.)"
        )
        st.write(scenario_text)
    else:
        st.info("Insufficient data available for scenario analysis.")