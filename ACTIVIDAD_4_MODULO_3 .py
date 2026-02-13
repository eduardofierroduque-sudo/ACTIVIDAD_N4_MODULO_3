# 1. Definición de las listas de datos
nombres = ["Juan", "Ana", "Pedro", "Luis", "Maria"]
edades = [20, 22, 19, 21, 23]
calificaciones = [8, 6, -1, 9, 5]

# Variables para el cálculo del promedio
suma_calificaciones = 0
contador_aprobados = 0

print("--- Procesando lista de estudiantes ---")

# 2 y 3. Uso de zip() para unir listas y enumerate() para el índice
for indice, (nombre, edad, calificacion) in enumerate(zip(nombres, edades, calificaciones)):
    
    # 4. Control para estudiante retirado
    if calificacion == -1:
        print(f"Índice {indice}: El estudiante {nombre} está RETIRADO. Deteniendo programa...")
        break
    
    # 5. Control para estudiantes reprobados (menor a 6)
    if calificacion < 6:
        print(f"Índice {indice}: {nombre} tiene calificación {calificacion} (Reprobado). Saltando...")
        continue
    
    # 7. Si llega aquí, es un estudiante aprobado
    print(f"Índice {indice}: {nombre} ha aprobado con {calificacion}.")
    
    # Acumulamos los datos para el promedio
    suma_calificaciones += calificacion
    contador_aprobados += 1

# 6. Cálculo y muestra del promedio final
if contador_aprobados > 0:
    promedio = suma_calificaciones / contador_aprobados
    print("---")
    print(f"El promedio de los estudiantes aprobados es: {promedio}")
else:
    print("No hubo estudiantes aprobados para promediar.")