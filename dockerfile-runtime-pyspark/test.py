
import findspark
findspark.init()
import sys
from pyspark.context import SparkContext
from pyspark import SQLContext, SparkConf
print(sys.version)
sc_conf = SparkConf()
sc = SparkContext(conf=sc_conf)
print(sc.version)
