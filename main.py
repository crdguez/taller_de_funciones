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
      \n * :key: Tienen una **expresión general** del tipo: $\\boxed{\\bm{y=mx+n}}$
        \n * Su representación gráfica es una **línea recta**
          \n * El parámetro *m* refleja la inclinación o **pendiente** de la recta
          \n * El parámetro *n* refleja por dónde **corta** la recta al eje OY. A este
          parámetro se le llama **ordenada en el origen**"""
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
    l=[i for i in range(-1*sz,sz+1)]
    l.remove(0)
    # st.write(l)
    a = st.sidebar.select_slider('a',options=l,value=1)
    b = st.sidebar.select_slider('b',options=list(range(-1*sz,sz+1)),value=1)
    c = st.sidebar.select_slider('c',options=list(range(-1*sz,sz+1)),value=1)
    ex=r'ax^2+bx+c'
    eq = parse_latex(ex).subs('a',a).subs('b',b).subs('c',c)
    d=dict()
    d['ex_gen']=ex_gen
    d['eq']=eq
    d['tex']=ex
    d['md']= """Las funciones *cuadráticas* son las funciones polinómicas de segundo grado.
        \n * :key: Tienen una **expresión general** de este tipo: $"""+"""\\boxed{\\bm{y=ax^2+bx+c}}$
        \n * Su representación gráfica es una **curva parabólica**
        \n * Dependiendo de la oriéntación de la parábola, esta tendrá un mínimo o máximo relativo
        llamado **vértice**
        \n * La **parábola es una curva simétrica** y su eje de simetría es la recta vertical que pasa
        por el vértice

        """

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
       \n * :key: Tienen una expresión general del tipo:  $\\boxed{\\bm{y=a+\\frac{k}{x-b}}}$
       \n * :key: Si operamos la expresión anterior llegaremos a una expresión general reducida del tipo:
       $\\boxed{\\bm{y=\\dfrac{a_1 x +b_1}{c_1 x +d_1}}}$
       \n * Su representación gráfica es una **hipérbola**"""
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
    d['md']= """Las funciones *exponenciales* tienen una expresión general del tipo:
           \n :key: $y=a^x$ con $a > 0$
           \n * Si $a > 1 \\to$  la función es creciente
           \n * Si $a < 1 \\to$  la función es decreciente"""
       # \n  $"""+r"""y=a^x$ con $a>0$"""+""" \n *Observa que si a es mayor que 1 la función es creciente y si es menor que uno decreciente*"""
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

FUNCIONES_ACT = {
    "Lineales": 'lineal',
    "Cuadráticas": 'cuadratica',
    "Proporcionalidad inversa":' prop_inversa',
    "Exponencial": 'exponencial',
    "Logarítmica": 'logaritmica',
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
    tipo = st.sidebar.radio("Tipo de función:", list(FUNCIONES_ACT.keys()),index=1)
    actividades.app(FUNCIONES_ACT[tipo])

else :
    intro.app()
