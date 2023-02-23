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

## Requisitos para el despliegue de la aplicación

¡Necesitas tener instalado [Python](https://www.python.org/downloads/) y [pip](https://pip.pypa.io/en/stable/) para poder desplegar la aplicación!

Necesitas además tener instalados los siguientes módulos:

```bash
pip install nextcord
```
```bash
pip install flask
```
```bash
pip install discord-py-slash-command
```

Los requisitos para desplegar la web son:

- Instalar XAMPP
- Poner la web en C:\xampp\htdocs
- Iniciar apache desde XAMPP

Tras desplegar la web deberás poner en funcionamiento la API y el Bot:

- Configurar el archivo config.json de la API
- Crear una aplicación en Discord y un bot en ella https://discord.com/developers/applications
- Configurar el archivo config.json del Bot
- Meter al Bot en tu servidor
- Rellenar el formulario web que has desplegado (deberán hacerlos todos aquellos que quieran un perfil)

Si necesita cualquier cosa contacte conmigo en Discord a través de Usuariozombie#9110
