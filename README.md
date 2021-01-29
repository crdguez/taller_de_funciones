# Probando Streamlit
Pues eso, pruebas de [streamlit](https://www.streamlit.io/)

Las pruebas las estoy haciendo mediante el fichero *main.py*

## Lanzando un docker con la aplicacion *main.py*

He creado un fichero *main.py* con el código de *streamlit*. Si no tengo el docker creado, lo creo con el siguiente comando:

```
docker run -it -p 8501:8501 -v $PWD:/app crdguez/streamlit main.py
```

## Viendo la aplicación *deployada* en el servicio de Streamlit

https://share.streamlit.io/crdguez/probando_streamlit/main/main.py

## Desplegada en *Google colab*

Ejecutar desde ahí el *notebook* que aparece en la raíz del repositorio,