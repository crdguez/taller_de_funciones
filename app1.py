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

def carac(exp) :
    # Devuelve un diccionario con las características de la función f(x)=exp
    d = dict()
    d['exp']=exp
    #d['raices']=solve(exp)
    d['raices']=list(solveset(exp, domain=S.Reals))
    d['oy']=exp.subs(x,0)
    d['dominio']=S.Reals - singularities(exp,x)
    d['fg']= plot_implicit(Eq(y,exp), (x, -10, 10), (y, -10, 10))._backend.fig
    d['poly']=exp.is_polynomial()

    return d

def dom_rec(eq,cte,dominio=True) :
    # Devuelve la gráica de la ecuación y la recta, y los puntos de corte
    p2 = plot_implicit(Eq(y,eq), (x, -5, 5), (y,-10, 10), show=False)
    p2.extend(plot_implicit(Eq(x,cte), (x, -5, 5), (y, -10, 10), show=False))
    if eq.is_polynomial() and (degree(eq, gen=x) == 1) :
        # vx, vy =list(solve([Eq(y,eq),Eq(x,v)]).values())
        puntos=[]
        puntos.append(solve([Eq(x,eq),Eq(y,cte)]))
    else :
        # vx, vy =list(solve([Eq(y,eq),Eq(x,v)])[0].values())
        puntos=solve([Eq(y,eq),Eq(x,cte)])

    for p in list(puntos) :
        vx,vy= p.values()
        p2.append(List2DSeries([vx-0.1,vx+0.1],[vy,vy]))
        # p2.append(List2DSeries([vx,vx],[vy-0.1,vy-0.1]))

    p2.show()
    fg =  p2._backend.fig

    return [fg,puntos]

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

    ex=r'ax^2+bx+c'

    #ex=r'\frac{1}{x}'
    eq = parse_latex(ex).subs('a',a).subs('b',b).subs('c',c)
    eq = E**x
    d = carac(eq)

    col11, col12 = st.beta_columns([1,1])

    with col11 :
        corte_x = ' No tiene' if len(list(solveset(eq, domain=S.Reals))) == 0 else "$"+", ".join(map(latex,d['raices']))+"$"
        st.write("**Características**:  \n * Función:  \n     *  $f(x) ="+ \
            latex(d['exp'])+"$  \n * Corte OX: "+corte_x+ \
            "  \n * Corte OY: $"+latex(d['oy'])+ \
            "$  \n * Dominio: $"+latex(d['dominio'])+"$")
        st.write(d['poly'])

    with col12 :
        # Graficamos la función
        st.pyplot(d['fg'])




    #st.markdown('---')
    #st.markdown('Código python usando la librería *streamlit*:')
    # Fin de echo, Si está dentro de un *echo* aparecerá el código

    st.pyplot(dom_rec(eq,2)[0])
    for p in dom_rec(eq,2)[1] :
        px, py = p.values()
        st.write(px,py)


    st.subheader('Estudiando el dominio')
    col21, col22 = st.beta_columns(2)
    with col21 :
        st.latex(latex(eq))
    with col22 :
        v = st.select_slider('x',options=list(np.arange(-3,3.25,0.25)),value=1)



    col31, col32 = st.beta_columns([6,3])
    with col31 :
        p2 = plot_implicit(Eq(y,eq), (x, -5, 5), (y,-10, 10), show=False)
        p2.extend(plot_implicit(Eq(x,v), (x, -5, 5), (y, -10, 10), show=False))
        if d['poly'] and (degree(eq, gen=x) == 1) :
            vx, vy =list(solve([Eq(y,eq),Eq(x,v)]).values())
        else :
            vx, vy =list(solve([Eq(y,eq),Eq(x,v)])[0].values())
        p2.append(List2DSeries([vx-0.1,vx+0.1],[vy,vy]))
        p2.show()
        fg =  p2._backend.fig
        st.pyplot(fg)
    with col32 :
        txt = """ El punto $\left("""+latex(vx)+r','+latex(vy)+r"\right)$"+""" pertenece a la gráfica. Por
        tanto:  \n * $"""+latex(vx)+""" \in Dom(f)$ y  \n * $"""+latex(vy)+""" \in Im(f)$ """
        st.markdown(txt)

#     st.write("Not multi-\nline")
#     st.write("Still not multi- \nline")
#     st.write("Ok now it's multi-  \nline")
#     st.markdown("Ok now it's multi-  \nline  \n * a ver  \n * a ver 2")
#     txt = """ El punto $\left("""+latex(vx)+r','+latex(vy)+r"\right)$"+""" pertenece a la gráfica. Por
#         tanto:  \n * $"""+latex(vx)+""" \in Dom(f)$ y  \n * $"""+latex(vy)+""" \in Im(f)$ """
#     st.markdown(txt)

#     st.markdown("Ok now it's multi-  \nline  \n * a ver  \n * a ver 2")
