# JupyterLab Container with Pyspark with Elyra





### Custom JupyterLab Elyra container images

This repository containers **ready to go**:

**Container 1 : Pyspark 3.1.2 with Apache Hadoop 3.2:**

```
docker run -p 8888:8888 ruslanmv/pyspark-elyra:3.1.2
```



**Container 2 :  Pyspark 3.0.2 with Apache Hadoop 2.7:**

```
docker run  -p 8888:8888 ruslanmv/pyspark-elyra:3.0.2
```



The images are stored at the Docker Hub [here](https://hub.docker.com/repository/docker/ruslanmv/pyspark-elyra)

**Packages preinstalled:**



- [ibm-watson-machine-learning](http://ibm-wml-api-pyclient.mybluemix.net/#id564)

The `ibm-watson-machine-learning` Python library allows you to work with IBM Watson Machine Learning services. You can train, store, and deploy your models, score them using APIs, and finally integrate them with your application development. 

- [pyspark2pmml](https://github.com/jpmml/pyspark2pmml)

PySpark users should additionally install the `pyspark2pmml`package, which provides Python language wrappers for JPMML-SparkML public API classes and methods. 



### **Troubleshooting's**

**Could not install packages due to an EnvironmentError: [Errno 13] Permission denied:**

You are trying to install the package to a system folder which you don't have permissions to write to.
You have three options(use only one of them):
1-setup a virtual env to install the package **(recommended)**:

```
go to your termimnal
conda create -n env
conda activate env
pip install <your-new-package>
```



2-use sudo to install to the system folder **(not recommended)**
`sudo python -m pip install <your-new-package>`

but you need enter with root.

**Root password**

If you want to enter with **root**, you need run this command

```
docker run -p 8888:8888 -it --rm --user root -e GRANT_SUDO=yes ruslanmv/pyspark-elyra:3.0.2
```

Type the following command to become root user and issue passwd:

```
sudo -i passwd
```

you will get 

```
New password: 
Retype new password: 
passwd: password updated successfully
```

Test it your root password by typing the following command:

```
su -
```

or for example

```
sudo mkdir root
```

More information visit [ruslanmv.com](https://ruslanmv.com/blog/Docker-Container-with-Pyspark-and-Jupyter-and-Elyra)

