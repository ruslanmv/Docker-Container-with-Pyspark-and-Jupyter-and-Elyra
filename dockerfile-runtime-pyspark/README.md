# Runtime image Container with Pyspark for Elyra 

A runtime image configuration identifies a container image that Elyra can utilize to run pipeline nodes on container-based platforms, such as Kubeflow Pipelines or Apache Airflow.



A runtime image configuration is associated with a container image that must meet these prerequisites:

- The image is stored in a container registry in a public or private network that the container platform in which the pipeline is executed can connect to. Examples of such registries are [hub.docker.com](https://hub.docker.com/) or a self-managed registry in an intranet environment.
- The image must have a current `Python 3` version pre-installed and `python3` in the search path.
- The image must have `curl` pre-installed and in the search path.



A runtime image provides the execution environment in which nodes are executed when a Jupyter notebook is processed as part of a pipeline. Elyra includes a number of runtime images for popular configurations, such as TensorFlow or Pytorch.

Should none of these images meet your needs, you can utilize a custom container image, as long as it meets the following pre-requisites:

- The image is stored in a container registry in a public or private network that the container platform in which the pipeline is executed can connect to. Examples of such registries are [hub.docker.com](https://hub.docker.com/) or a self-managed registry in an intranet environment.
- The image can be pulled from the registry without the need to authenticate.
- [Python 3](https://www.python.org/) is pre-installed and in the search path. Python versions that have reached their “end of life” are not supported.
- [`curl`](https://curl.haxx.se/) is pre-installed and in the search path.

### Custom JupyterLab Elyra container images

This repository has three containers **ready to go**:

**Container 1 : Pyspark 3.1.2 with Apache Hadoop 3.2:**

```
docker run  ruslanmv/pyspark-runtime:3.1.2
```



**Container 2 :  Pyspark 3.0.2 with Apache Hadoop 2.7:**

```
docker run  ruslanmv/pyspark-runtime:3.0.2
```



The images are stored at the Docker Hub [here](https://hub.docker.com/repository/docker/ruslanmv/pyspark-elyra)

**Packages installed:**



- [ibm-watson-machine-learning](http://ibm-wml-api-pyclient.mybluemix.net/#id564)

The `ibm-watson-machine-learning` Python library allows you to work with IBM Watson Machine Learning services. You can train, store, and deploy your models, score them using APIs, and finally integrate them with your application development. 

- [pyspark2pmml](https://github.com/jpmml/pyspark2pmml)

PySpark users should additionally install the `pyspark2pmml`package, which provides Python language wrappers for JPMML-SparkML public API classes and methods. 





More information visit [ruslanmv.com](https://ruslanmv.com/blog/Docker-Container-with-Pyspark-and-Jupyter-and-Elyra)

