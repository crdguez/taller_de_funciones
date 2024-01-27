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
    d['exp']=nsimplify(exp)
    # d['exp']=exp
    # d['raices']=solve(exp)
    d['raices']=list(solveset(exp, domain=S.Reals))
    d['oy']=(0,exp.subs(x,0))
    #d['dominio']=S.Reals - singularities(exp,x)
    d['dominio']=continuous_domain(exp,x,S.Reals)
    d['rango']=function_range(exp,x,S.Reals)
#     plot_implicit(Eq(y,exp), (x, -10, 10), (y, -10, 10))._backend.fig
    p=plot_implicit(Eq(y,exp), (x, -10, 10), (y, -10, 10))
    fg, ax = p._backend.fig, p._backend.ax
    ax[0].set_title("$y="+latex(nsimplify(exp))+"$  \n ")
    ax[0].set_aspect('equal')
    plt.grid(True)


    # d['poly']=exp.is_polynomial()

    # extra
    d['extra'] = dict()

    if tipo == 'lineal' :
        # d['extra']['0'] = "Pendiente: " +latex(Poly(exp,x).LC())+" y Ordenada en \
            # el origen: " + latex(Poly(exp,x).TC())
        # d['extra']['pendiente']= "$"+latex(Poly(exp,x).LC())+"$"
        # d['extra']['ordenada']= "$"+latex(Poly(exp,x).TC())+"$"
        d['extra']['Pendiente']= Poly(exp,x).LC()
        d['extra']['Ordenada']= Poly(exp,x).TC()
        d['forma']='La **gráfica** de la función es una **línea recta**. Si la pendiente es positiva \
        la función es creciente, si es negativa, decreciente, y si es cero, la recta es horizontal. \
        A las funciones cuya gráfica es horizontal se les llama **funciones constantes**. '

    if tipo == 'cuadratica' :
        v0=-1*Poly(exp,x).all_coeffs()[1]/(2*Poly(exp,x).all_coeffs()[0])
        fv0=exp.subs(x,v0)
        d['extra']['Vértice']= "$\\left("+latex(v0)+","+latex(fv0)+"\\right)$"
        d['forma']='La **gráfica** de la función es una **parábola**.'
        d['extra']['Eje de Simetría']= "$x="+latex(v0)+"$"
        plt.plot([v0,v0],[-10,10],linestyle='dotted',color='yellow')

    if tipo == 'prop_inversa' :
        av=list(singularities(exp,x))[0]
        ah=limit(exp,x,oo)
        d['extra']['Asíntota vertical']= "$x="+latex(av)+"$"
        d['extra']['Asíntota horizontal']= "$y="+latex(ah)+"$"
        d['forma']='La **gráfica** de la función es una **hipérbola**.'
        plt.plot([av,av],[-10,10],linestyle='dotted',color='yellow')
        plt.plot([-10,10],[ah,ah],linestyle='dotted',color='yellow')

    d['fg']= fg

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
    txt = " * Dados dos puntos de la gráfica, la razón entre \
    la variación de las **y** y la variación de las **x** se mantiene constante. \
      \n * A la constante anterior se le llama *pendiente* y coincide con el valor del \
      parámetro *m*. Por esta razón al parámetro *m* de la función lineal se le llama **pendiente** \
      \n * Observa que el parámetro *n* coincide con el valor del punto donde la recta corta \
      al eje **OY**. Por esta razón al parámetro *n* de la función lineal se le llama **ordenada en el origen**"
    plt.scatter(lista,imagen)

    d['fg']=p2._backend.fig
    d['md1']=txt

    return d

def tabla_valores(eq, tipo, num, max):
    d = dict()
    lista=np.linspace(0.0001,max,num) if tipo == 'logaritmica' else np.linspace(-max,max,num)
    if tipo == 'lineal' and poly(eq,x).degree() == 0 :
    # if tipo == 'lineal'  :
        lista2 = [eq for i in lista]
        lista2 = np.float_(lista2)
    else :
        # lista2 = lambdify(x,eq)(lista)
        lista2 = [eq.subs(x,i) for i in lista]
        lista2 = np.float_(lista2)

    p = plot_implicit(Eq(y,eq), (x, -10, 10), (y, -10, 10),line_color='yellow')
    fg, ax = p._backend.fig, p._backend.ax
    ax[0].set_title("$y="+latex(nsimplify(eq))+"$  \n ")
    ax[0].set_aspect('equal')
    plt.grid(True)

    plt.scatter(lista,lista2)
    d['df']=pd.DataFrame({'x':lista,'y':lista2})
    d['fg']=fg

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


def cortes(eq) :
    d = dict()
    # devuelve los puntos de corte
    p=plot_implicit(Eq(y,eq), (x, -10, 10), (y, -10, 10))
    fg, ax = p._backend.fig, p._backend.ax
    ax[0].set_title("$y="+latex(eq)+"$   \n ")
    ax[0].set_aspect('equal')
    # corte_x = [] if len(list(solveset(eq, domain=S.Reals))) == 0 else list(solveset(eq, domain=S.Reals))
    lista=list(solveset(eq, domain=S.Reals))
    imagenes = [eq.subs(x,i) for i in lista]
    plt.scatter(lista,imagenes)
    [plt.text(i,eq.subs(x,i)+1,"$\left("+latex(i)+r','+latex(eq.subs(x,i))+r"\right)$") for i in lista]
    plt.scatter([0],[eq.subs(x,0)])
    plt.text(0,eq.subs(x,0)+1,"$\left("+latex(0)+r','+latex(eq.subs(x,0))+r"\right)$")
    plt.grid(True)

    d['fg']=fg
    d['ox']=list(zip(lista,imagenes))
    d['oy']=(0,eq.subs(x,0))

    return d


def dom_rec(eq,cte,var=x) :
    # Devuelve la gráfica de la ecuación y la recta, y los puntos de corte con la recta var=ctw
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
            # st.write(puntos)

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

                txt += "  \n * El punto $\left("+ latex(vx) + r"," +latex(vy) + r"\right)$ "+" pertenece a la gráfica $\\to "+latex(vx)+" \in Dom(f) \land "+latex(vy)+" \in Im(f)$  "

    return [fg,puntos, txt]
