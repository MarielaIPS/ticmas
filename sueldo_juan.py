# las siguientes variables representan el Sueldo de juan segun el mes
Enero_Junio= 300 * 6
Julio_Octubre= 500 * 4
Noviembre_Diciembre = 700 * 2

promedio_sueldo = (Enero_Junio + Julio_Octubre + Noviembre_Diciembre) / 12
print(f"El sueldo promedio de Juan es de: {promedio_sueldo:.2f} dolares")

if promedio_sueldo < 300:
    print("El sueldo de juan es Bajo")
elif promedio_sueldo >= 300 and promedio_sueldo <= 900:
    print("El sueldo de Juan es Normal")
else: print("El sueldo de Juan es mejor que los demas") 


print("Otra manera de resolver el ejercicio")

import pandas as pd

datos=[{"Mes":"Enero","Sueldo":300},{"Mes":"Febrero","Sueldo":300}
       ,{"Mes":"Marzo","Sueldo":300},{"Mes":"Abril","Sueldo":300},
       {"Mes":"Mayo","Sueldo":300},{"Mes":"Junio","Sueldo":300},
       {"Mes":"Julio","Sueldo":500},{"Mes":"Agosto","Sueldo":500},
       {"Mes":"Septiembre","Sueldo":500},{"Mes":"Octubre","Sueldo":500},
       {"Mes":"Noviembre","Sueldo":700},{"Mes":"Diciembre","Sueldo":700}]

dataFreme= pd.DataFrame(datos)

print(dataFreme)

promedio2=dataFreme.Sueldo.mean()
print('El sueldo promedio de Juan es: ', round(promedio2,2))

if promedio2 > 900:
    print("El sueldo promedio de Juan es mejor que los demas")
elif promedio2 >= 300 and promedio2 <= 900:
    print("El sueldo promedio de Juan es Normal")
else: print("El sueldo promedio de juan es Bajo")




