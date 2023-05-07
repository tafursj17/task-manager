# Instalación:

## Base de datos:
Crear un archivo llamado **.env** y agregar las siguientes variables:
* DATABASE_NAME=nombre de la base de datos
* DATABASE_USER=nombre del usuario de base de datos
* DATABASE_PASSWORD=contraseña del usuario


## Configuracion:
```
# Crear ambiente virtual
python -m venv env

# Activar ambiente virtual
env\Scripts\activate

# Instalar requerimientos
pip install -r requirements.txt

# Realizar las migraciones
python manage.py migrate

# Ejecutar el servidor
python manage.py runserver
```
