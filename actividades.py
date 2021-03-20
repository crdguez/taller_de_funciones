# import streamlit as st
from libreria_funciones import *

import time

def app(tipo) :
    st.info(":exclamation: En **CONSTRUCCIÓN**")
    txt="Actividades del tipo de función: {}".format(tipo)
    st.title(txt)
    st.warning(':bell: Las actividades propuestas vienen con la solución sin mostrar. Se recomienda encarecidamente no \
        consultarla hasta que no se haya trabajado previamente. Se recomienda realizar las actividades con los \
        manipulables que aparecen en el apartado **Estudio de funciones** del menú.')
    # st.write(tipo)


    if tipo == 'lineal' :
        # Estudio de Parámetros
        st.info(":exclamation: **RECUERDA:** Las funciones *lineales* tienen una **expresión general** del tipo: $\\boxed{\\bm{y=mx+n}}$")
        st.header('**Actividad:** ¿Qué forma tienen las gráficas de las funciones lineales?')
        exp = x+1
        st.write('Toma, por ejemplo, la función $y='+latex(exp)+'$ \
          \n * Haz una tabla de valores \
          \n * Representa los puntos de la gráfica \
          \n * ¿Cómo se encuentran dichos puntos?¿Qué tipo de curva queda al unir los puntos?')
        with st.beta_expander('Ver solución') :

            st.write('Tienen forma de **línea recta**. \
              \n Por ejemplo: Si tomamos la función $y='+latex(exp)+'$ y representamos una tabla de valores  \
              vemos que los puntos de la gráfica están alineados:' )
            col01, col02 = st.beta_columns([1,3])
            d = tabla_valores(exp,tipo,9,4)
            with col01 :
                st.dataframe(d['df'])
            with col02 :
                st.pyplot(d['fg'])

        st.header('**Actividad:** ¿Cómo se comportan las funciones lineales al modificar el parámetro pendiente?')
        exp = 2*x-1
        lc, tc = Poly(exp,x).LC(), Poly(exp,x).TC()
        func=[exp, exp+x, exp-x, -lc*x+tc]
        st.write('Toma, por ejemplo, las funciones $y='+latex(func[0])+'$, $y='+latex(func[1])+'$ , $y='+latex(func[2])+'$ , $y='+latex(func[3])+'$ \
          \n * ¿Qué pendientes tienen las diferentes expresiones analíticas? \
          \n * Representa las funciones \
          \n * ¿Qué tienen en común todas las funciones? \
          \n * ¿Qué pasa al aumentar la pendiente?¿Y al disminuirla? \
          \n * ¿Qué pasa si el parámetro pendiente es negativo?')
        with st.beta_expander('Ver solución') :

            st.write('Todas las funciones son lineales y pasan por el punto $\\left(0,'+latex(Poly(exp,x).TC())+'\\right)$. \
              \n Las pendientes de las expresiones analíticas valen: '+",".join(map(latex,[Poly(i,x).LC() for i in func]))+" respectivamente.  \n \
              Se puede observar que al aumentar el valor absoluto de la pendiente aumenta la inclinación de la recta. Al revés, si disminuye \
              la inclinación también lo hace.   \n  \
              Por último, si la pendiente es positiva, la función es creciente. Pero si es negativa, la función es decreciente.")

            p=plot_implicit(Eq(y,func[0]), (x, -10, 10), (y, -10, 10),show = False)
            p.append(plot_implicit(Eq(y,func[1]), (x, -10, 10), (y, -10, 10), line_color='red')[0])
            p.append(plot_implicit(Eq(y,func[2]), (x, -10, 10), (y, -10, 10), line_color='green')[0])
            p.append(plot_implicit(Eq(y,func[3]), (x, -10, 10), (y, -10, 10), line_color='orange')[0])
            p.show()
            fg, ax = p._backend.fig, p._backend.ax
            plt.text(-9,9,"$y="+latex(nsimplify(func[0]))+"$",color='blue')
            plt.text(-9,8,"$y="+latex(nsimplify(func[1]))+"$",color='red')
            plt.text(-9,7,"$y="+latex(nsimplify(func[2]))+"$",color='green')
            plt.text(-9,6,"$y="+latex(nsimplify(func[3]))+"$",color='orange')
            ax[0].set_aspect('equal')

            plt.grid(True)
            st.pyplot(fg)

        # Ordenada en el origen
        st.header('**Actividad:** ¿Cómo se comportan las funciones lineales al modificar el parámetro pendiente?')
        exp = 2*x-1
        lc, tc = Poly(exp,x).LC(), Poly(exp,x).TC()
        func=[exp, exp+x, exp-x, -lc*x+tc]
        st.write('Toma, por ejemplo, las funciones $y='+latex(func[0])+'$, $y='+latex(func[1])+'$ , $y='+latex(func[2])+'$ , $y='+latex(func[3])+'$ \
          \n * ¿Qué pendientes tienen las diferentes expresiones analíticas? \
          \n * Representa las funciones \
          \n * ¿Qué tienen en común todas las funciones? \
          \n * ¿Qué pasa al aumentar la pendiente?¿Y al disminuirla? \
          \n * ¿Qué pasa si el parámetro pendiente es negativo?')
        with st.beta_expander('Ver solución') :

            st.write('Todas las funciones son lineales y pasan por el punto $\\left(0,'+latex(Poly(exp,x).TC())+'\\right)$. \
              \n Las pendientes de las expresiones analíticas valen: '+",".join(map(latex,[Poly(i,x).LC() for i in func]))+" respectivamente.  \n \
              Se puede observar que al aumentar el valor absoluto de la pendiente aumenta la inclinación de la recta. Al revés, si disminuye \
              la inclinación también lo hace.   \n  \
              Por último, si la pendiente es positiva, la función es creciente. Pero si es negativa, la función es decreciente.")

            p=plot_implicit(Eq(y,func[0]), (x, -10, 10), (y, -10, 10),show = False)
            p.append(plot_implicit(Eq(y,func[1]), (x, -10, 10), (y, -10, 10), line_color='red')[0])
            p.append(plot_implicit(Eq(y,func[2]), (x, -10, 10), (y, -10, 10), line_color='green')[0])
            p.append(plot_implicit(Eq(y,func[3]), (x, -10, 10), (y, -10, 10), line_color='orange')[0])
            p.show()
            fg, ax = p._backend.fig, p._backend.ax
            plt.text(-9,9,"$y="+latex(nsimplify(func[0]))+"$",color='blue')
            plt.text(-9,8,"$y="+latex(nsimplify(func[1]))+"$",color='red')
            plt.text(-9,7,"$y="+latex(nsimplify(func[2]))+"$",color='green')
            plt.text(-9,6,"$y="+latex(nsimplify(func[3]))+"$",color='orange')
            ax[0].set_aspect('equal')

            plt.grid(True)
            st.pyplot(fg)
