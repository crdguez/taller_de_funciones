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

def dom_rec(eq,cte,var=x) :
    # Devuelve la gráica de la ecuación y la recta, y los puntos de corte con la recta var=ctw
    p2 = plot_implicit(Eq(y,eq), (x, -5, 5), (y,-10, 10), show=False)
    p2.extend(plot_implicit(Eq(var,cte), (x, -5, 5), (y, -10, 10), show=False))
    if eq.is_polynomial() and (degree(eq, gen=x) == 1) :
        # vx, vy =list(solve([Eq(y,eq),Eq(x,v)]).values())
        puntos=[]
        puntos.append(solve([Eq(y,eq),Eq(var,cte)]))
    else :
        # vx, vy =list(solve([Eq(y,eq),Eq(x,v)])[0].values())
        puntos=solve([Eq(y,eq),Eq(var,cte)])

    p2.show()
    fg =  p2._backend.fig
    txt = ""

    for p in list(puntos) :
        # vx,vy= p.values()
        if p[x].is_real and p[y].is_real:
            vx = p[x]
            vy = p[y]
            plt.scatter([vx],[vy])
            plt.text(vx+0.2,vy+0.5,"$\left("""+latex(vx)+r','+latex(vy)+r"\right)$")
            # p2.append(List2DSeries([vx-0.1,vx+0.1],[vy,vy]))

            txt += """  \n El punto $\left("""+latex(vx)+r','+latex(vy)+r"\right)$"+""" pertenece a la gráfica. Por
            tanto:  \n * $"""+latex(vx)+""" \in Dom(f)$ y  \n * $"""+latex(vy)+""" \in Im(f)$   \n """

    return [fg,puntos, txt]

def app(funcion) :
    eq, md, title =funcion['eq'],funcion['md'],funcion['title']

    st.title(title)
    # st.markdown(r"""Las funciones *cuadráticas* son las funciones polinómicas de segundo grado.
    # Por tanto tienen una expresión de este tipo:""")
    # st.latex("y=ax^2+bx+c")
    st.write(md)
    st.markdown("**Ejemplo:**")
    st.latex(eq)
    d = carac(eq)

    col11, col12 = st.beta_columns([1,1])

    with col11 :
        corte_x = ' No tiene' if len(list(solveset(eq, domain=S.Reals))) == 0 else "$"+", ".join(map(latex,d['raices']))+"$"
        st.write("**Características**:  \n * Función:  \n     *  $f(x) ="+ \
            latex(d['exp'])+"$  \n * Corte OX: "+corte_x+ \
            "  \n * Corte OY: $"+latex(d['oy'])+ \
            "$  \n * Dominio: $"+latex(d['dominio'])+"$")

    with col12 :
        # Graficamos la función
        st.pyplot(d['fg'])


    st.subheader('Estudiando el dominio y el recorrido')

    col21, col22, col23 = st.beta_columns(3)
    with col21 :
        st.latex("f(x)="+latex(eq))
    with col22 :
        var=y if st.radio('',('Dominio','Recorrido')) == 'Recorrido' else x
    with col23 :
        cte = st.select_slider(str(var),options=list(np.arange(-3,3.25,0.25)),value=1)

    fg, puntos, txt = dom_rec(eq,cte,var)
    st.pyplot(fg)
    st.markdown(txt)
