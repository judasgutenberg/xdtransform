```
usage: xdtransform [-h] [-s SOURCE] [-d DESTINATION] -t TRANSFORM

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        The source XML file (you can specify - to mean stdin)
  -d DESTINATION, --destination DESTINATION
                        The destination XML file (you can specify - to mean stdout)
  -t TRANSFORM, --transform TRANSFORM
                        The transformation XML file
```


This version has some improvements over the 0.0.1 version in that it now does the deeper transforms required by MS Visual Studio configurations.
It also handles the "InsertIfMissing" transform type, which the stock version did not.

--Gus Mueller, June 2, 2022
