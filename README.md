Programación Web – Unidad III – Encargo 3

Institución: IPLACEX
Asignatura: Programación Web
Tecnologías: Python, Flask, HTML y CSS

Descripción

Aplicación web desarrollada para el Encargo 3 de la Unidad III, que incluye dos ejercicios:

Ejercicio 1: Cálculo de promedio de notas y determinación de aprobación según asistencia.

Ejercicio 2: Identificación del nombre de mayor longitud entre tres nombres ingresados.

Consideraciones de implementación

Para resolver situaciones no especificadas expresamente en el enunciado, se adoptaron los siguientes criterios:

Ejercicio 1 – Notas y asistencia

Se utilizaron notas enteras entre 10 y 70 y porcentajes de asistencia enteros entre 0 y 100.

La aprobación requiere cumplir simultáneamente el promedio mínimo de 40 y la asistencia mínima del 75 %.

Ejercicio 2 – Nombres

Se aceptan nombres con letras, tildes y espacios.

Se rechazan nombres repetidos, sin distinguir entre mayúsculas y minúsculas.

Se eliminan los espacios al inicio y al final; los espacios interiores se consideran al contar caracteres.

En caso de empate en la longitud máxima, se selecciona el primer nombre ingresado que cumpla esa condición, dado que el enunciado no establece un criterio de desempate.

Ejecución

Instalar las dependencias:

pip install -r requirements.txt

Ejecutar la aplicación:

python main.py

Abrir en el navegador: http://127.0.0.1:5000

Proyecto desarrollado con fines académicos para IPLACEX.
