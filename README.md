# AWS Desde Cero

Este es un proyecto que tiene como objetivo enseñar las bases de AWS a usuarios con pocos o ningún conocimiento de desarrollo de software. 
La creación de esta web está automatizada mediante plantillas Flask y workflows.

## Para crear un nuevo post

1. Crear una imagen en `static/img/pubs/principal` con el nombre `aws-<numero>_<descripcion-con-guiones>.jpg`. El número debe ser el siguiente al último post creado. 
2. Crar un archivo en `templates/pubs` con el nombre `aws-<numero>_<descripcion-con-guiones>.html`.
3. Añade todas las imágenes que quieras crear en la carpeta `static/img/inside-pubs/<nombre>`. 
4. Añade los diagramas que quieras crear en la carpeta `templates/diagrams/<nombre-del-diagrama>`. Referencialos con `{% include 'diagrams/01_Food2Go.html' %}`.

## Requisitos

Antes de comenzar, es necesario tener instalados los siguientes programas:

- Python 3
- Flask
- Frozen Flask

## Desarrollo

1. Clona este repositorio:

git clone https://github.com/tu-usuario/aws-desde-cero.git

2. Navega al directorio del proyecto:

cd aws-desde-cero

3. Crea y activa un entorno virtual:

python3 -m venv env
source env/bin/activate

4. Instala las dependencias:
pip install -r requirements.txt

5. Ejecuta la aplicación Flask:
flask run  --debug --reload

6. Accede a la página web en tu navegador web en la dirección http://localhost:5000/

## Despliegue 

1. Genera los archivos estáticos:
python freeze.py


## Autor

Este proyecto fué creado por [Fernando Carazo](https://github.com/FernandoCarazoMelo/). Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto conmigo a través de mi correo electrónico o mi perfil de GitHub.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más información.



