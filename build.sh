#!/bin/bash

SERVER="/home/pctorre/projects/Pink-Celsius/SERVER-Pink-Celsius"
CLIENTE="/home/pctorre/projects/Pink-Celsius/CLIENT-Pink-Celsius"

echo -e "\n     ---- Compilar react ---- "
cd $CLIENTE
npm run build

echo -e "\n     ---- Borrar anteriores ---- "
rm -r "$SERVER/static"
rm "$SERVER/templates/index.html"

echo -e "\n     ---- Mover ficheros ---- "
cp -r "$CLIENTE/dist/static" "$SERVER"
cp "$CLIENTE/dist/index.html" "$SERVER/templates"