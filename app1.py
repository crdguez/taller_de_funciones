from libreria_funciones import *

def app(funcion) :
    ex, eq, md, title = funcion['tex'],funcion['eq'],funcion['md'],funcion['title']
    tipo = funcion['tipo']

    d = carac(eq, tipo)

    st.title(title)
    st.write(md)
    st.markdown("**Ejemplo:**")
    st.latex("f(x)="+latex(eq))

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


    #Estudio de la forma de la función

    st.subheader('Estudiando su forma')

    st.write('Vamos a hacer una **tabla de valores** y representamos \
        los puntos del plano correspondientes:')

    p=st.select_slider('Número de puntos', options=[10,20,50])
    col31, col32 = st.beta_columns(2)

    with col31 :
        lista=np.linspace(-2,2,p)
        if tipo == 'lineal' and poly(d['exp'],x).degree() == 0 :
        # if tipo == 'lineal'  :
            lista2 = [eq for i in lista]
        else :
            lista2 = lambdify(x,eq)(lista)
        st.dataframe(pd.DataFrame({'x':lista,'y':lista2}))

    with col32:
        p3 = plot_implicit(Eq(y,eq), (x, -3, 3), (y, -10, 10),line_color='yellow')
        fig = p3._backend.fig
        plt.scatter(lista,lista2)
        st.pyplot(fig)


    # Estudio del dominio y el Recorrido

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


    #Estudio de la función en cuestión

    if tipo == 'lineal' :
        # graficamos la Pendiente
        st.subheader('Estudiando la pendiente y la ordenada')
        x0 = int(st.select_slider('x0', options=[2,4,6]))
        x1 = int(st.select_slider('x1', options=[8,10,12]))
        d1=pendiente_ordenada(eq,x0,x1)
        st.pyplot(d1['fg'])
        st.markdown(d1['md1'])

    if tipo == 'cuadratica' :
        # graficamos la Pendiente
        st.subheader('Estudiando el vértice de la función cuadrática')
        d2=max_min(eq)
        st.pyplot(d2['fg'])
        # st.markdown(d1['md1'])
        txt = "Observa que el **vértice** tiene de coordenadas $\\left(\\frac{-b}{2a},f\\left(\\frac{-b}{2a}\\right)\\right)$: \
           \n  * Primera coordenada: \
            $\\frac{-b}{2a}=\\frac{"+latex(-1*Poly(eq,x).all_coeffs()[1])+"}{2\\cdot\\left("+latex(Poly(eq,x).all_coeffs()[0])+"\\right)}="
        txt += latex(-1*Poly(eq,x).all_coeffs()[1]/(2*Poly(eq,x).all_coeffs()[0]))+"$."
        txt += "  \n * Segunda coordenada:  \n"
        txt += "$"+latex(eq.subs(x,UnevaluatedExpr(d2['maxmin'][0])))+"="+latex(eq.subs(x,d2['maxmin'][0]))+"$"
        st.info(txt)
