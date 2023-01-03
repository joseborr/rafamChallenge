# Challenge para Rafam
## Jose Ignacio Borajo

## Base de datos
Se uso una bd postgresql:
- nombre : rafamChallenge
- usuario: postgres
- password: 1234
- host: 127.0.0.1
- puerto: 5433

## Servidor
Ejecutar `python manage.py runserver` dentro de el directorio rafamChallenge/challengeback para levantar el servidor.

## Datos de prueba
Ejecutar `python manage.py loaddata students.json lessons.json` dentro de el directorio rafamChallenge/challengeback.
Esto poblará la bd con datos de prueba para las tablas 'student' y 'lesson' pero no crea las relaciones 

## Test
Ejecutar `python manage.py test` en el directorio rafamChallenge/challengeback para correr los 4 test definidos para cada uno de los endpoints. 
Los datos de prueba se cargan automáticamente para los test.

#### Alternativa
Es posible visualizar el comportamiento de la base de datos y ver reflejado en los distintos endpoints. Mediante navegación en http://127.0.0.1:8000/ es posible cargar nuevos estudiantes, amistades y clases tomadas, estableciendo las relaciones correspondientes en la bd. Para las api ingresar en http://127.0.0.1:8000/api/ donde hay accesos a los endpoints que muestran todos los estudiantes y todas las amistades. Para visualizar las clases tomadas por el estudiante con id = 1 ingresar en http://127.0.0.1:8000/api/mylessons/1/ y para ver sus amistades http://127.0.0.1:8000/api/myfriends/1/


