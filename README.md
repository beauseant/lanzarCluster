# lanzarCluster

Ejemplo de como lanzar un script de PySpark en el cluster del TSC sin usar notebooks.

El código es una modificación de los scripts iniciales creados por https://github.com/hmolina

## Modificación 7 de Marzo 

Se ha añadido la posibilidad de pasar parámetros al script. En el ejemplo hay dos parámetros, uno con el path (-p) y otro de test (-t) Ambos obligatorios.


# 1) Generar token de acceso.

Antes de poder usar el cluster debemos tener un token de acceso, para ello debemos ir a:
https://www.tsc.uc3m.es/cluster_auth/get_token.php

Al token generado le quitamos los corchetes y se queda en un cadena de texto que grabamos en el lugar que queramos lanzar el script.

En este ejemplo lo he llamado tokencluster.json y está vacío, puedes rellenarlo con el que deses.

# 2) Definir el PATH de python.

Este paso sólo es necesario si se usan clases adicionales, como es el caso de este ejemplo. Para ello debemos modificar el PATH de python para que pueda leerlas.

Es importante que el directorio donde se guarda la clase sea una ruta que pueda leerse por cualquier nodo del cluster. Es decir, debemos usar bien usuarios01, bien ml4ds.

En el caso de este ejemplo estamos usando la ruta de /export/usuarios01/sblanco, que esta definida como HOME, por lo que debemos escribir en la consola el siguiente comando:

export PYTHONPATH=${PYTHONPATH}:${HOME}/lanzarCluster/includes/

Si estamos usando, por ejemplo, usuarios_ml4ds, sería:

export PYTHONPATH=${PYTHONPATH}:/export/usuarios_ml4ds/sblanco/lanzarCluster/includes/

La consola en la que se define esa variable debe ser la misma en la que se lanzará el script, no se puede abrir una consola, modificar la variable y luego lanzar en otra pestaña o consola.


# 3) Definir el PATH de los datos.

El ejemplo propuesto lee un fichero de texto en la línea número 21 del fichero test.py. Ese fichero tiene un ruta local (no hdfs) al fichero de datos, debe modificarse al gusto del usuario.


# 4) Lanzar el script.

### 4.1 Sin usar notebook.

Con todos los pasos anteriores listos ya estamos en condiciones de lanzar el código. En la misma consola que hemos definido el path de python nos dirijimos al directorio del proyecto y escribimos el comando:

./launch-spark  -C tokencluster.json -c 4 -N 10  -S test.py -P "-p file:///export/usuarios01/sblanco/lanzarCluster/data/texto.txt -t test"

Donde script_spark es el script de Linux que prepara el entorno, tokencluster.json es el fichero con el token y test.py es el programa principal. En este caso estamos lanzando 10 máquinas con 4 hilos de ejecución en cada una.

Evidentemente el script debe lanzarse desde alguna de las máquinas con acceso al cluster. En el caso del grupo ML4DS el lugar obvio es usar cualquiera de las hators.

Para especificar la arquitectura a usar, se ha agregado la opcion -X
./script-spark  -C tokencluster.json -c 4 -N 10  -S test.py -P "-p file:///export/usuarios01/sblanco/lanzarCluster/data/texto.txt -t test" -X "cpu_arch:ARCH"

Donde los valores de arch son (de más antiguo a nuevo):
* core2
* nehalem
* westmere
* sandybridge
* ivybridge
* broadwell
* cascadelake

NO abusar de esta opcion

### 4.2 Usando notebook.

Si lo que queremos es usar un notebook para tener sesiones interactivas debemos lanzar el script de la siguiente forma:

./launch-spark  -C tokencluster.json -c 4 -N 10 -j 

Una vez lanzado se muestran una serie de mensajes en la pantalla y, entre ellos, aparece un mensaje con las direcciones que debemos usar para nuestro notebook:

[I 2023-09-08 10:17:33.260 ServerApp] http://hator05.tsc.uc3m.es:8888/lab
[I 2023-09-08 10:17:33.260 ServerApp]     http://127.0.0.1:8888/lab
[I 2023-09-08 10:17:33.261 ServerApp] Use Control-C to stop this server

La importante es http://hator05.tsc.uc3m.es:8888/lab, si ponemos esa dirección en el navegador ya tenemos acceso a un notebook interactivo donde podemos crear el entorno de spark:

 spark = SparkSession\
        .builder\
        .appName("Nombre de la APP")\
        .getOrCreate()

    sc = spark.sparkContext


# 5) Comprobar ejecución.

Para ver la ejecución de nuestro script debemos ir a una de las siguientes direcciones (probar la que funcione):
   
https://subserver1.tsc.uc3m.es:5050

https://subserver2.tsc.uc3m.es:5050

https://subserver3.tsc.uc3m.es:5050

https://subserver4.tsc.uc3m.es:5050

https://subserver5.tsc.uc3m.es:5050





