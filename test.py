import sys
from typing import Tuple

from pyspark.rdd import RDD
from pyspark.sql import SparkSession
from Utils import Forlayo
import argparse



if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("PythonSort")\
        .getOrCreate()

    sc = spark.sparkContext

    print(sc.version)

    parser = argparse.ArgumentParser(description='Script de ejemplo para lanzar en el cluster')
    parser.add_argument('-p', '--path', help='ruta con el fichero', type=str, required=True)
    parser.add_argument('-t', '--test', help='un parametro de test', type=str, required=True)
    arg = parser.parse_args()


    utils = Forlayo ()
    
    #rdd = sc.textFile('file:///export/usuarios01/sblanco/lanzarCluster/data/texto.txt')
    rdd = sc.textFile ( arg.path )

    rdd2 = utils.prueba (rdd)

    print (rdd2.collect())



    sc.stop()
