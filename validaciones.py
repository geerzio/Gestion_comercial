import os
import time 

class Validacion(object):
    def numero(self,loQueSea,mayorQue,menorQue):
        ingreso = -1
        while True:
            try:
                while ingreso < mayorQue or ingreso > menorQue:
                    ingreso = int(input(f"\nIngrese {loQueSea}: "))
                    if ingreso < mayorQue or ingreso > menorQue:
                        os.system('cls')
                        print(f"\nEl {loQueSea} debe tener un valor entre {mayorQue} y {menorQue}.")
                break
            except ValueError:
                os.system('cls')
                print("\nPor favor ingrese valores numéricos")
        return ingreso      
    def stringSinNum(self,loQueSea):
        ingreso =""
        validar = True
        while True:
            try:
                while validar == True or len(ingreso) < 1 or len(ingreso) >30:
                    ingreso = input(f"\nIngrese {loQueSea}: ").title()
                    if len(ingreso) < 1 or len(ingreso) >30:
                        os.system('cls')
                        print(f"\nEl {loQueSea} debe tener entre 1 y 30 caracteres.")
                    cont = 0
                    for elemento in ingreso:
                        if not elemento.isdigit():
                            cont += 1
                    if cont != len(ingreso):
                        os.system('cls')
                        print(f"\nPor favor ingrese sólo letras para el {loQueSea}.")
                    else:
                        validar = False
                break
            except ValueError:
                os.system('cls')
                print("\nOcurrió un error.")
        return ingreso
    def string30(self,loQueSea):
        ingreso =""
        while True:
            try:
                while len(ingreso) < 1 or len(ingreso) >30:
                    ingreso = input(f"\nIngrese {loQueSea}: ")
                    if len(ingreso) < 1 or len(ingreso) >30:
                        os.system('cls')
                        print(f"\n{loQueSea} debe tener entre 1 y 30 caracteres.")
                break
            except ValueError:
                os.system('cls')
                print("\nOcurrió un error.")
        return ingreso
    def email(self):
        ingreso =""
        while True:
            try:
                while len(ingreso) < 1 or len(ingreso) >40:
                    ingreso = input(f"\nIngrese el Email: ")
                    if len(ingreso) < 1 or len(ingreso) >40:
                        os.system('cls')
                        print(f"\nEl email debe tener entre 1 y 40 caracteres.")
                break
            except ValueError:
                os.system('cls')
                print("\nOcurrió un error.")
        return ingreso
    def fecha(self):
        ingreso = ""
        dia = 0
        mes = 0
        año = 0
        meses31 = [1,3,5,8,10,12]
        meses30 = [4,6,7,9,11]
        while True:
            try:
                while año < 2022 or año > 2050:
                    año = int(input(f"\nIngrese el año: "))
                    if año < 2022 or año > 2050:
                        os.system('cls')
                        print(f"\nEl año debe tener un valor entre 2022 y 2050.")
                break
            except ValueError:
                os.system('cls')
                print("\nPor favor ingrese valores numéricos")
        while True:
            try:
                while mes < 1 or mes > 12:
                    mes = int(input(f"\nIngrese el mes: "))
                    if mes < 1 or mes > 12:
                        os.system('cls')
                        print(f"\nEl mes debe tener un valor entre 1 y 12.")
                break
            except ValueError:
                os.system('cls')
                print("\nPor favor ingrese valores numéricos")
        if mes in meses30:
            while True:
                try:
                    while dia < 1 or dia > 30:
                        dia = int(input(f"\nIngrese el día: "))
                        if dia < 1 or dia > 30:
                            os.system('cls')
                            print(f"\nEl dia debe tener un valor entre 1 y 30.")
                    break
                except ValueError:
                    os.system('cls')
                    print("\nPor favor ingrese valores numéricos")
        elif mes in meses31:
            while True:
                try:
                    while dia < 1 or dia > 31:
                        dia = int(input(f"\nIngrese el día: "))
                        if dia < 1 or dia > 31:
                            os.system('cls')
                            print(f"\nEl dia debe tener un valor entre 1 y 31.")
                    break
                except ValueError:
                    os.system('cls')
                    print("\nPor favor ingrese valores numéricos")
        else:
            while True:
                try:
                    while dia < 1 or dia > 28:
                        dia = int(input(f"\nIngrese el día: "))
                        if dia < 1 or dia > 28:
                            os.system('cls')
                            print(f"\nEl dia debe tener un valor entre 1 y 28.")
                    break
                except ValueError:
                    os.system('cls')
                    print("\nPor favor ingrese valores numéricos")
        ingreso = str(año) + "-" + str(mes) + "-" + str(dia)
        return ingreso 
    def precio(self,loQueSea,mayorQue,menorQue):
        ingreso = 0
        while True:
            try:
                while ingreso < mayorQue or ingreso > menorQue:
                    ingreso = float(input(f"\nIngrese el {loQueSea}: "))
                    if ingreso < mayorQue or ingreso > menorQue:
                        os.system('cls')
                        print(f"\nEl {loQueSea} debe tener un valor entre {mayorQue} y {menorQue}.")
                break
            except ValueError:
                os.system('cls')
                print("\nPor favor ingrese valores numéricos")
        return (f'{ingreso:.2f}')  
    def tiempoAhora(self):
        tiempo = time.localtime()
        ahora = (f'{tiempo[0]}-{tiempo[1]}-{tiempo[2]}')
        return ahora
