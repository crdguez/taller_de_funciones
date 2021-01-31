import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sympy.parsing.latex import parse_latex
from sympy import *
x, y, z, t = symbols('x y z t')

def app() :
    # El eco es para publicar el código después, se puede borrar y eliminar el tabulado
    with st.echo('below') :
        st.title('Funciones cuadráticas')
        st.markdown(r"""Las funciones *cuadráticas* son las funciones polinómicas de segundo grado.
        Por tanto tienen una expresión de este tipo:""")
        st.latex("y=ax^2+bx+c")

        st.markdown("**Ejemplo:**")
        # Columnas para los deslizadores
        col01, col02, col03 = st.beta_columns(3)
        # Columnas para presentar los datos interactivos
        col11, col12 = st.beta_columns([1,2])
        #Tamaño de los deslizadores
        sz = 5
        with col01 :
            a = st.select_slider('a',options=list(range(-1*sz,sz+1)),value=1)
        with col02 :
            b = st.select_slider(' b',options=list(range(-1*sz,sz+1)),value=1)
        with col03 :
            c = st.select_slider('  c',options=list(range(-1*sz,sz+1)),value=1)
        with col11 :
            ex=r'ax^2+bx+c'
            eq = parse_latex(ex).subs('a',a).subs('b',b).subs('c',c)
            st.markdown('**Función**')
            st.latex('y='+latex(eq))
            st.markdown('**Raíces**')
            st.write(r' $'+ latex(eq)+r'\to$' )
            st.write(r'$'+r', '.join(map(latex,solve(eq)))+r'$')
            st.markdown('**Dominio**')
            st.write(r'$'+latex(S.Reals - singularities(eq,x))+'$')

        with col12 :
            # Graficamos la función
            p1 = plot_implicit(Eq(y,eq), (x, -10, 10), (y, -10, 10))
            fg =  p1._backend.fig
            st.pyplot(fg)

        st.markdown('---')
        st.markdown('Código python usando la librería *streamlit*:')
        # Si está dentro de un *echo* aparecerá el código
