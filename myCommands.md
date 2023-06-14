## commands i used for each exe:
### exe1:

````
docker build -t myimage .
docker run -e PORT=9090 myimage
````

### exe2:
````
docker build -t webserver .
docker run -d -p 8000:80  webserver
````
### exe3:
````
docker run -d -p 5000:5000 --restart always --name registry registry:2
docker ps
docker tag webserver localhost:5000/webserver
docker push localhost:5000/webserver
docker tag dockerfileimage  localhost:5000/dockerfileimage
docker push localhost:5000/dockerfileimage
docker pull localhost:5000/webserver
docker pull localhost:5000/dockerfileimage
````
### exe4:
````
docker build -t myimage .
docker run -e PORT=9090 myimage
````

### exe5:

````
docker run -v <your pass>:/www/data/index.html/ -d -p 8000:80  webserver
docker restart <container name>
````