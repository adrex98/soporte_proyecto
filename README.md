# TICKET SYSTEM

Este proyecto consiste en la creacion de un projecto en DJANGO para la emision de tickets para soporte.

## Requisitos Previos

Antes de comenzar, asegurate de tener los siguientes requsisitos:

- Python 3.x: [Descargar Python](https://www.python.org/downloads/)
- Django 4.x: [How To Install](https://docs.djangoproject.com/en/4.2/intro/install/)

## Configuracion del Entorno

### Entorno Virtual

```bash

python -m venv venv
source venv/bin/activate # En Windwos, usa venv/Scripts/activate

```

### Instalacion de Dependencias

Instala las Dependencias

```bash

pip install -r requirements.txt

```

### Migrar los Modelos

```bash

python manage.py migrate

```

### Ejecucion

```bash

python manage.py runserver #Por defecto el puerto es 8000, sin emgargo si tuvieras problemas utilizando el puertos puedes introducir el puerto que gustes luego de 'runserver'

```