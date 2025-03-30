
import streamlit as st
import pandas as pd

st.set_page_config(page_title="2025 F1 Season Dashboard", layout="wide")
st.title("2025 Formula 1 Season Dashboard")

calendar_data = {
    "Round": list(range(1, 25)),
    "Grand Prix": ["Australian GP", "Chinese GP", "Japanese GP", "Bahrain GP", "Saudi Arabian GP",
                   "Miami GP", "Emilia-Romagna GP", "Monaco GP", "Spanish GP", "Canadian GP",
                   "Austrian GP", "British GP", "Belgian GP", "Hungarian GP", "Dutch GP",
                   "Italian GP", "Azerbaijan GP", "Singapore GP", "United States GP",
                   "Mexican GP", "Brazilian GP", "Las Vegas GP", "Qatar GP", "Abu Dhabi GP"],
    "Circuit": ["Albert Park, Melbourne", "Shanghai International Circuit", "Suzuka Circuit, Suzuka",
                "Bahrain International Circuit, Sakhir", "Jeddah Corniche Circuit, Jeddah",
                "Miami International Autodrome, Miami", "Imola, Italy", "Circuit de Monaco, Monte Carlo",
                "Circuit de Barcelona-Catalunya, Barcelona", "Circuit Gilles-Villeneuve, Montreal",
                "Red Bull Ring, Spielberg", "Silverstone Circuit, Silverstone", "Spa-Francorchamps, Spa",
                "Hungaroring, Budapest", "Circuit Zandvoort, Zandvoort", "Monza, Italy",
                "Baku City Circuit, Baku", "Marina Bay Street Circuit, Singapore",
                "Circuit of the Americas, Austin", "Autódromo Hermanos Rodríguez, Mexico City",
                "Interlagos, São Paulo", "Las Vegas Strip Circuit, Las Vegas", "Lusail International Circuit, Lusail",
                "Yas Marina Circuit, Abu Dhabi"],
    "Approx. Dates": ["Mar 14–16, 2025", "Mar 21–23, 2025", "Apr 4–6, 2025", "Apr 11–13, 2025", "Apr 18–20, 2025",
                      "May 2–4, 2025 (Sprint)", "May 16–18, 2025", "May 23–25, 2025", "May 30–Jun 1, 2025", "Jun 13–15, 2025",
                      "Jun 27–29, 2025", "Jul 4–6, 2025", "Jul 25–27, 2025 (Sprint)", "Aug 1–3, 2025", "Aug 29–31, 2025",
                      "Sep 5–7, 2025", "Sep 19–21, 2025", "Oct 3–5, 2025", "Oct 17–19, 2025 (Sprint)", "Oct 24–26, 2025",
                      "Nov 7–9, 2025 (Sprint)", "Nov 20–22, 2025", "Nov 28–30, 2025 (Sprint)", "Dec 5–7, 2025"]
}
st.dataframe(pd.DataFrame(calendar_data), use_container_width=True)
