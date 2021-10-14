# JupyterLab Container with Pyspark with Elyra





### Custom JupyterLab Elyra container images

This repository containers **ready to go**:

**Container 1 : Pyspark 3.1.2 with Apache Hadoop 3.2:**

```
docker run  ruslanmv/pyspark-elyra:3.1.2
```



**Container 2 :  Pyspark 3.0.2 with Apache Hadoop 2.7:**

```
docker run  ruslanmv/pyspark-elyra:3.0.2
```



The images are stored at the Docker Hub [here](https://hub.docker.com/repository/docker/ruslanmv/pyspark-elyra)

**Packages installed:**



- [ibm-watson-machine-learning](http://ibm-wml-api-pyclient.mybluemix.net/#id564)

The `ibm-watson-machine-learning` Python library allows you to work with IBM Watson Machine Learning services. You can train, store, and deploy your models, score them using APIs, and finally integrate them with your application development. 

- [pyspark2pmml](https://github.com/jpmml/pyspark2pmml)

PySpark users should additionally install the `pyspark2pmml`package, which provides Python language wrappers for JPMML-SparkML public API classes and methods. 





More information visit [ruslanmv.com](https://ruslanmv.com/blog/Docker-Container-with-Pyspark-and-Jupyter-and-Elyra)

