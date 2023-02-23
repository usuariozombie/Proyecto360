# Proyecto360
Aplicación para el Proyecto 360º de Sistemas Informáticos para 1º de Desarrollo de Aplicaciones Multiplataforma. Formulario web con API a la que conecta Bot de Discord para la creación de perfiles de servidor configurables.

## Estructura de carpetas

```
PROYECTO360
├───BOT (BOT DE DISCORD CUYA TAREA ES RECIBIR TODOS LOS DATOS DE LA DB Y CON ELLOS ESTRUCTURAR LOS PERFILES SOLICITADOS POR LOS USUARIOS)
│   ├───commands.py
│   ├───config.json
│   ├───main.py
│   └───utils.py
├───API-REST (AQUÍ SE ALMACENA TANTO LA API QUE ESTÁ LANZADA EN LA WEB COMO LA BASE DE DATOS JSON)
│   ├───db
│   │   └───db.json
│   ├───app.py
│   ├───config.json
│   └───utils.py
├───WEB (FORMULARIO WEB QUE HACE EL POST DE LOS DATOS A LA API)
│   ├───form
│   │   └───form.php
│   ├───src
│   │   └───disc.png
│   ├───index.html
│   ├───script.js
│   └───style.css
└───README.md

```
