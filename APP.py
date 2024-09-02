import streamlit as st
import pickle
import pandas as pd

model_path = r'C:\University of Phayao\Year 3\Web Scaping\model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

country_mapping = {
    'England': 19, 'Norway': 40, 'Brazil': 7, 'France': 20, 'Germany': 22,
    'Spain': 51, 'Uruguay': 57, 'Argentina': 2, 'Nigeria': 39, 'Portugal': 43,
    'Netherlands': 38, 'Georgia': 21, 'Italy': 30, 'Ecuador': 17, 'Colombia': 11,
    'Croatia': 13, 'Hungary': 26, 'Sweden': 52, 'Denmark': 16, 'Belgium': 5,
    'Serbia': 48, 'Morocco': 37, 'Egypt': 18, 'Ireland': 28, 'Slovenia': 50,
    'Ghana': 23, 'Canada': 10, 'Japan': 32, 'Wales': 59, 'Türkiye': 54,
    'Senegal': 47, 'Burkina Faso': 8, 'Korea, South': 33, 'Switzerland': 53,
    'Jamaica': 31, "Cote d'Ivoire": 12, 'Mexico': 36, 'Cameroon': 9,
    'United States': 56, 'Guinea': 25, 'Ukraine': 55, 'Algeria': 1, 'Mali': 35,
    'Slovakia': 49, 'Scotland': 46, 'Poland': 42, 'Iceland': 27, 'Czech Republic': 14,
    'Russia': 45, 'Austria': 4, 'DR Congo': 15, 'Bosnia-Herzegovina': 6,
    'Israel': 29, 'Romania': 44, 'Kosovo': 34, 'Venezuela': 58, 'Greece': 24,
    'Paraguay': 41, 'Albania': 0, 'Armenia': 3
}

club_mapping = {
    'Real Madrid': 58, 'Manchester City': 45, 'Arsenal FC': 12, 'Bayer 04 Leverkusen': 17,
    'Bayern Munich': 18, 'FC Barcelona': 29, 'Inter Milan': 39, 'SSC Napoli': 63,
    'Atlético de Madrid': 16, 'AC Milan': 0, 'Newcastle United': 47, 'Chelsea FC': 25,
    'RB Leipzig': 54, 'Liverpool FC': 44, 'Athletic Bilbao': 15, 'Juventus FC': 41,
    'Tottenham Hotspur': 70, 'Manchester United': 46, 'West Ham United': 74,
    'Sporting CP': 67, 'Aston Villa': 13, 'Paris Saint-Germain': 53, 'Crystal Palace': 26,
    'Al-Ittihad Club': 8, 'Brighton & Hove Albion': 23, 'LOSC Lille': 42,
    'Real Sociedad': 59, 'Al-Ahli SFC': 6, 'SL Benfica': 61, 'Atalanta BC': 14,
    'PSV Eindhoven': 52, 'Wolverhampton Wanderers': 76, 'Valencia CF': 71,
    'FC Porto': 31, 'Everton FC': 28, 'Feyenoord Rotterdam': 33, 'Villarreal CF': 73,
    'Nottingham Forest': 48, 'Brentford FC': 22, 'Borussia Dortmund': 20,
    'AFC Bournemouth': 2, 'Olympique Marseille': 51, 'Shakhtar Donetsk': 64,
    'Ajax Amsterdam': 5, 'AS Roma': 4, 'Fulham FC': 34, 'Without ClubWithout Club': 75,
    'Al-Hilal SFC': 7, 'Sociedade Esportiva Palmeiras': 65, 'Real Betis Balompié': 57,
    'Leicester City': 43, 'VfB Stuttgart': 72, 'AS Monaco': 3, 'ACF Fiorentina': 1,
    'Girona FC': 37, 'Inter Miami CF': 38, 'Eintracht Frankfurt': 27,
    'Botafogo de Futebol e Regatas': 21, 'Red Bull Salzburg': 60, 'Southampton FC': 66,
    'Olympique Lyon': 50, 'OGC Nice': 49, 'RC Lens': 55, 'SS Lazio': 62,
    'Stade Rennais FC': 68, 'Torino FC': 69, 'Ipswich Town': 40, 'Al-Nassr FC': 9,
    'Al-Orobah FC': 10, 'Bologna FC 1909': 19, 'CR Flamengo': 24, 'Fenerbahce': 32,
    'GNK Dinamo Zagreb': 35, 'Al-Sadd SC': 11, 'Galatasaray': 36, 'FC Krasnodar': 30,
    'Zenit St. Petersburg': 77, 'RC Strasbourg Alsace': 56
}

st.set_page_config(
    page_title="Football Player Values Prediction",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("Football Player Values Prediction")
st.write("Predict the value of a football player.")

with st.form(key='prediction_form'):
    st.subheader("Player Details:")
    country = st.selectbox('Country', list(country_mapping.keys()))
    club = st.selectbox('Club', list(club_mapping.keys()))
    age = st.slider('Age', min_value=0, max_value=100, value=20)
    submit_button = st.form_submit_button(label='Predict')

if submit_button:
    country_value = country_mapping[country]
    club_value = club_mapping[club]
    input_data = pd.DataFrame([[country_value, club_value, age]], columns=['Country', 'club', 'Age'])
    
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"predicted value player: **€{prediction:,.2f}m**")
    except ValueError as e:
        st.error(f"An error occurred: {e}")

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 10px;
        background-color: #f0f2f6;
        font-size: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
