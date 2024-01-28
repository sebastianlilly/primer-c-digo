print("Hola Vamos a Hacer algunos c‡lculos")
print("Y para eso requiero que me digas cuantas personas hay qen tu oficina ")

num_personas = int(input("Ingrese la cantidad de personas en el trabajo: "))

salarios = []

for i in range(num_personas):
    salario = float(input(f"Ingrese el sueldo del empleado {i+1}: "))
    salarios.append(salario)
    
sueldo_promedio=sum(salarios)/len(salarios)
print("El promedio de sueldos de esta oficina es : $",sueldo_promedio)
sueldo_menor=min(salarios)
sueldo_mayor=max(salarios)


print("El sueldo mas bajo es $",sueldo_menor)
print("El sueldo mas alto es $",sueldo_mayor)

if sueldo_menor <= (sueldo_promedio / 3):
    print("¡Estamos en problemas!")
    print("Hay que ajustar el sueldo menor.")
    sueldo_menor2 = sueldo_menor * 1.35
    print("Nuevo sueldo menor después del ajuste: $", sueldo_menor2)
    
elif sueldo_promedio >= 5000000:
    print("El sueldo promedio excede lo permitido por la compañía.")
    print("Se realizará un ajuste en el sueldo mayor de un 35% menos.")
    sueldo_mayor *= (1 - 0.35)
    print("El nuevo sueldo mayor ahora es: $", sueldo_mayor)    
    descuento_a_sueldo_mayor = sueldo_mayor * 0.35
    print("El descuento aplicado al sueldo mayor fue de: $", descuento_a_sueldo_mayor)
else:
    print("La situación financiera es estable. No se requieren ajustes.")
   
