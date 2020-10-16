import streamlit as st
import pandas as pd



st.text("COVID-19 Swiss perspective")

df = pd.read_csv("https://raw.githubusercontent.com/openZH/covid_19/master/COVID19_Fallzahlen_CH_total_v2.csv")

st.write(df)