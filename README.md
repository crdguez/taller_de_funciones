# Probando Streamlit

Pues eso, pruebas de [streamlit](https://www.streamlit.io/)

Las pruebas las estoy haciendo en el fichero *main.py*. Podemos lanzar la aplicación de diferentes maneras:


## Lanzando un contendor docker con Streamlit y la aplicacion *main.py*

He creado un fichero *main.py* con el código de *streamlit*. Si no tengo el docker creado, lo creo con el siguiente comando:

```
docker run -it -p 8501:8501 -v $PWD:/app crdguez/streamlit main.py
```

Para que funcione deberá lanzarse desde la ruta donde esté el fichero *main.py*

Si está creado aparecerá al ejecutar:

```
docker ps -a
```

Si aparece *stopped* lo levantamos con el comando

```
docker start nombre_contenedor
```
Si queremos abrir un terminal en modo root del contenedor:

```
docker exec -it -u 0 nombre_contenedor /bin/bash
```

### Modificar la imagen docker *crdguez/streamlit*

EL fichero *Dockerfile* y *requirements.txt* contienen la información para crear la imagen docker. Se pueden modificar los fichero a gusto del consumidor.

Para generar la imagen utilizamos este comando o similar:

```
docker build -t usuario_docker_hub/streamlit .
```

## Viendo la aplicación *deployada* en el servicio de Streamlit

https://share.streamlit.io/crdguez/probando_streamlit/main/main.py

## Desplegada en *Google colab*

Para ello ejecutamos desde *Google colab* el *notebook* que aparece en la raíz del repositorio
