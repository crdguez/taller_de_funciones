# app2.py
import streamlit as st
import streamlit.components.v1 as components

def app() :
    st.title('Pruebas')
    st.markdown('### Ejemplo de uso de $\LaTeX$')
    components.iframe("https://www.heraldo.es/", scrolling = True)
