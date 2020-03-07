print(" ")
codigo = str(input("Ingrese su codigo          : "))
print(" ")
dni = str(input("Ingrese su DNI             : "))
print(" ")
nombre = str(input("Ingrese su nombre          : "))
print(" ")
sueldo_neto = float(input("Ingrese sueldo neto mensual: "))
print(" ")
print("OPCIONAL: ")
sueldo_extra = float(input("Ingrese su remuneración extra : "))

UIT = 4300
UIT_05 = UIT * 5
UIT_07 = UIT * 7
UIT_20 = UIT * 20
UIT_35 = UIT * 35
UIT_45 = UIT * 45

TASA_08 = 0.08  # <= 5 UIT
TASA_14 = 0.14
TASA_17 = 0.17
TASA_20 = 0.20
TASA_30 = 0.30

sueldo_anual = sueldo_neto * 12 + sueldo_extra * 12
exedente = sueldo_anual - UIT_07

print(" ")
print("***************************")
print(" ")


if sueldo_anual > UIT_07:

    if exedente <= UIT_05:
        exedente_anual = exedente
        porc_retencion = 8
        impuesto = exedente * TASA_08
        sueldoreal = sueldo_anual - impuesto

    elif exedente > UIT_05 and exedente <= UIT_20:
        exedente_anual = exedente
        porc_retencion = 14
        impuesto = exedente * TASA_14
        sueldoreal = sueldo_anual - impuesto

    elif exedente > UIT_20 and exedente <= UIT_35:
        exedente_anual = exedente
        porc_retencion = 17
        impuesto = exedente * TASA_17
        sueldoreal = sueldo_anual - impuesto

    elif exedente > UIT_35 and exedente <= UIT_45:
        exedente_anual = exedente
        porc_retencion = 20
        impuesto = exedente * TASA_20
        sueldoreal = sueldo_anual - impuesto

    elif exedente > UIT_45:
        exedente_anual = exedente
        porc_retencion = 30
        impuesto = exedente * TASA_30
        sueldoreal = sueldo_anual - impuesto

else:
    exedente_anual = 0
    porc_retencion = 0
    impuesto = 0
    sueldoreal = sueldo_anual - impuesto


print("Remuneración bruta anual    : ", sueldo_anual)
print("Remuneración exedente anual : ", exedente_anual)
print("% de retención              : ", porc_retencion, "%")
print("Retención                   : ", impuesto)
print("Remuneración anual          : ", sueldoreal)
print(" ")
