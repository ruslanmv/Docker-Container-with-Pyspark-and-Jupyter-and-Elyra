## Python runtime container image for Elyra with Pyspark

This container can have python 3.8 with Apache Spark 3.1.2 

```
docker run  ruslanmv/pyspark-runtime:3.1.2
```



It is a runtime  python3, This is needed to execute a airflow as a runtime

 https://elyra.readthedocs.io/en/v2.1.0/recipes/configure-airflow-as-a-runtime.html



```python
#Loading Spark
import findspark
findspark.init()
#Importing Spark
import sys
from pyspark.context import SparkContext
from pyspark import SQLContext, SparkConf
print(sys.version)
sc_conf = SparkConf()
sc = SparkContext(conf=sc_conf)
print(sc.version)
3.1.2
```



```
docker build --rm -t ruslanmv/pyspark-runtime  .
```

![](assets/images/posts/README/a1.jpg)

```
docker run -it ruslanmv/pyspark-runtime
```



![](assets/images/posts/README/a2.jpg)

```
docker tag   a3284357c099 ruslanmv/pyspark-runtime:3.1.2
```

```
docker push ruslanmv/pyspark-runtime:3.1.2
```

It is installed 

**ibm-watson-machine-learning**

**pyspark2pmml**

