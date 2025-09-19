"""
Integrantes
Carlos Osvaldo Díaz García

Fecha
18 de septiembre de 2025

Calcular el sueldo semanal de un empleado, 
dadas las horas trabajadas y la tarifa horaria. 
Considerar que si trabajó más de 48 horas, las 
horas excedentes se pagan dobles. Desglosar la 
cantidad y el importe correspondientes a las 
horas extra.
"""

# Declaraciones
horas_extras = 0
sueldo_extra = 0

# Entradas
horas_trabajadas = int(input("Horas trabajadas: "))
tarifa = float(input("Tarifa por hora: "))

# Proceso
if horas_trabajadas > 48:
    horas_extras = horas_trabajadas - 48
    horas_trabajadas = horas_trabajadas - horas_extras

    sueldo_extra = (horas_extras * 2) * tarifa

sueldo_total = (horas_trabajadas * tarifa) + sueldo_extra

# Salidas
print("Horas extras:", horas_extras)
print("Sueldo por horas extras:", sueldo_extra)
print("Sueldo total:", sueldo_total)