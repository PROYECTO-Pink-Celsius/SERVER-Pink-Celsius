#!/bin/bash

SERVER="."
WEB="../CLIENT-Pink-Celsius"
#######################################
#
# COMPILAR WEB
#
#######################################
echo -e "\n\n---- Compilar react ----\n"
npm --prefix "./$WEB" run build


echo -e "\n\n---- Borrar anteriores ----\n"
rm -r "$SERVER/static"
rm "$SERVER/templates/index.html"

echo -e "\n\n---- Mover ficheros ----\n"
cp -r "$WEB/dist/static" "$SERVER/static"
cp "$WEB/dist/index.html" "$SERVER/templates"

#######################################
#
# COMPILAR DOCKER
#
#######################################

docker buildx build --platform linux/arm64 --load -t granja-api-v1:latest .

docker save -o granja-api-v1.tar granja-api-v1

echo -e "\n\n---- Enviando imagen ----\n"

scp granja-api-v1.tar pi-server:/home/pi/granja

