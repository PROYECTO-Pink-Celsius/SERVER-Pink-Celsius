# Proyecto de Conversión de Granja en un Sistema IoT

Este proyecto tiene como objetivo convertir una granja en un sistema IoT (Internet de las Cosas) que permita monitorear y controlar la temperatura de manera remota. El sistema IoT nos brindará la capacidad de supervisar la temperatura de la granja desde cualquier ubicación, lo que facilitará la gestión y el mantenimiento de las condiciones óptimas para el cultivo.

## python verion: 3.13

#### 1. Crear un entorno
```
virtualenv -p python3.13 myenv
```
#### 2. Activar el entorno

```
source myenv/bin/activate 
```
#### 3. Instalar dependencias
```
pip install -r requirements.txt 
```
#### 4. Lanzar el servidor
```
python -m uvicorn main:app --reload
```
#### 4.1 Opcion para indicar puerto
```
uvicorn main:app --host 192.168.1.133 --port 9876
```