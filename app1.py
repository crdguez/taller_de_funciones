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
from sympy.calculus.util import continuous_domain, function_range

#init_session()
#continuous_domain(log(x,2),x,S.Reals)

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
    ex, eq, md, title = funcion['tex'],funcion['eq'],funcion['md'],funcion['title']
    tipo = funcion['tipo']

    d = carac(eq, tipo)

    st.title(title)
    st.write(md)
    st.markdown("**Ejemplo:**")
    st.latex("f(x)="+latex(eq))

    # graficamos la Pendiente

    x0, x1 = 5, 8
    lista=[x0,x1]
    lista.append(0)
    imagen=lambdify(x,eq)(np.array(lista))
    p2 = plot(eq)
    p2.append(List2DSeries([x0,x1,x1],[imagen[0],imagen[0],imagen[1]]))
    p2.show()
    [plt.text(i,eq.subs(x,i)+1,"$\left("+latex(i)+r','+latex(eq.subs(x,i))+r"\right)$") for i in lista]
    plt.text((x0+x1)/2,imagen[0],"$"+latex(x1-x0)+"$")
    plt.text(x1,imagen[0],r"$m=\frac{"+latex(S(imagen[1]-imagen[0]))+r"}{"+latex(x1-x0)+r"}="+latex((S(imagen[1]-imagen[0]))/(x1-x0))+"$")
    # plt.text(x1,(imagen[1]+imagen[0])/2,"$"+latex(imagen[1]-imagen[0])+"$")
    plt.text(x1,(imagen[1]+imagen[0])/2,"$"+latex(S(imagen[1]-imagen[0]))+"$")

    fg=p2._backend.fig
    # plt.scatter(lista,lambdify(x,eq)(np.array(lista))
    plt.scatter(lista,imagen)

    # plt.text(x0+2,eq.subs(x,x0)+1,'a ver')
    # r'$\left('+latex(x0)+r","ĺatex(eq.subs(x,x0))+r"\right)$"

    st.pyplot(fg)

    col11, col12 = st.beta_columns([1,1])

    with col11 :
        corte_x = ' No tiene' if len(list(solveset(eq, domain=S.Reals))) == 0 else "$"+", ".join(map(latex,d['raices']))+"$"
        st.write("**Características**:  \n  $f(x) ="+ \
            latex(d['exp'])+"$   \n * Corte OX: "+corte_x+ \
            "  \n * Corte OY: $"+latex(d['oy'])+ \
            "$  \n * Dominio: $"+latex(d['dominio'])+"$ \
              \n * Recorrido: $"+latex(d['rango'])+"$")

        for k,v in d['extra'].items() :
            st.markdown(k + r' $\to$ ' + v)

    with col12 :
        # Graficamos la función
        st.pyplot(d['fg'])

    st.subheader('Estudiando su forma')

    st.write('Vamos a hacer una **tabla de valores** y representamos \
        los puntos del plano correspondientes:')

    p=st.select_slider('Número de puntos', options=[10,20,50])
    col31, col32 = st.beta_columns(2)

    with col31 :
        lista=np.arange(-2,2.2,0.2)
        lista=np.linspace(-2,2,p)
        fu=lambdify(x,eq)
        # st.table(pd.DataFrame({'x':lista,'y':fu(lista)},index=False))
        # st.dataframe(pd.DataFrame({'x':lista,'y':fu(lista)}),width=500,height=400)
        st.dataframe(pd.DataFrame({'x':lista,'y':fu(lista)}))


    with col32:
        p3 = plot_implicit(Eq(y,eq), (x, -3, 3), (y, -10, 10),line_color='yellow')
        fig = p3._backend.fig
        plt.scatter(lista,fu(lista))
        st.pyplot(fig)



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
