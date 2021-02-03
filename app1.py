import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sympy.parsing.latex import parse_latex
from sympy.plotting.plot import List2DSeries
from sympy import *
x, y, z, t = symbols('x y z t')

def app() :
    # El eco es para publicar el código después, se puede borrar y eliminar el tabulado
    # with st.echo('below') :
    st.title('Funciones cuadráticas')
    st.markdown(r"""Las funciones *cuadráticas* son las funciones polinómicas de segundo grado.
    Por tanto tienen una expresión de este tipo:""")
    st.latex("y=ax^2+bx+c")

    st.markdown("**Ejemplo:**")

    sz = 5
    # Columnas para los deslizadores
    col01, col02, col03 = st.beta_columns(3)
    # Columnas para presentar los datos interactivos
    with col01 :
        a = st.select_slider('a',options=list(range(-1*sz,sz+1)),value=1)
    with col02 :
        b = st.select_slider(' b',options=list(range(-1*sz,sz+1)),value=1)
    with col03 :
        c = st.select_slider('  c',options=list(range(-1*sz,sz+1)),value=1)

    col11, col12 = st.beta_columns([1,2])
    #Tamaño de los deslizadores

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

    #st.markdown('---')
    #st.markdown('Código python usando la librería *streamlit*:')
    # Fin de echo, Si está dentro de un *echo* aparecerá el código

    st.subheader('Estudiando el dominio')
    col21, col22 = st.beta_columns(2)
    with col21 :
        st.latex(latex(eq))
    with col22 :
        v = st.select_slider('x',options=list(np.arange(-3,3.25,0.25)),value=1)



    col31, col32, col33 = st.beta_columns([6,1,3])
    with col31 :
        p2 = plot_implicit(Eq(y,eq), (x, -5, 5), (y,-10, 10), how=False)
        p2.extend(plot_implicit(Eq(x,v), (x, -5, 5), (y, -10, 10), show=False))
        vx, vy =list(solve([Eq(y,eq),Eq(x,v)])[0].values())
        p2.append(List2DSeries([vx-0.1,vx+0.1],[vy,vy]))
        p2.show()
        fg =  p2._backend.fig
        st.pyplot(fg)
    with col32 :
        st.latex(r'\to')
    with col33 :
        txt = r""" El punto
        $\left("""+latex(vx)+r','+latex(vy)+r"""\right)$ pertenece a la gráfica. Por
        tanto:"""
        st.markdown(txt)
        txt = r"""- $"""+latex(vx)+""" \in Dom(f)$ y"""
        st.markdown(txt)
        txt = r"""- $"""+latex(vy)+""" \in Im(f)$ """
        st.markdown(txt)
