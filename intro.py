# intro.py
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

def app() :
    st.title('Laboratorio de Funciones')
    # image = Image.open('img/parabolas_red.jpg')
    # st.image(image, caption='Photo by Ricardo Gomez Angel', use_column_width=True)
    image = Image.open('img/parabolas2_red.jpg')
    st.image(image, caption='foto de Johannes Groll (https://unsplash.com/photos/mrIaqKh9050)', use_column_width=False)

    # Photo by Johannes Groll on Unsplash
    st.write('EL siguiente material es un conjunto de \
    manipulables para el **estudio de las funciones**.   ',\
    '  \n El material está pensado para niveles de **4ºESO** o **primero de Bachillerato**.')
    # st.markdown('### Ejemplo de uso de $\LaTeX$')
    # components.iframe("https://www.heraldo.es/", scrolling = True)
    st.subheader('Instrucciones')
    st.write('La aplicación es bastante intuitiva.  \n Simplemente \
    hay que desplegar el menú de la izquierda y seleccionar el tipo de función \
    que se quiera estudiar. Al hacerlo apareceran unos deslizadores \
    correspondientes a los parámetros generales \
    del tipo de función.')

    # st.markdown('![instrucciones](./instrucciones.gif)')
    # image = Image.open('instrucciones.gif')
    # st.image(image)
    # st.markdown("![Alt Text](instrucciones)")
    # st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
    st.image('./instrucciones.gif')

    st.subheader('Sobre el proyecto')
    st.markdown('- Autor: *Carlos Rodríguez*  \n - [Repo *Github*](https://github.com/crdguez/probando_streamlit)' )
    st.subheader('Licencia')
    st.write('Tanto el código como la aplicación se publican con **licencia libre**. \
      \n * En caso de uso, se agradece la atribución \
        \n * Así mismo, se agradecen sugerencias y contribuciones \
        a través de *pull requests* en el repositorio')
