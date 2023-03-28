from baseDeDatos import BaseDeDatos
from OpcMenu import *
import os

class GestionCliente(object):
    def __init__(self):
        self.base = BaseDeDatos()
        self.base.inicializacionBase()
        self.menu = opcMenu()          
    def altaCliente(self,dni_cliente,cliente):
        clienteporagregar = self.base.hacerConsulta("Clientes","DNI_Cli",dni_cliente) 
        print1=(f''' Se generará el cliente:
                DNI de cliente______: {cliente[0]}
                Nombre de cliente___: {cliente[1]}
                Apellido cliente____: {cliente[2]}
                Direccion cliente___: {cliente[3]}
                Telefono cliente____: {cliente[4]}
                Email de cliente____: {cliente[5]}
                Situación IVA cli___: {cliente[6]}
                ''')  
        if type(clienteporagregar) == str:
            if self.menu.menuSiNo(print1):
                os.system("cls")
                self.base.altaCliente(cliente)
                print("\n Registro exitoso.")
            else:
                print("\nSe canceló la operación.")
        elif clienteporagregar[7] == 'I':
            if self.menu.menuSiNo(print1):
                os.system("cls")
                self.base.modificarCliente(cliente[0],cliente)
                print("\n Registro exitoso.")
            else:
                print("\nSe canceló la operación.")
        else:
            print("\nEl cliente que se quiere dar de alta ya está registrado")          
    def borrarCliente(self,dni_cliente):
        clienteABorrar = self.base.hacerConsulta("Clientes","DNI_Cli",dni_cliente)  
        if not type(clienteABorrar) == str:
            print1=(f'''Clientes a borrar: 
                DNI de cliente: {clienteABorrar[0]}
                Nombre de cliente: {clienteABorrar[1]}
                Apellido cliente: {clienteABorrar[2]}
                Direccion: {clienteABorrar[3]}
                Telefono: {clienteABorrar[4]}
                Email: {clienteABorrar[5]}
                Situacion IVA: {clienteABorrar[6]}
                ''')
            if self.menu.menuSiNo(print1):
                os.system("cls")
                self.base.cambioEstado("Clientes","DNI_Cli",dni_cliente,'I')
                print("\n Cliente eliminado exitosamente.")
            else:
                print("\nSe canceló la operación.")     
        else:
            print("\nEl DNI no se encuentra registrado.")   
    def modiClientes(self,dni_cliente,clienteModificado):
        clienteAModificar = self.base.hacerConsulta("Clientes","DNI_Cli",dni_cliente)  
        if not type(clienteAModificar) == str:
            print1=(f'''Cliente a modificar: 
                DNI de cliente: {clienteModificado[0]}
                Nombre de cliente: {clienteModificado[1]}
                Apellido cliente: {clienteModificado[2]}
                Direccion: {clienteModificado[3]}
                Telefono: {clienteModificado[4]}
                Email: {clienteModificado[5]}
                Situacion IVA: {clienteModificado[6]}
                ''')
            if self.menu.menuSiNo(print1):
                os.system("cls")
                self.base.modificarCliente(dni_cliente,clienteModificado)
                os.system("cls")
                print("\nModificación de cliente exitosa.")
            else:
                print("\nSe canceló la operación.")
        else:
            print("\nEl DNI no corresponde a un cliente registrado.")