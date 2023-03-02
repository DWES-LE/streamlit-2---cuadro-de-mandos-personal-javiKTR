import pandas as pd
import streamlit as st

st.title('Datos de las 100 canciones más escuchadas en Spotif')

URL = 'top_100_streamed_songs.csv'
df = pd.read_csv(URL)

# Checkbox para ver la tabal entera
entera = st.checkbox('Mostrar tabla entera') 

if entera == False:
    filtro = st.selectbox('Filtrar por', ['Duración', 'Energía', 'Valance', 'Bailabilidad'])

    if filtro == 'Duración':
        duration = st.selectbox('Duración mayor de ', [2, 3, 4])
        df = df[((df['duration'] >= duration) & (df['duration'] <= duration+1))]
    elif filtro == 'Energía':
        energia = st.selectbox('Ordenar ', ['Descendente', 'Ascendente'])
        if energia == 'Ascendente':
            df = df.sort_values(by='energy', ascending=True)
        elif energia == 'Descendente':
            df = df.sort_values(by='energy', ascending=False)      
    elif filtro == 'Valance':
        valance = st.selectbox('Ordenar ', ['Descendente', 'Ascendente'])
        if valance == 'Ascendente':
            df = df.sort_values(by='valance', ascending=True)
        elif valance == 'Descendente':
            df = df.sort_values(by='valance', ascending=False)      
    elif filtro == 'Bailabilidad':
        baile = st.selectbox('Ordenar ', ['Descendente', 'Ascendente'])
        if baile == 'Ascendente':
            df = df.sort_values(by='danceability', ascending=True)
        elif baile == 'Descendente':
            df = df.sort_values(by='danceability', ascending=False) 

# Mostramos los datos
st.write(df)
