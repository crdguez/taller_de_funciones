import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from sympy import *

x, y, z, t = symbols('x y z t')



st.title('Mi primera aplicación')

latex(x**2+3)

st.balloons()

st.help(pd.DataFrame)

st.sidebar.markdown('# Introducción')
