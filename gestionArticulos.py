from baseDeDatos import BaseDeDatos
from OpcMenu import *
import os

class GestionArticulos(object):
    def __init__(self):
        self.base = BaseDeDatos()
        self.base.inicializacionBase()
        self.menu = opcMenu()
    def altaArt(self,codBarra,articulo):
        artAGenerar = self.base.hacerConsulta('Articulos','codigoBarra',codBarra)
        print1 = (f'''Se va a generar el alta del artículo:
                        Código de barra: {articulo[0]}
                        Nombre de artículo: {articulo[1]}
                        Categoría de artículo: {articulo[2]}
                        Precio: {articulo[3]}
                        Cantidad: {articulo[4]}
                        Cuit de proveedor: {articulo[5]}''')
        if  type(artAGenerar) == str:
            if self.menu.menuSiNo(print1):
                os.system('cls')
                self.base.altaArticulo(articulo)
                print('\nRegistro exitoso.')
            else:
                print('\nSe canceló la operación.')
        elif artAGenerar[6] == 'I':
            if self.menu.menuSiNo(print1):
                os.system('cls')
                self.base.modificarArticulo(articulo[0],articulo)
                print('\nRegistro exitoso.')
            else:
                print('\nSe canceló la operación.')
        else:
            print('\nEl artículo que se quiere dar de alta ya está registrado.')
    def bajaArt(self,codigoDeBarra):
        artABorrar = self.base.hacerConsulta('Articulos','codigoBarra',codigoDeBarra)
        if  not type(artABorrar) == str and artABorrar[6]!='I' :
            print1 = (f'''Se va a eliminar el articulo:
                    Código de barra: {artABorrar[0]}
                    Nombre de artículo: {artABorrar[1]}
                    Categoría de artículo: {artABorrar[2]}
                    Precio: {artABorrar[3]}
                    Cantidad: {artABorrar[4]}
                    Cuit de proveedor: {artABorrar[5]}''')
            if self.menu.menuSiNo(print1):
                os.system('cls')
                self.base.cambioEstado('Articulos','codigoBarra',artABorrar[0],'I')
                print('\nBorrado exitoso.')
            else:
                print('\nOperación cancelada.')
        else:
            print('\nEl codigo de barra ingresado no se encuentra registrado.')
    def modificacionArt(self,codBarra,artModificado):
        artAModificar1 = self.base.hacerConsulta('Articulos','codigoBarra',codBarra)
        if  not type(artAModificar1) == str:
            print1 = (f'''Verifique los campos del articulo:
                        Código de barra:  {artModificado[0]}
                        Nombre de artículo:  {artModificado[1]}
                        Categoría de artículo: {artModificado[2]}
                        Precio: {artModificado[3]}
                        Cantidad: {artModificado[4]}
                        ''')
            if self.menu.menuSiNo(print1):
                os.system('cls')
                self.base.modificarArticulo(codBarra,artModificado)
                print('\nRegistro exitoso.')
            else:
                print('\nOperación cancelada.')
        else:
            print('\nEl codigo de barra ingresado no se encuentra registrado.')
    def ingresoArt(self,codBarra,cantidad):
        ingreso = self.base.hacerConsulta('Articulos','codigoBarra',codBarra)
        if  not type(ingreso) == str and ingreso[6] !='I':
            self.base.ingresarArticulos(codBarra,cantidad)
            print(f'\nCodigo de barra: {codBarra} Ingreso exitoso.')
        else:
            print(f"\n------------------ERROR: El código de barra: {codBarra} ingresado no se encuentra registrado, genere el ingreso a través de alta.------------------")
    def ingresoRemito(self,listaArticulos,listaCantidades):
        for ind in range(0,len(listaArticulos)):
            self.ingresoArt(listaArticulos[ind],listaCantidades[ind])
    def listadoArt(self):
        listaRegistros = []
        registros= self.base.cantidadDeRegistros('Articulos')
        for registro in registros:
            if registro[6]!='I':
                listaRegistros.append(list(registro))
        tablaArticulos = """\
                        ---------------------- Se muestra un límite de 100 registros ----------------------                           
+-----------------------------------------------------------------------------------------------------------------------------------+
|   CODIGO DE BARRA               NOMBRE                  CATEGORIA        PRECIO        CANTIDAD            CUIT-PROVEEDOR         |   
|-----------------------------------------------------------------------------------------------------------------------------------|
{}
+-----------------------------------------------------------------------------------------------------------------------------------+\
"""
        tablaArticulos = (tablaArticulos.format('\n'.join("| {0:^18} |{1:^30} |{2:^15} |{3:^15}| {4:^10} | {5:^30} |".format(*fila)
 for fila in listaRegistros)))
        os.system('cls')
        print(tablaArticulos)
    def listadoSinStock(self):
        listaRegistros = []
        registros= self.base.consultarStock('Articulos','CantidadArt',0)
        if len(registros) > 0:
            for registro in registros:
                if registro[6]!='I':
                    listaRegistros.append(list(registro))
            tablaArticulos = """\
                               ---------------------- LISTADO DE FALTANTES DE STOCK ---------------------- 
                            ---------------------- Se muestra un límite de 100 registros ----------------------                           
+-----------------------------------------------------------------------------------------------------------------------------------+
|   CODIGO DE BARRA               NOMBRE                  CATEGORIA        PRECIO        CANTIDAD            CUIT-PROVEEDOR         |   
|-----------------------------------------------------------------------------------------------------------------------------------|
{}
+-----------------------------------------------------------------------------------------------------------------------------------+\
    """
            tablaArticulos = (tablaArticulos.format('\n'.join("| {0:^18} |{1:^30} |{2:^15} |{3:^15}| {4:^10} | {5:^30} |".format(*fila)
    for fila in listaRegistros)))
            os.system('cls')
            print(tablaArticulos)
        else:
            print("\nPor el momento no se registran faltantes de stock.")
    def descontarArticulos(self,codBarra,cantidad):
        artADesc = self.base.hacerConsulta('Articulos','codigoBarra',codBarra)
        if not type(artADesc) == str:
            self.base.descuentaArticulos(codBarra,cantidad)
        else:
            print("\nEl código de barra ingresado no corresponde a un artículo registrado.")
