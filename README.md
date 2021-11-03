# pjecz-justicia-digital

Página de bienvenida (landing page) a [www.justiciadigital.gob.mx](https://www.justiciadigital.gob.mx)

## Objetivo

Dar una amigable vista a la modernización tecnológica en el [Poder Judicial del Estado de Coahuila de Zaragoza](https://www.pjecz.gob.mx)

## Entorno Virtual con Python 3.6 o superior

Crear el entorno virtual dentro de la copia local del repositorio, con

    python -m venv venv

O con virtualenv

    virtualenv -p python3 venv

Active el entorno virtual, en Linux con...

    source venv/bin/activate

O en windows con

    venv/Scripts/activate

Verifique que haya el mínimo de paquetes con

    pip list

Actualice el pip de ser necesario

    pip install --upgrade pip

Y luego instale los paquetes que requiere Plataforma Web

    pip install -r requirements.txt

Verifique con

    pip list

## Configurar

Guarde los siguientes valores en un archivo .env

    FLASK_APP=justicia_digital.app
    FLASK_DEBUG=1

## Script de Bash

Escriba un script de Bash en .bashrc con este contenido

    #!/bin/bash
    if [ -f ~/.bashrc ]; then
            . ~/.bashrc
    fi

    . venv/bin/activate
    export $(grep -v '^#' .env | xargs)

    figlet Justicia Digital

    echo "-- Variables de entorno"
    echo "   FLASK_APP:   ${FLASK_APP}"
    echo "   FLASK_DEBUG: ${FLASK_DEBUG}"

    alias arrancar="flask run --port 5009"
    echo "-- Aliases"
    echo "   arrancar:    Arrancar Flask en http://localhost:5009"
    echo

Cambie el número de puerto si lo necesita

## Arrancar Flask

Si cargo el Bash Script

    arrancar

De lo contrario, ejecutar

    flask run --port 5009
