from libreria_funciones import *
import streamlit as st
import app1
import intro

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
    d['tex']=ex
    d['md']= """Las funciones *lineales* son las funciones polinómicas de primer grado.
    Por tanto tienen una expresión de este tipo:   \n  $"""+"""y=mx+n$"""
    d['title']= 'Funciones Lineales'
    d['tipo']=lineal.__name__
    # d['extra']=dict()
    # d['extra']['pendiente']=m
    # d['extra']['ordenada']=n
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
    d['tex']=ex
    d['md']= """Las funciones *cuadráticas* son las funciones polinómicas de segundo grado.
    Por tanto tienen una expresión de este tipo:   \n  $"""+"""y=ax^2+bx+c$"""
    d['title']= 'Funciones Cuadráticas'
    d['tipo']=cuadratica.__name__
    return d

def prop_inversa():
    sz=5
    st.sidebar.write('Parámetros de la función de proporcionalidad inversa:')
    a = st.sidebar.select_slider('a',options=list(range(-1*sz,sz+1)),value=1)
    b = st.sidebar.select_slider('b',options=list(range(-1*sz,sz+1)),value=1)
    k = st.sidebar.select_slider('k',options=list(range(-1*sz,sz+1)),value=1)
    ex=r'a+\frac{k}{x-b}'
    eq = parse_latex(ex).subs('a',a).subs('b',b).subs('k',k)
    d=dict()
    d['eq']=eq
    d['tex']=ex
    d['md']= """Las funciones *de proporcionalidad inversa* son las funciones del tipo:
       \n  $"""+r"""a+\frac{k}{x-b}$"""
    d['title']= 'Funciones de proporcionalidad inversa'
    d['tipo']=prop_inversa.__name__
    return d

def exponencial():
    sz=3
    st.sidebar.write('Parámetros de la función exponencial:')
    rango = list(np.arange(0.25,sz+1,0.25))
    rango.remove(1)
    a = st.sidebar.select_slider('a',options=rango,value=2)
    ex=r'a^x'
    eq = parse_latex(ex).subs('a',a)
    d=dict()
    d['eq']=eq
    d['tex']=ex
    d['md']= """Las funciones *exponenciales* son las funciones del tipo:
       \n  $"""+r"""a^x$"""
    d['title']= 'Funciones exponenciales'
    d['tipo']=exponencial.__name__
    return d

def logaritmica():
    sz=3
    st.sidebar.write('Parámetros de la función logarítmica:')
    rango = list(np.arange(0.25,sz+1,0.25))
    rango.remove(1)
    a = st.sidebar.select_slider('a',options=rango,value=2)
    ex=r'\log_{a}x'
    eq = log(x,a,evaluate=False).subs('a',a)
    d=dict()
    d['eq']=eq
    d['tex']=ex.replace('a',latex(eq.args[1]))
    d['md']= """Las funciones *logarítmicas* son las funciones del tipo:
       \n  $"""+r"""\log_{a}x$"""
    d['title']= 'Funciones logarítmicas'
    d['tipo']=logaritmica.__name__
    return d

PAGES = {
    "Introducción": intro,
    "Funciones": app1,
}

FUNCIONES = {
    "Lineales": lineal,
    "Cuadráticas": cuadratica,
    "Proporcionalidad inversa": prop_inversa,
    "Exponencial": exponencial,
    "Logarítmica": logaritmica,
}


st.set_page_config(
    page_title='Laboratorio de funciones',
    page_icon="🧊",
    layout='wide')
st.sidebar.title('Índice')
selection = st.sidebar.radio("Selecciona:", list(PAGES.keys()),index=0)

if selection == list(PAGES.keys())[1] :
    # Aquí le pasaré la función
    tipo = st.sidebar.radio("Tipo de función:", list(FUNCIONES.keys()),index=1)
    app1.app(FUNCIONES[tipo]())
else :
    intro.app()

# page = PAGES[selection]
# page.app()



# st.sidebar.subheader('Sobre el proyecto')
# st.sidebar.markdown('- Autor: *Carlos Rodríguez*')
# st.sidebar.markdown('- [Repo *Github*](https://github.com/crdguez/probando_streamlit)')
