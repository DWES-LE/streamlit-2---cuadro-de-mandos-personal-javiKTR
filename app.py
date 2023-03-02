import pandas as pd
import streamlit as st

# Cargamos los datos
URL = 'top_100_streamed_songs.csv'
st.title('Datos de las 100 canciones más escuchadas en Spotify')

df = pd.read_csv(URL)

# Mostramos los datos
st.write(df)