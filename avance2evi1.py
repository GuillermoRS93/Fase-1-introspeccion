import pandas as pd 
import openpyxl

basedatos = pd.read_csv(r"Z:/Usuario/Guillermo RS/Escritorio/Tarifas por zonas 2016-2017.csv")

lista = basedatos["maxima_base_interrumpible"].tolist()
fechaFin = basedatos["fecha_fin"].tolist()
demanda = basedatos["uso_base_firme"].tolist()

def promedioTiempo(basedatos):
    acum2016 = 0
    acum2017 = 0
    len2016 =  0
    len2017 = 0

    for a, b in zip (lista, fechaFin):
        if any ("2016" in b for c in fechaFin):
            acum2016 = a + acum2016
            len2016 = len2016 + 1
        else:
            acum2017 = a+ acum2017
            len2017 = len2017 + 1

promedio2017 = acum2017 / len2017
promedio2016 = acum2016 / len2016

print("Promedio de tarifa maxima_base_interrumpible en el 2016: ", (promedio2016))
print("Promedio de tarifa maxima_base_interrumpible en el 2017:", (promedio2017))

promedioTiempo(basedatos)
print()

def diferencia(basedatos):
    datos2016 = 0
    datos2017 = 0
    resta = 0

    for a, b in  zip(lista, fechaFin):
        if any ("2016" in b for c in fechaFin):
            datos2016 = a + datos2016
        else:
            datos2017 = a + datos2017
    
    resta = datos2017 - datos2016
    print("Variacion de precio de gas natural es de: ", resta)

diferencia(basedatos)
print()

def demandaprom2016(basedatos):
    tarifa2016 = 0
    num2016 = 0
    promedio2016 = 0

    for a, b in zip (lista, fechaFin):
        if any ("2016" in b for c in fechaFin):
            tarifa2016 = a + tarifa2016
            num2016 = num2016 + 1
        promedio2016 = tarifa2016/num2016

    print("Demanda promedio del 2016:", promedio2016)

demandaprom2016(basedatos)
print()

def demandaprom2017(basedatos):
    tarifa2017 = 0
    num2017 = 0
    promedio2017 = 0

    for a, b in zip(lista, fechaFin):
        if any ("2017" in b for c in fechaFin):
            tarifa2017 = a + tarifa2017
            num2017 = num2017 + 1
    promedio2017 = tarifa2017 / num2017

    print("Demanda promedio del año 2017: ", promedio2017)

demandaprom2017(basedatos)
print()

def maxtarifas(basedatos):
    max2016 = 0
    max2017 = 0
    t1 = 0
    t2 = 0

    for a, b in zip (lista, fechaFin):
        if any ("2016" in b for c in fechaFin):
            t1 = a
            if t1 > max2016:
                max2016 = t1
            else:
                t2 = a
                if t2 > max2017:
                    max2017 = t2

print("Tarifa maxima del 2016: ", max2016)
print("Tarifa maxima del 2017: ", max2017)

maxtarifas(basedatos)

