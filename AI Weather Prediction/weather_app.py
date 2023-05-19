import streamlit as st
import pandas as pd
import joblib

bgcolor = 'white'
fontcolor = '#1F1F1F'
st.set_page_config(page_title='Rainfall Prediction Prototype', page_icon=':guardsman:', layout='wide', initial_sidebar_state='collapsed')
st.markdown(f"""<style>body{{background-color: {bgcolor}; color: {fontcolor}}}</style>""", unsafe_allow_html=True)



st.title("Welcome to Our Rainfall Prediction Prototype")
st.subheader("Interact with the sliders and start predicting!")
st.text("Made by: Enoch Hii Chen Seng and Loo Seng Xian")

st.write('---')

# Load Dataset
weather = pd.read_csv('C:/Users/Bryan/Desktop/AI Weather Prediction/preprocessed_data.csv')
X = weather

# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Specify Input Parameters')

def user_input_features():
    VisibilityLowMiles = st.sidebar.slider('Visibility (Miles)', 0, X.VisibilityLowMiles.max(), int(X.VisibilityLowMiles.mean()), step=1)
    DewPointHighF = st.sidebar.slider('Dew Point (F)', X.DewPointHighF.min(), X.DewPointHighF.max(), int(X.DewPointHighF.mean()), step=1)
    HumidityHighPercent = st.sidebar.slider('Humidity (%)', 0, X.HumidityHighPercent.max(), int(X.HumidityHighPercent.mean()), step=1)
    TempHighF = st.sidebar.slider('Temperature (F)', X.TempHighF.min(), X.TempHighF.max(), int(X.TempHighF.mean()), step=1)

    data = {'VisibilityLowMiles': VisibilityLowMiles,
            'DewPointHighF': DewPointHighF,
            'HumidityHighPercent': HumidityHighPercent,
            'TempHighF': TempHighF}
    features = pd.DataFrame(data, index=[0])

    # Print specified input parameters
    st.markdown("<h1 style='text-align: center; font-size: 40px;'>Your Input Parameters</h1>", unsafe_allow_html=True)


    for col in features.columns:
        st.write(f"<div style='text-align: center;'><span style='font-size: 30px;'>{col}: </span><span style='font-size: 24px; font-weight: bold;'>{features[col].iloc[0]}</span></div>", unsafe_allow_html=True)


    return features

df = user_input_features()

# Load Model
model = joblib.load('C:/Users/Bryan/Desktop/AI Weather Prediction/rainpred_model.joblib')

# Apply Model to Make Prediction
prediction = model.predict(df)
st.write('---')
st.markdown("<h1 style='text-align: center; font-size: 40px;'>Will it Rain Tommorow?</h1>", unsafe_allow_html=True)
if prediction == 0:
    st.markdown("""
    <div style='text-align:center; display: flex; flex-direction: column; align-items: center; justify-content: center;'>
        <img src='https://imgsrv2.voi.id/NMw_dz0B5GujN301OfrlUKR1OfABjCs1reHPonXlHKo/auto/1200/675/sm/1/bG9jYWw6Ly8vcHVibGlzaGVycy8yNDI1OTAvMjAyMzAxMDYyMzU2LW1haW4uY3JvcHBlZF8xNjczMDI0MjE2LmpwZw.jpg' width='800'>
        <span style="font-size:30px">Yay! There will be No Rain Tomorrow!</span>
    </div>
    """, unsafe_allow_html=True)
elif prediction == 1:
    st.markdown("""
    <div style='text-align:center; display: flex; flex-direction: column; align-items: center; justify-content: center;'>
        <img src='https://cdn.pixabay.com/photo/2017/07/30/17/47/rainy-day-2555006_1280.jpg' width='800'>
        <span style="font-size:30px">Okay lah, tommorow Light Rain only</span>
    </div>
    """, unsafe_allow_html=True)
elif prediction == 2:
    st.markdown("""
    <div style='text-align:center; display: flex; flex-direction: column; align-items: center; justify-content: center;'>
        <img src='https://i.pinimg.com/736x/19/cc/ed/19ccedbb63ab75218ea516c82ddd84f0.jpg' width='800'>
        <span style="font-size:30px">Ermm, there will be a Moderate Rain Tomorrow. Bring your umbrella just in case!</span>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div style='text-align:center; display: flex; flex-direction: column; align-items: center; justify-content: center;'>
        <img src='https://myrepublica.nagariknetwork.com/uploads/media/rain_20210802140558.jpg' width='800'>
        <span style="font-size:30px">Alamak! Tommorow Heavy Rain! Don't forget to bring umbrella :(</span>
    </div>
    """, unsafe_allow_html=True)




st.write('---')