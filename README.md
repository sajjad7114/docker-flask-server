# docker-flask-server
a flask server that can send images and find faces in that image.
# Run
sudo docker build -t server:v3 .
sudo docker run --rm -p80:80 --name server -v ~/Desktop/pythonlab/project/server/app/volume:/app/volume server:v3
