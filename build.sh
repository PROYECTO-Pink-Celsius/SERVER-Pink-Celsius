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

docker build --no-cache -t granja-api-v1:latest .
