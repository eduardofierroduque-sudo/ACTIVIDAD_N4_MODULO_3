<img width="1318" height="834" alt="image" src="https://github.com/user-attachments/assets/b8b50e26-561b-4895-9ae1-1c913339ac0c" />
Este proyecto es un script de Python diseñado para gestionar y analizar datos de estudiantes (nombres, edades y calificaciones) utilizando estructuras de control de flujo y funciones integradas del lenguaje.
El programa recorre las listas de datos y realiza las siguientes acciones:
Sincronización de datos: Utiliza zip() para agrupar la información de nombres, edades y notas de forma simultánea.
Seguimiento de índices: Emplea enumerate() para mostrar la posición de cada registro procesado.
Control de flujo inteligente:
Finalización anticipada (break): Si encuentra una calificación de -1, el programa identifica al estudiante como "Retirado" y detiene el proceso inmediatamente.
Salto selectivo (continue): Si un estudiante tiene una nota menor a 6, se considera reprobado y se ignora para el cálculo del promedio, saltando a la siguiente iteración.
Cálculo de estadísticas: Calcula automáticamente el promedio final basándose únicamente en los estudiantes que aprobaron el curso.
<img width="1425" height="334" alt="image" src="https://github.com/user-attachments/assets/10d60627-ca6a-4f7c-ab1f-af4dc1db7c85" />



