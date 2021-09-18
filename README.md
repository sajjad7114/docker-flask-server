# docker-flask-server
a flask server that can send images and find faces in that image.
I found the haarcascade_frontalface_default.xml file from https://github.com/opencv/opencv/tree/master/data/haarcascades
# Run
sudo docker build -t server:v3 .
sudo docker run --rm -p80:80 --name server -v ~/Desktop/pythonlab/project/server/app/volume:/app/volume server:v3
