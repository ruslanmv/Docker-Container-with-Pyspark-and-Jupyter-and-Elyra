## Simple docker with Python 3.8



This is example to run simple test.py file with your docker container

```
import sys
print(sys.version)
```

You simply build it

```
docker build --rm -t ruslanmv/python
```

and run it

```
docker run -it ruslanmv/python test.py
```

the output

```
3.8.12 (default, Oct 13 2021, 09:15:35)
[GCC 10.2.1 20210110]
```

Great!