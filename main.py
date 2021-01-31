import app1
import app2
import streamlit as st

PAGES = {
    "Mi primera aplicación": app1,
    "Otra aplicación": app2
}

'-página creada por CRJ-'

st.sidebar.title('Índice')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
