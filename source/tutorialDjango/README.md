### Link Curso
https://www.youtube.com/embed?listType=playlist&list=PLEtcGQaT56cg3A3r-TNoc-PyVeOuAMB4x
### Instrucciones para usar entorno virtual

* Crear environment

    `$ virtualenv env`

* Activar environment

    `$ source env/bin/activate`

* Instalar requerimientos de *requirements.txt*

    `$ pip install -r requirements.txt`

* Para salir del env

    `$ deactivate`

### Instrucciones para trabajar en branch por issue

* Una vez clonado el documento crear un branch nuevo e ingresar

    `$ git checkout -b newBranch`

* Luego de hacer las modificaciones... 
 
    `$ git add ...` y `$ git commit ...` 

* ...hacer primer push en nuestra rama 

    `$ git push -u origin newBranch`

* Cuando el trabajo este listo para ser verificado realizar **pull-request** online y esperar la verificacion de los compañeros luego hacer **merge** online

### Instrucciones generales
* Crear proyecto
	`$ python django-admin.py startproyect <nombre>`
* Correr Proyecto
	`$ python manage.py runserver`
* Crear App
	`$ python manage.py startapp preguntasyrespuestas`
* Crear superusuario
	`$ python manage.py createsuperuser --username=admin --email=admin@example.com`
* Migrar cambio de modelos
	`$ python manage.py makemigrations`
	`$ python manage.py migrate`
* Limpiar base de datos
	`$ python manage.py flush`