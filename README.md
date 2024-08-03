# Proyecto de Conversión de Granja en un Sistema IoT

Este proyecto tiene como objetivo convertir una granja en un sistema IoT (Internet de las Cosas) que permita monitorear y controlar la temperatura de manera remota. El sistema IoT nos brindará la capacidad de supervisar la temperatura de la granja desde cualquier ubicación, lo que facilitará la gestión y el mantenimiento de las condiciones óptimas para el cultivo.

## Características principales

- Monitoreo remoto de temperatura: El sistema IoT recopilará datos de temperatura de diferentes áreas de la granja y los transmitirá a una plataforma centralizada para su visualización y análisis.
- Alertas y notificaciones: Se configurarán alertas automáticas que enviarán notificaciones en caso de que la temperatura supere ciertos límites establecidos.
- Control de temperatura: Se implementarán actuadores para controlar la temperatura en caso de que sea necesario, como la activación de ventiladores o sistemas de calefacción.
- Visualización de datos: Se proporcionará una interfaz intuitiva para visualizar los datos de temperatura en tiempo real, así como registros históricos para análisis y seguimiento.

## Levantar servicio
```sh
uvicorn main:app --reload
uvicorn main:app --host 192.168.1.200 --port 8000
nohup uvicorn main:app --host 0.0.0.0 --port 8666 > uvicorn.log 2>&1 &
```

## 1. Despliegue (Local)
```docker
# Actualizar el cliente
./build.sh
# Crear docker
docker build -t pink-server:latest .
# Comprimir docker
docker save -o pink-server.tar pink-server:latest
```
## 2. Despliegue (Server)
```docker
# Cargar docker
docker load -i mi-aplicacion.tar

# Desplegar docker
docker run -d -p 80:80 mi-aplicacion:latest
```
