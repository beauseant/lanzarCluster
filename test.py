import sys
from typing import Tuple

from pyspark.rdd import RDD
from pyspark.sql import SparkSession
from Utils import Forlayo

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("PythonSort")\
        .getOrCreate()

    sc = spark.sparkContext

    print(sc.version)


    utils = Forlayo ()
    
    rdd = sc.textFile('file:///export/usuarios01/sblanco/lanzarCluster/data/texto.txt')

    rdd2 = utils.prueba (rdd)

    print (rdd2.collect())



    sc.stop()
