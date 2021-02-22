import streamlit as st

def app() :
    st.title("Actividades")
    st.write('Aquí irán las actividades que se propongan ...')

    st.subheader('Actividad: ¿Qué forma tienen las gráficas de las funciones lineales?')
    with st.beta_expander('Ver solución') :
        st.write('Aquí irá la solución ... (obviamente, tienen forma de línea recta :smirk:)')
