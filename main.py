import app1
import app2
import streamlit as st
import numpy as np

PAGES = {
    "Funciones cuadráticas": app1,
    "Pruebas": app2,
}

st.sidebar.title('Índice')
selection = st.sidebar.radio("Tipos de funciones", list(PAGES.keys()))

if selection == list(PAGES.keys())[0] :
    st.sidebar.slider('Slide me', min_value=0, max_value=10)
    st.sidebar.select_slider('Slide to select', options=list(np.arange(-2,2.25,0.25)))

page = PAGES[selection]
page.app()



st.sidebar.subheader('Sobre el proyecto')
st.sidebar.markdown('- Autor: *Carlos Rodríguez*')
st.sidebar.markdown('- [Repo *Github*](https://github.com/crdguez/probando_streamlit)')
