# lanzarCluster

Ejemplo de como lanzar un script de PySpark en el cluster del TSC sin usar notebooks.

El código es una modificación de los scripts iniciales creados por https://github.com/hmolina

## Generar token de acceso.

Antes de poder usar el cluster debemos tener un token de acceso, para ello debemos ir a:
https://www.tsc.uc3m.es/cluster_auth/get_token.php

Al token generado le quitamos los corchetes y se queda en un cadena de texto que grabamos en el lugar que queramos lanzar el script.

En este ejemplo lo he llamado tokencluster.json y está vacío, puedes rellenarlo con el que deses.

## Definir el PATH de python.

Si se usan clases adicionales, como es el caso de este ejemplo, debemos modificar el PATH de python para que pueda leerlas.

Es importante que el directorio donde se guarda la clase sea una ruta que pueda leerse por cualquier nodo del cluster. Es decir, debemos usar bien usuarios01, bien ml4ds.

En el caso de este ejemplo estamos usando la ruta de /export/usuarios01/sblanco, que esta definida como HOME, por lo que debemos escribir en la consola el siguiente comando:

export PYTHONPATH=${PYTHONPATH}:${HOME}/lanzarCluster/includes/

Si estamos usando, por ejemplo, usuarios_ml4ds, sería:

export PYTHONPATH=${PYTHONPATH}:/export/usuarios_ml4ds/sblanco/lanzarCluster/includes/

La consola en la que se define esa variable debe ser la misma en la que se lanzará el script, no se puede abrir una consola, modificar la variable y luego lanzar en otra pestaña o consola.


## Definir el PATH de los datos.

El ejemplo propuesto lee un fichero de texto en la línea número 21 del fichero test.py. Ese fichero tiene un ruta local (no hdfs) al fichero de datos, debe modificarse al gusto del usuario.


## Lanzar el script.

Con todos los pasos anteriores listos ya estamos en condiciones de lanzar el código. En la misma consola que hemos definido el path de python nos dirijimos al directorio del proyecto y escribimos el comando:

./script-spark  -C tokencluster.json -c 4 -N 10  -S test.py 

Donde script_spark es el script de Linux que prepara el entorno, tokencluster.json es el fichero con el token y test.py es el programa principal. En este caso estamos lanzando 10 máquinas con 4 hilos de ejecución en cada una.

Evidentemente el script debe lanzarse desde alguna de las máquinas con acceso al cluster. En el caso del grupo ML4DS el lugar obvio es usar cualquiera de las hators.



