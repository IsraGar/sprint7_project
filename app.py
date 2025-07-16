import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Sprint-7 - Project')
grafica = st.radio(
    "Selecciona el tipo de gráfico que deseas visualizar:",
    options=["Ninguno", "Histograma", "Dispersión", "Barras"]
)

if grafica == "Histograma":
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')         
    fig = px.histogram(car_data, x="odometer")     
    st.plotly_chart(fig, use_container_width=True)

elif grafica == "Dispersión":
    st.write('Creación de diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

elif grafica == "Barras":
    st.write('Creación de gráfico de barras de Top 5 de tipos de coches por precio')
    car_data_top_5 = (
    car_data.groupby('type', as_index=False)['price']
    .sum()
    .sort_values(by='price', ascending=False)
    .head(5)
    )
    fig = px.bar(car_data_top_5, x="type", y="price", title="Top 5 tipos de coches por precio total") # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)