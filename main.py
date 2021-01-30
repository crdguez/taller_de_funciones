import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sympy.parsing.latex import parse_latex
from sympy import *
x, y, z, t = symbols('x y z t')

st.title('Mi primera aplicación')

st.markdown('### Ejemplo de uso de $\LaTeX$')

#sol=solve(x**2-2*x+1)

eq=r'x^2-2x+1'
eq=r'x^2-4'

#r'Las soluciones de $$'+ eq +r'$$ son: '+r'$'+latex(solve(parse_latex(eq)))+r'$'

r'Las ráices de $$'+ eq +r'$$ son: '+r'$'+', '.join(map(latex,solve(parse_latex(eq))))+r'$'

st.pyplot(plot_implicit(Eq(y,x**2)))


st.balloons()

#st.help(pd.DataFrame)

st.sidebar.markdown('# Introducción')
