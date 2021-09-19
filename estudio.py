from libreria_funciones import *

def app(funcion) :
    ex, eq, md, title, tipo = funcion['tex'],funcion['eq'],funcion['md'],funcion['title'],funcion['tipo']

    d = carac(eq, tipo)

    st.title(title)
    st.info(md)
    st.markdown("**Ejemplo:**")
    tex = "\\boxed{y="+latex(d['exp'])+"\\to y="+latex(simplify(d['exp']))+"}" if tipo == 'prop_inversa' else "\\boxed{y="+latex(d['exp'])+"}"
    st.latex(tex)
    st.warning(":point_left: :point_left: :point_left: Puedes cambiar de ejemplo modificando los **parámetros** de la función desde el **menú desplegable de la izquierda**")
    st.write(":unlock: Vamos a ver cómo se comporta la función ejemplo:")
    col11, col12 = st.columns([1,2])

    with col11 :
        # corte_x = ' No tiene' if len(list(solveset(eq, domain=S.Reals))) == 0 else "$"+", ".join(map(latex,d['raices']))+"$"
        corte_x = ' No tiene' if len(list(solveset(eq, domain=S.Reals))) == 0 else "$"+", ".join(['({},0)'.format(latex(i)) for i in d['raices']])+"$"
        txt_carac = "**Características de ** $y="+ \
            latex(d['exp'])+"$   \n * Corte OX: "+corte_x+ \
            "  \n * Corte OY: $"+latex(d['oy'])+ \
            "$  \n * Dominio: $"+latex(d['dominio'])+"$ \
              \n * Recorrido: $"+latex(d['rango'])+"$"
        for k,v in d['extra'].items() :
#             txt_carac +="  \n * "+str(k) + r': $'+ latex(v) +"$ "
            txt_carac +="  \n * "+str(k) + r': '+ str(v)
            # st.markdown(k + r' $\to$ ' + v)
        st.write(txt_carac)

    with col12 :
        # Graficamos la función
        st.pyplot(d['fg'])


    #Estudio de la forma de la función

    st.subheader('Estudiando la forma de la gráfica de $y='+latex(eq)+"$")

    st.write('Vamos a hacer una **tabla de valores** y representamos \
        los puntos del plano correspondientes:')


    # p=st.select_slider('Selecciona el número de puntos que se representarán', options=[10,20,50])
    p=st.selectbox('Selecciona el número de puntos que se representarán', (10,20,50))
    st.write("Dando valores a la variable **x** y sustituyendo en la expresión $"+latex(d['exp'])+"$, obtenemos los valores de la **y**:")

    col31, col32 = st.columns([1,3])
    d5 = tabla_valores(eq,tipo,p,2)
    with col31 :

        st.dataframe(d5['df'])

        # lista=np.linspace(0.0001,2,p) if tipo == 'logaritmica' else np.linspace(-2,2,p)
        # if tipo == 'lineal' and poly(d['exp'],x).degree() == 0 :
        # # if tipo == 'lineal'  :
        #     lista2 = [eq for i in lista]
        # else :
        #     # lista2 = lambdify(x,eq)(lista)
        #     lista2 = [eq.subs(x,i) for i in lista]
        # st.dataframe(pd.DataFrame({'x':lista,'y':lista2}))


    with col32 :
        # p3 = plot_implicit(Eq(y,eq), (x, -3, 3), (y, -10, 10),line_color='yellow')
        # fig = p3._backend.fig
        # plt.scatter(lista,lista2)
        # st.pyplot(fig)

        st.pyplot(d5['fg'])

    if 'forma' in d:
        st.write(':white_check_mark: Observa que:')
        st.success(d['forma'])



    # Estudio del dominio y el Recorrido

    st.subheader('Estudiando el dominio y recorrido de $y='+latex(eq)+"$")

    st.write("Modifica los actuadores para comprobar si un valor determinado pertenece al dominio o al recorrido")

    col21, col22= st.columns([1,4])
    with col21 :
        var=y if st.radio('Selecciona:',('Dominio','Recorrido')) == 'Recorrido' else x
        cte = st.select_slider(str(var),options=list(np.arange(-3,3.25,0.25)),value=1)
        fg, puntos, txt = dom_rec(eq,cte,var)
    with col22 :
        st.pyplot(fg)
    st.markdown(txt)
    st.write(':white_check_mark: Observa que:')
    st.info("\
      \n * El dominio es $"+latex(d['dominio'])+"$ \
      \n * El recorrido es $"+latex(d['rango'])+"$")




    #Estudio de la función en cuestión

    if tipo == 'lineal' :
        # graficamos la Pendiente
        st.subheader('Estudiando la pendiente y la ordenada de $y='+latex(eq)+"$")
        st.write('Modifica los deslizadores para seleccionar puntos diferentes de la recta:')
        col31, col32 = st.columns([1,4])
        with col31 :
            x0 = int(st.select_slider('x0', options=[2,4,6]))
            x1 = int(st.select_slider('x1', options=[8,10,12]))
            d1=pendiente_ordenada(eq,x0,x1)
        with col32 :
            st.pyplot(d1['fg'])
        st.write(':white_check_mark: Observa que:')
        st.info(d1['md1'])

    if tipo == 'cuadratica' :
        # Dibujamos el vértice
        st.subheader('Estudiando el vértice de la función cuadrática de $y='+latex(eq)+"$")
        d2=max_min(eq)
        st.pyplot(d2['fg'])
        # st.markdown(d1['md1'])
        st.write(':white_check_mark: Observa que:')
        txt = " *  El **vértice** tiene de coordenadas $\\left(\\frac{-b}{2a},f\\left(\\frac{-b}{2a}\\right)\\right)$: \
           \n  * Primera coordenada: \
            $\\frac{-b}{2a}=\\frac{"+latex(-1*Poly(eq,x).all_coeffs()[1])+"}{2\\cdot\\left("+latex(Poly(eq,x).all_coeffs()[0])+"\\right)}="
        txt += latex(-1*Poly(eq,x).all_coeffs()[1]/(2*Poly(eq,x).all_coeffs()[0]))+"$."
        txt += "  \n * Segunda coordenada:  \n"
        txt += "$"+latex(eq.subs(x,UnevaluatedExpr(d2['maxmin'][0])))+"="+latex(eq.subs(x,d2['maxmin'][0]))+"$"
        txt += "  \n * Por tanto, el vértice se encuentra en el punto: "+d['extra']['Vértice']+""
        st.info(txt)

        # Cortes con los ejes
        st.subheader('Estudiando los cortes con los ejes de $y='+latex(eq)+"$" )

        cort=cortes(eq)
        st.pyplot(cort['fg'])
        txt="Puntos de cortes con los ejes:"

        # for i in cort['ox'] :
        #     txt += "  \n * $"+latex(i)+"$"
        if len(cort['ox']) != 0 :
            txt += "  \n * Cortes OX: $"+"$, $".join(list(map(latex, cort['ox'])))+"$"
        txt += "  \n * Cortes OY: $"+latex(cort['oy'])+"$"
        st.write(txt)

        st.write(':white_check_mark: Observa que en general:')
        st.info(':paperclip: Dependiendo de los valores de los parámetros **a**, **b**, **c** \
        el vértice puede estar por debajo, por arriba o en \
        el mismo eje. Según la orientación de la parábola, esto nos dará **0, 2 o 1** corte con el eje **OX** ')
        st.write("Modifica los parámetros en el menú de la izquierda para comprobarlo. Puedes probar con $y=x^2$ \
            , $y=x^2+1$ y $y=x^2-1$. ¿Cuántos cortes con los ejes aparecen?"  )
        st.info(':paperclip: Con el eje **OY** siempre habrá un corte con el eje y además viene determinado por el parámetro **c**: $\\left(0,c\\right)$ \
        ')

    if tipo == 'prop_inversa' :
        # Paso encontrar la expresión general a partir de la reducida
        st.subheader('Encontrar la expresión general de $y='+latex(simplify(eq))+"$")
        st.write('Recuerda la **Propiedad Fundamental de la División**:')
        st.success(':key:  $\\boxed{\\bm{D=d\cdot c +r}} \\to \\dfrac{D}{d}=c+\\dfrac{r}{d}$')
        n,d = fraction(simplify(eq))
        c,r = pdiv(n,d)
        st.write('Si dividimos $'+latex(n)+"$ entre $"+latex(d)+"$ obtenemos: \
              \n  * Cociente:  $"+latex(c)+"$ y Resto: $"+latex(r)+"$ \
              \n  * Aplicando la propiedad fundamental:  \n   \t * $\\dfrac{"+latex(n)+"}{"+latex(d)+"}=  \
              "+latex(c)+"+\\dfrac{"+latex(r)+"}{"+latex(d)+"}$ \
              \n * Por tanto, tendremos la siguiente **expresión general**: $\\boxed{\\bm{y="+latex(eq).replace('frac','dfrac')+"}}$" )
