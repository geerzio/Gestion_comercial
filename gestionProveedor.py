from baseDeDatos import BaseDeDatos
from OpcMenu import *
import os
##   - Alta/Baja/Modificación de Proveedor (DNI, Nombre de Fantasía, Direccion, Telefono, mail, Situacion IVA (Inscripto, Exento, etc..))
##         - Pedido de reposición a Proveedor
##        - Devolución a proveedor: se podrá realizar una baja de stock de articulos de un proveedor para devolver, 
##         habrá que completar un campo Observacion o Estado(vencido, dañado, etc)


class GestionProveedor(object):
    def __init__(self):
        self.base = BaseDeDatos()
        self.base.inicializacionBase()
        self.menu = opcMenu()
    def altaProv(self,Prov,proveedor):
        IngresoProveedor=self.base.hacerConsulta('Proveedores','CUIL_CUIT_Prov',Prov)
        print1 = (f'''Se va a generar el alta del proveedor:
                    CUIL / CUIT PROV._____: {proveedor[0]}
                    Nombre de Proveedor___: {proveedor[1]}
                    Dirección Proveedor___: {proveedor[2]}
                    Teléfono Proveedor____: {proveedor[3]}
                    Mail de Proveedor_____: {proveedor[4]}
                    Estado IVA Proveedor__: {proveedor[5]}
                    ''')
        if type(IngresoProveedor)==str:
            if self.menu.menuSiNo(print1):
                os.system('cls')
                self.base.altaProveedor(proveedor)
                print('\nRegistro exitoso.\n')
            else:
                print('\nSe canceló la operación.\n')
        elif IngresoProveedor[6]=='I':
            if self.menu.menuSiNo(print1):
                os.system('cls')
                self.base.modificarProveedor(proveedor[0],proveedor)
                print('\nRegistro exitoso.\n')
            else:
                print('\nSe canceló la operación.\n')
        else:
            print("Proveedor ya registrado en Base de Datos...\n")
    def bajaProv(self,Prov):
        ingresoProveedor=self.base.hacerConsulta('Proveedores','CUIL_CUIT_Prov',Prov)
        if not type(ingresoProveedor)==str and ingresoProveedor[6] != 'I':
            print1 = (f'''\nSe va a generar la baja del proveedor:\n
                    CUIL / CUIT PROV.____: {ingresoProveedor[0]}
                    Nombre de Proveedor__: {ingresoProveedor[1]}
                    Dirección Proveedor__: {ingresoProveedor[2]}
                    Teléfono Proveedor___: {ingresoProveedor[3]}
                    Mail de Proveedor____: {ingresoProveedor[4]}
                    Estado IVA Proveedor_: {ingresoProveedor[5]}
                    ''')
            if self.menu.menuSiNo(print1):
                os.system('cls')
                self.base.cambioEstado('Proveedores','CUIL_CUIT_Prov',Prov,'I')
                print('\nSe ha dado de baja a Proveedor.\n')
            else:
                print('\nSe canceló la operación.\n')
        else:
            print("Proveedor no registrado en Base de Datos.")
    def modificarProv(self,Prov,modprov):
        proveedorAMod=self.base.hacerConsulta('Proveedores','CUIL_CUIT_Prov',Prov)
        if not type(proveedorAMod)==str:
            print1 = (f'''\nSe va a Modificar los datos de proveedor:\n
                    CUIL / CUIT PROV._____: {modprov[0]}
                    Nombre de Proveedor___: {modprov[1]}
                    Dirección Proveedor___: {modprov[2]}
                    Teléfono Proveedor____: {modprov[3]}
                    Mail de Proveedor_____: {modprov[4]}
                    Estado IVA Proveedor__: {modprov[5]}
                    ''')
            if self.menu.menuSiNo(print1):
                os.system('cls')
                self.base.modificarProveedor(Prov,modprov)
                print('\nSe ha modificado los datos exitosamente.')
            else:
                print('\nSe canceló la operación.')
        else:
            print("CUIL/CUIT no registrado en Tabla Proveedores.")
    def pedidoProveedor(self,pedidoprov):
        print1 = (f'''\nSolicitud por OP. de:\n
                    Código de Barra_____: {pedidoprov[0]}
                    Cantidad Artículo___: {pedidoprov[1]}
                    Nombre de Artículo__: {pedidoprov[2]}
                    Fecha de Solicitud__: {pedidoprov[3]}
                    CUIL/CUIT Proveedor_: {pedidoprov[4]}
                    ''')
        if self.menu.menuSiNo(print1):
            os.system('cls')
            self.base.registrarReposicion(pedidoprov)
            print('\nSolicitud de Productos exitosa.\n')
        else:
            print('\nSe canceló la operación.\n')
    def devolucionProveedor(self,devolucionProv):
            print1 = (f'''\nDatos de Devolución...:\n
                    Código de Barra______: {devolucionProv[0]}
                    Cantidad Artículo____: {devolucionProv[1]}
                    CUIL/CUIT Proveedor__: {devolucionProv[2]}
                    Motivo de devolución_: {devolucionProv[3]}
                    Fecha de devolución__: {devolucionProv[4]}
                    ''')
            if self.menu.menuSiNo(print1):
                os.system('cls')
                self.base.registraDevolucion(devolucionProv)
                self.base.descuentaArticulos(devolucionProv[0],devolucionProv[1])
                print('\nRegistro de devolución exitosa.\n')
            else:
                print('\nSe canceló la operación.\n')