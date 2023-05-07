#Instalación:

##Crear archivo de base de datos:
DATABASE_NAME=nombre de la base de datos
DATABASE_USER=nombre del usuario de base de datos
DATABASE_PASSWORD=contraseña del usuario

##Crear ambiente virtual
python -m venv env

##Activar ambiente virtual
venv\Scripts\activate

##Instalar requerimientos
pip install -r requirements.txt

##Realizar las migraciones
python manage.py migrate

##Ejecutar el servidor
python manage.py runserver