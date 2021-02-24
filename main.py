from libreria_funciones import *
import streamlit as st
import estudio
import intro
import actividades
import numpy as np
from sympy.parsing.latex import parse_latex
from sympy import *
x, y, z, t = symbols('x y z t')


def lineal():
    sz=5
    ex_gen = 'm*x+n'
    ex=latex(S(ex_gen))
    st.sidebar.write('Parámetros de $'+latex(Eq(y,S(ex_gen)))+"$ :")
    m = st.sidebar.select_slider('m',options=list(range(-1*sz,sz+1)),value=1)
    n = st.sidebar.select_slider('n',options=list(range(-1*sz,sz+1)),value=1)
    eq = parse_latex(ex).subs('m',m).subs('n',n)

    d=dict()
    d['ex_gen']=ex_gen
    d['eq']=eq
    d['tex']=ex
    d['md']= """Las funciones *lineales* son las funciones polinómicas de primer grado.
      \n * :key: Tienen una **expresión general** del tipo: $y=mx+n$
        \n * Su representación gráfica es una **línea recta**
          \n * El parámetro *m* refleja la inclinación o **pendiente** de la recta
          \n * El parámetro *n* refleja por dónde **corta** la recta al eje OY"""
    d['title']= 'Funciones Lineales'
    d['tipo']=lineal.__name__
    # d['extra']=dict()
    # d['extra']['pendiente']=m
    # d['extra']['ordenada']=n
    return d

def cuadratica() :
    sz=5
    ex_gen = 'a*x**2+b*x+c'
    ex=latex(S(ex_gen))
    st.sidebar.write('Parámetros de $'+latex(Eq(y,S(ex_gen)))+"$ :")
    a = st.sidebar.select_slider('a',options=list(range(-1*sz,sz+1)),value=1)
    b = st.sidebar.select_slider('b',options=list(range(-1*sz,sz+1)),value=1)
    c = st.sidebar.select_slider('c',options=list(range(-1*sz,sz+1)),value=1)
    ex=r'ax^2+bx+c'
    eq = parse_latex(ex).subs('a',a).subs('b',b).subs('c',c)
    d=dict()
    d['ex_gen']=ex_gen
    d['eq']=eq
    d['tex']=ex
    d['md']= """Las funciones *cuadráticas* son las funciones polinómicas de segundo grado.
        \n * :key: Tienen una **expresión general** de este tipo: $"""+"""y=ax^2+bx+c$
        \n * Su representación gráfica es una **curva parabólica**"""
    d['title']= 'Funciones Cuadráticas'
    d['tipo']=cuadratica.__name__
    return d

def prop_inversa():
    sz=5
    ex_gen = 'a+k/(x-b)'
    ex=latex(S(ex_gen,evaluate=False))
    st.sidebar.write('Parámetros de $'+latex(Eq(y,S(ex_gen)))+"$ :")
    a = st.sidebar.select_slider('a',options=list(range(-1*sz,sz+1)),value=1)
    b = st.sidebar.select_slider('b',options=list(range(-1*sz,sz+1)),value=1)
    k = st.sidebar.select_slider('k',options=list(range(-1*sz,sz+1)),value=1)
    ex=r'a+\frac{k}{x-b}'
    eq = parse_latex(ex).subs('a',a).subs('b',b).subs('k',k)
    d=dict()
    d['ex_gen']=ex_gen
    d['eq']=eq
    d['tex']=ex
    d['md']= """Las funciones *de proporcionalidad inversa* aparecen al relacionar dos magnitudes
    inversamente proporcionales:
       \n * :key: Tienen una expresión general del tipo:  $y=a+\\frac{k}{x-b}$
       \n * Su representación gráfica es una hipérbola"""
    d['title']= 'Funciones de proporcionalidad inversa'
    d['tipo']=prop_inversa.__name__
    return d

def exponencial():
    sz=3
    ex_gen = 'a**x'
    ex=latex(S(ex_gen,evaluate=False))
    st.sidebar.write('Parámetros de $'+latex(Eq(y,S(ex_gen)))+"$ :")
    rango = list(np.arange(0.25,sz+1,0.25))
    rango.remove(1)
    a = st.sidebar.select_slider('a',options=rango,value=2)
    ex=r'a^x'
    eq = parse_latex(ex).subs('a',a)
    d=dict()
    d['ex_gen']=ex_gen
    d['eq']=eq
    d['tex']=ex
    d['md']= """Las funciones *exponenciales* son las funciones del tipo:
       \n  $"""+r"""y=a^x$"""
    d['title']= 'Funciones exponenciales'
    d['tipo']=exponencial.__name__
    return d

def logaritmica():
    sz=3
    ex_gen='log(x,a)'
    st.sidebar.write('Parámetros de $y='+r"\log_{a}x$ :")
    rango = list(np.arange(0.25,sz+1,0.25))
    rango.remove(1)
    a = st.sidebar.select_slider('a',options=rango,value=2)
    ex=r'\log_{a}x'
    eq = log(x,a,evaluate=False).subs('a',a)
    d=dict()
    d['ex_gen']=ex_gen
    d['eq']=eq
    d['tex']=ex.replace('a',latex(eq.args[1]))
    d['md']= """Las funciones *logarítmicas* son las funciones del tipo:
       \n  $"""+r"""y=\log_{a}x$"""
    d['title']= 'Funciones logarítmicas'
    d['tipo']=logaritmica.__name__
    return d

PAGES = {
    "Introducción": intro,
    "Estudio de Funciones": estudio,
    "Actividades": actividades,
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
st.sidebar.title('Laboratorio de Funciones')
selection = st.sidebar.radio("Selecciona:", list(PAGES.keys()),index=0)

if selection == list(PAGES.keys())[1] :
    # Aquí le pasaré la función
    tipo = st.sidebar.radio("Tipo de función:", list(FUNCIONES.keys()),index=1)

    estudio.app(FUNCIONES[tipo]())

elif selection == list(PAGES.keys())[2] :
    actividades.app()

else :
    intro.app()
