import app1
import app2
import streamlit as st

PAGES = {
    "Funciones cuadráticas": app1,
    "Pruebas": app2,
}

st.sidebar.title('Índice')
selection = st.sidebar.radio("Tipos de funciones", list(PAGES.keys()))

page = PAGES[selection]
page.app()



st.sidebar.subheader('Sobre el proyecto')
st.sidebar.markdown('- Autor: *Carlos Rodríguez*')
st.sidebar.markdown('- [Repo *Github*](https://github.com/crdguez/probando_streamlit)')
