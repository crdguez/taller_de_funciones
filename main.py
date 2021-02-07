import app1
import app2
import streamlit as st
import numpy as np
from sympy.parsing.latex import parse_latex
from sympy import *
x, y, z, t = symbols('x y z t')


def lineal():
    sz=5
    st.sidebar.write('Parámetros de la función lineal:')
    m = st.sidebar.select_slider('m',options=list(range(-1*sz,sz+1)),value=1)
    n = st.sidebar.select_slider('n',options=list(range(-1*sz,sz+1)),value=1)
    ex=r'mx+n'
    eq = parse_latex(ex).subs('m',m).subs('n',n)
    d=dict()
    d['eq']=eq
    d['md']= """Las funciones *lineales* son las funciones polinómicas de primer grado.
    Por tanto tienen una expresión de este tipo:   \n  $"""+"""y=mx+n$"""
    d['title']= 'Funciones Lineales'
    return d

def cuadratica() :
    sz=5
    st.sidebar.write('Parámetros de la función cuadrática:')
    a = st.sidebar.select_slider('a',options=list(range(-1*sz,sz+1)),value=1)
    b = st.sidebar.select_slider('b',options=list(range(-1*sz,sz+1)),value=1)
    c = st.sidebar.select_slider('c',options=list(range(-1*sz,sz+1)),value=1)
    ex=r'ax^2+bx+c'
    eq = parse_latex(ex).subs('a',a).subs('b',b).subs('c',c)
    d=dict()
    d['eq']=eq
    d['md']= """Las funciones *cuadráticas* son las funciones polinómicas de segundo grado.
    Por tanto tienen una expresión de este tipo:   \n  $"""+"""y=ax^2+bx+c$"""
    d['title']= 'Funciones Cuadráticas'
    return d

def prop_inversa():
    sz=5
    st.sidebar.write('Parámetros de proporcionalidad inversa:')
    a = st.sidebar.select_slider('a',options=list(range(-1*sz,sz+1)),value=1)
    b = st.sidebar.select_slider('b',options=list(range(-1*sz,sz+1)),value=1)
    ex=r'a+\frac{1}{x-b}'
    eq = parse_latex(ex).subs('a',a).subs('b',b)
    d=dict()
    d['eq']=eq
    d['md']= """Las funciones *de proporcionalidad inversa* son las funciones del tipo:
       \n  $"""+r"""a+\frac{1}{x-b}$"""
    d['title']= 'Funciones de proporcionalidad inversa'
    return d

PAGES = {
    "Introducción": app2,
    "Funciones": app1,
}

FUNCIONES = {
    "Lineales": lineal,
    "Cuadráticas": cuadratica,
    "Proporcionalidad inversa": prop_inversa,
}


st.sidebar.title('Índice')
selection = st.sidebar.radio("Selecciona:", list(PAGES.keys()),index=0)

if selection == list(PAGES.keys())[1] :
    # Aquí le pasaré la función
    tipo = st.sidebar.radio("Tipo de función:", list(FUNCIONES.keys()),index=1)
    app1.app(FUNCIONES[tipo]())
else :
    app2.app()

# page = PAGES[selection]
# page.app()



# st.sidebar.subheader('Sobre el proyecto')
# st.sidebar.markdown('- Autor: *Carlos Rodríguez*')
# st.sidebar.markdown('- [Repo *Github*](https://github.com/crdguez/probando_streamlit)')
