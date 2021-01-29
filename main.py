import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from sympy import *
x, y, z, t = symbols('x y z t')

st.title('Mi primera aplicación')

sol=solve(x**2-2*x+1)

'Las soluciones son', sol

st.balloons()

st.help(pd.DataFrame)

st.sidebar.markdown('# Introducción')
