# Proyecto Urban Grocers - Pruebas al Parámetro Name al Crear un Kit con authToken de Usuario

Este proyecto busca optimizar las pruebas al parámetro name al crear de un kit con authToken de usuario.
El proyecto está diseñado para enviar solicitudes (POST) que crean un nuevo usuario y luego crear un kit personal para el usuario, utilizando el token de autenticación (authToken) obtenido (GET) durante la creación del usuario. 

## Archivos 

El proyecto contiene los siguientes archivos:
- **configuration.py**: Contiene las rutas del servidor y los paths necesarios.
- **data.py**: Contiene el encabezado y los cuerpos de las requests.
- **sender_stand_request.py**: Contiene las funciones para enviar las solicitudes necesarias.
- **create_kit_name_kit_test.py**: Contiene las pruebas al parámetro name al crear un kit.

## Detalles a considerar

- Descargar los archivos en tu carpeta de proyectos.
- Verifica que Python está instalado escribiendo en la terminal el siguiente comando para saber que versión está instalada *python --version*, si se muestra un error se debe instalar Python.
 - En PyCharm, necesitas tener instalados los paquetes pytest y requests para ejecutar las pruebas.
   - Para instalar los paquetes abre la consola y ejecuta:
     - pip install pytest
     - pip install requests
- Puedes ejecutar las pruebas desde Pycharm, Current File: create_kit_name_kit_test.py o en tu terminal con el comando: pytest create_kit_name_kit_test.py

## Pruebas que se deben comprobar

1. **Prueba #1** Verifica que se puede crear un kit con el nombre de un solo carácter (1).
2. **Prueba #2** verifica que se puede crear un kit con el nombre de 511 caracteres.
3. **Prueba #3** Comprueba que se recibe un error al intentar crear un kit con un nombre vacío (0 caracteres).
4. **Prueba #4** Comprueba que se recibe un error al intentar crear un kit con el nombre de 512 caracteres.
5. **Prueba #5** Valida que se puede crear un kit con caracteres especiales en el nombre.
6. **Prueba #6** Valida que se puede crear un kit con espacios en el nombre.
7. **Prueba #7** Valida que se puede crear un kit con números en el nombre.
8. **Prueba #8** Comrpueba que se recibe un error al intentar crear un kit sin pasar el parámetro "name".
9. **Prueba #9** Comprueba que se recibe un error al intentar crear un kit con un tipo de parámetro no válido (número) para el parámetro "name".