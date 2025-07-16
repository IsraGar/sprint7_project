import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Sprint-7 - Project')
#1er diagrama
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir diagrama de dispersión')
if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')         
    fig = px.histogram(car_data, x="odometer")     
    st.plotly_chart(fig, use_container_width=True)
elif build_scatter:
    st.write('Creación de diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.ploty_chart(fig, use_container_width=True)
    