import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sympy.parsing.latex import parse_latex
from sympy import *
x, y, z, t = symbols('x y z t')

st.balloons()

st.title('Mi primera aplicación')

st.markdown('### Ejemplo de uso de $\LaTeX$')

#sol=solve(x**2-2*x+1)
sz=5
a = st.select_slider('a',options=list(range(-1*sz,sz+1)))
st.write('El paraḿetro a es: ', a)

eq=r'x^2-2x+1'
eq=r'ax^2-4'.replace('a',latex(a))


#r'Las soluciones de $$'+ eq +r'$$ son: '+r'$'+latex(solve(parse_latex(eq)))+r'$'

r'Las raíces de $$'+ eq +r'$$ son: '+r'$'+', '.join(map(latex,solve(parse_latex(eq))))+r'$'

p1 = plot_implicit(Eq(y,parse_latex(eq)))
fg =  p1._backend.fig
st.pyplot(fg)





#st.help(pd.DataFrame)

st.sidebar.markdown('# Introducción')
