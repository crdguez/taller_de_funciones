# -*- coding: utf-8 -*-
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sympy.parsing.latex import parse_latex
from sympy.plotting.plot import List2DSeries
from sympy import *
x, y, z, t = symbols('x y z t')
from sympy.calculus.util import continuous_domain, function_range

def carac(exp,tipo) :
    # Devuelve un diccionario con las características de la función f(x)=exp
    d = dict()
    d['exp']=exp
    #d['raices']=solve(exp)
    d['raices']=list(solveset(exp, domain=S.Reals))
    d['oy']=exp.subs(x,0)
    #d['dominio']=S.Reals - singularities(exp,x)
    d['dominio']=continuous_domain(exp,x,S.Reals)
    d['rango']=function_range(exp,x,S.Reals)
    d['fg']= plot_implicit(Eq(y,exp), (x, -10, 10), (y, -10, 10))._backend.fig
    d['poly']=exp.is_polynomial()

    # extra
    d['extra'] = dict()
    # d['extra']['0'] = "Nada, de momento"

    if tipo == 'lineal' :
        # d['extra']['0'] = "Pendiente: " +latex(Poly(exp,x).LC())+" y Ordenada en \
            # el origen: " + latex(Poly(exp,x).TC())
        d['extra']['pendiente']= "$"+latex(Poly(exp,x).LC())+"$"
        d['extra']['ordenada']= "$"+latex(Poly(exp,x).TC())+"$"


    return d

def pendiente_ordenada(eq, x0, x1) :
    d = dict()
    lista=[x0,x1]
    lista.append(0)
    if Poly(eq,x).degree() == 0 :
        imagen=[eq,eq,eq]
    else:
        imagen=lambdify(x,eq)(np.array(lista))
    p2 = plot_implicit(Eq(y,eq),(x, -(x1+1), x1+1),(y,-abs(imagen[1])-1,abs(imagen[1])+1),show=False)
    p2.append(List2DSeries([x0,x1,x1],[imagen[0],imagen[0],imagen[1]]))
    p2.show()
    [plt.text(i,eq.subs(x,i)+1,"$\left("+latex(i)+r','+latex(eq.subs(x,i))+r"\right)$") for i in lista]
    plt.text((x0+x1)/2,imagen[0],"$"+latex(x1-x0)+"$")
    plt.text(x1,imagen[0],r"$m=\frac{"+latex(S(imagen[1]-imagen[0]))+r"}{"+latex(x1-x0)+r"}="+latex((S(imagen[1]-imagen[0]))/(x1-x0))+"$")
    plt.text(x1,(imagen[1]+imagen[0])/2,"$"+latex(S(imagen[1]-imagen[0]))+"$")
    txt = "Observa que dados dos puntos de la gráfica, la razón entre \
    la variación de las **y** y la variación de las **x** se mantiene constante."
    plt.scatter(lista,imagen)

    d['fg']=p2._backend.fig
    d['md1']=txt

    return d

def max_min(eq) :
    # devuelve los máximos y mínimos de una función
    d = dict()
    lista=solve(eq.diff())
    imagen=lambdify(x,eq)(np.array(lista))
    p2 = plot_implicit(Eq(y,eq))
    p2.show()
    [plt.text(i,eq.subs(x,i)+1,"$\left("+latex(i)+r','+latex(eq.subs(x,i))+r"\right)$") for i in lista]
    plt.scatter(lista,imagen)

    d['fg']=p2._backend.fig
    d['maxmin']=lista

    return d

def dom_rec(eq,cte,var=x) :
    # Devuelve la gráica de la ecuación y la recta, y los puntos de corte con la recta var=ctw
    p2 = plot_implicit(Eq(y,eq), (x, -5, 5), (y,-10, 10), show=False)
    p2.extend(plot_implicit(Eq(var,cte), (x, -5, 5), (y, -10, 10), show=False, line_color='red'))
    puntos = []
    if eq.is_polynomial() and (degree(eq, gen=x) == 0) and (var == y):
        p2.show()
        fg =  p2._backend.fig
        txt = "Función constante: $"+latex(cte)
        txt += "\\in Im(f)$" if eq==cte else "\\notin Im(f)$"


    else :
        if eq.is_polynomial() and (degree(eq, gen=x) <= 1) :
            # vx, vy =list(solve([Eq(y,eq),Eq(x,v)]).values())
            puntos=[]
            puntos.append(solve([Eq(y,eq),Eq(var,cte)]))
        else :
            # vx, vy =list(solve([Eq(y,eq),Eq(x,v)])[0].values())
            puntos=solve([Eq(y,eq),Eq(var,cte)])
            st.write(puntos)

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