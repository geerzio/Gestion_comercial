from gestionArticulos import *
from gestionCliente import *
from gestionProveedor import *
from baseDeDatos import *
from OpcMenu import *
from validaciones import *
from gestionVentas import *
import os
os.system("cls")

print(f'''
♦- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -♦
:          BIENVENIDO/A !!! AL  SISTEMA Y GESTIÓN DE ABASTECIMIENTO                 :
:                        SUPPLY TECHNOLOGY PLG. SA.                                 :
♦- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -♦
''')
print(input("\nPresione 'ENTER' para comenzar..."))

class GestionComercial (object):
    def __init__(self):
        self.menuGral = (f'''
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            --                      "Gestion interna"                      --
            -----------------------------------------------------------------
            --  1: Menu Proveedores                                        --
            --  2: Menu Clientes                                           --
            --  3: Menu Articulos                                          --
            --  4: Menu Ventas                                             --
            --  5: Salir del Sistema                                       --
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            ''')
        self.menuProv = (f'''
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            --                    "Menu Proveedores"                       --
            -----------------------------------------------------------------
            --  1: Alta Proveedor                                          --
            --  2: Baja Proveedor                                          --
            --  3: Modificacion Proveedor                                  --
            --  4: Pedido Proveedor                                        --
            --  5: Devolución Proveedor                                    --
            --  6: Salir                                                   --
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            ''')
        self.menuCli = (f'''
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            --                    "Menu Clientes"                          --
            -----------------------------------------------------------------
            --  1: Alta Clientes                                           --
            --  2: Baja Clientes                                           --
            --  3: Modificacion Clientes                                   --
            --  4: Salir                                                   --
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            ''')
        self.menuArt = (f'''
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            --                     "Menu Articulos"                        --
            -----------------------------------------------------------------
            --  1: Alta Articulos                                          --
            --  2: Baja Articulos                                          --
            --  3: Modificacion Articulos                                  --
            --  4: Ingreso de Articulo                                     --
            --  5: Ingreso de remito                                       --
            --  6: Listado de articulos Faltantes                          --
            --  7: Salir                                                   --
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            ''')
        self.ventaDirecta = (f'''
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            --                      "Menu Venta"                           --
            -----------------------------------------------------------------
            --  1: Facturación (A)-(B)                                     --
            --  2: Listado Ventas Realizadas                               --
            --  3: Salir                                                   -- 
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            ''')        
        self.estadoIVa = (f'''
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            --                      "Estado de IVA"                        --
            -----------------------------------------------------------------
            --  1: Inscripto                                               --
            --  2: Excento                                                 --
            --  3: Final                                                   -- 
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            ''')
        self.menu = opcMenu()
        self.gestProv = GestionProveedor()
        self.gestArt = GestionArticulos()
        self.gestCli = GestionCliente()
        self.val = Validacion()
        self.base = BaseDeDatos()
        self.gestVentas = gestionVentas()
        self.base.inicializacionBase()
    def menuArticulos(self):
        seleccion = self.menu.menuNum(self.menuArt,7)
        if seleccion == 1:
            nuevoCodBarra = self.val.numero('Código de Barra',99999999999,999999999999)
            nuevoCuit = self.val.numero('CUIT',9999999999,99999999999)
            cuitExiste = self.base.hacerConsulta('Proveedores','CUIL_CUIT_Prov',nuevoCuit)
            artACrear = self.base.hacerConsulta("Articulos","codigoBarra",nuevoCodBarra)
            if type(artACrear) == str or artACrear[6] == 'I':
                if not type(cuitExiste) == str and cuitExiste[6]!= 'I':
                    nuevoNom = self.val.string30('Nombre de artículo')
                    nuevaCat = self.val.stringSinNum('Categoría')
                    nuevoPrecio = self.val.precio('Precio',0.1,999999.99)
                    nuevaCant = self.val.numero('número de existencias',1,999)
                    estado = 'A'
                    nuevoArt = [nuevoCodBarra,nuevoNom,nuevaCat,nuevoPrecio,nuevaCant,nuevoCuit,estado]
                    self.gestArt.altaArt(nuevoArt[0],nuevoArt)
                else:
                    print("""
                        El CUIT ingresado no corresponde a ningún proveedor registrado.
                        Genere el alta de proveedor y vuelva a ingrear el artículo.
                        """)
            else:
                print("\nEl código de barra ingresado ya corresponde a un articulo registrado.\nSe salió del menu de alta de artículos.")
        elif seleccion == 2:
            nuevoCodBarra = self.val.numero('Código de Barra',99999999999,999999999999)
            artABorrar = self.base.hacerConsulta("Articulos","codigoBarra",nuevoCodBarra)
            if not type(artABorrar) == str:
                self.gestArt.bajaArt(nuevoCodBarra)
            else:
                print("\nEl codigo de barra ingresado no se encuentra registrado.")
        elif seleccion == 3:
            printModiArt = ('''
                -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
                --                    "Modificación de Artículo"               --
                -----------------------------------------------------------------
                --  1: Modificar Codigo de Barra                               --
                --  2: Modificar Nombre                                        --
                --  3: Modificar Categoría                                     --
                --  4: Modificar precio                                        --
                --  5: Modificar Cantidad                                      --
                --  6: Modificar Todo                                          --
                --  7: Salir                                                   --
                -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
                ''')
            codBarra = self.val.numero('Código de Barra',99999999999,999999999999)
            artAMod = self.base.hacerConsulta("Articulos","codigoBarra",codBarra)
            if not type(artAMod) == str and artAMod[6] !='I':
                subMenu = self.menu.menuNum(printModiArt,7)
                if subMenu == 1:
                    nuevoCodBarra = self.val.numero('Nuevo Código de Barra',99999999999,999999999999)
                    artAMod[0] = nuevoCodBarra
                    self.gestArt.modificacionArt(codBarra,artAMod)
                if subMenu == 2:
                    nuevoNom = self.val.string30('Nuevo Nombre de artículo')
                    artAMod[1] = nuevoNom
                    self.gestArt.modificacionArt(codBarra,artAMod)
                if subMenu == 3:
                    nuevaCat = self.val.stringSinNum('Nueva Categoría')
                    artAMod[2] = nuevaCat
                    self.gestArt.modificacionArt(codBarra,artAMod)
                if subMenu == 4:
                    nuevoPrecio = self.val.precio('Nuevo Precio',0.1,999999.99)
                    artAMod[3] = nuevoPrecio
                    self.gestArt.modificacionArt(codBarra,artAMod)
                if subMenu == 5:
                    nuevaCant = self.val.numero('número de existencias',0,999)
                    artAMod[4] = nuevaCant
                    self.gestArt.modificacionArt(codBarra,artAMod)
                if subMenu == 6:
                    nuevoCodBarra = self.val.numero('Nuevo Código de Barra',99999999999,999999999999)
                    nuevoNom = self.val.string30('Nuevo Nombre de artículo')
                    nuevaCat = self.val.stringSinNum('Nueva Categoría')
                    nuevoPrecio = self.val.precio('Nuevo Precio',0.1,999999.99)
                    nuevaCant = self.val.numero('número de existencias',1,999)
                    estado='A'
                    articuloModi = [nuevoCodBarra,nuevoNom,nuevaCat,nuevoPrecio,nuevaCant,artAMod[5],estado]
                    self.gestArt.modificacionArt(codBarra,articuloModi)
                else:
                    pass
            else:
                print("\nEl código de barra ingresado no corresponde a un artículo registrado.\nSe debe generar el alta primero.")
        elif seleccion == 4:
            nuevoCodBarra = self.val.numero('Código de Barra',99999999999,999999999999)
            cantidadDeArt = self.val.numero('número de existencias a ingresar',1,999)
            artAIngresar = self.base.hacerConsulta("Articulos","codigoBarra",nuevoCodBarra)
            if not type(artAIngresar) == str and artAIngresar[6] != 'I':
                self.gestArt.ingresoArt(nuevoCodBarra,cantidadDeArt)
            else:
                print("\nEl código de barra ingresado no corresponde a un artículo registrado.")
        elif seleccion == 5:
            artDistintos = self.val.numero('número de artículos distintos a ingresar',1,50)
            listaCodBarra = []
            listaCantidad = []
            for cant in range(0,artDistintos):
                os.system('cls')
                nuevoCodBarra = self.val.numero('Código de Barra',99999999999,999999999999)
                cantidadDeArt = self.val.numero('número de existencias correspondiente al codigo de barra que ingresó',1,999)
                listaCodBarra.append(nuevoCodBarra)
                listaCantidad.append(cantidadDeArt)
            self.gestArt.ingresoRemito(listaCodBarra,listaCantidad)
        elif seleccion == 6:
            self.gestArt.listadoSinStock()
        else:
            print("\n...Saliendo de menu Artículos.")
    def menuProveedores(self):
        seleccion = self.menu.menuNum(self.menuProv,6)
        if seleccion == 1:
            nuevoCuit= self.val.numero('CUIT',9999999999,99999999999)
            proveedorACrear = self.base.hacerConsulta("Proveedores","CUIL_CUIT_Prov",nuevoCuit)
            if type(proveedorACrear) == str or proveedorACrear[6] == 'I':  
                nuevoNom = self.val.stringSinNum('Nombre de Proveedor')
                nuevaDir = self.val.string30('la dirección del proveedor')
                nuevoTel = self.val.numero('Teléfono',1099999999,11099999999)
                nuevoEmail = self.val.email()
                selIVA = self.menu.menuSel(self.estadoIVa,3)
                if selIVA == 1:
                    nuevoEstadoIva = 'Inscripto'
                elif selIVA == 2:
                    nuevoEstadoIva = 'Exento'
                else:
                    nuevoEstadoIva = 'Final'
                estado = 'A'
                nuevoProv =[nuevoCuit,nuevoNom,nuevaDir,nuevoTel,nuevoEmail,nuevoEstadoIva,estado]
                self.gestProv.altaProv(nuevoCuit,nuevoProv)
            else:
                print("""\nEl CUIT corresponde a un proveedor ya registrado.""")
        elif seleccion == 2:
            nuevoCuit= self.val.numero('CUIT',9999999999,99999999999)
            self.gestProv.bajaProv(nuevoCuit)
        elif seleccion == 3:
            printModiProv = ('''
                -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
                --                 "Modificación de Proveedor"                 --
                -----------------------------------------------------------------
                --  1: Modificar CUIT                                          --
                --  2: Modificar Nombre                                        --
                --  3: Modificar Dirección                                     --
                --  4: Modificar Teléfono                                      --
                --  5: Modificar Email                                         --
                --  6: Modificar Estado de IVA                                 --
                --  7: Modificar Todo                                          --
                --  8: Salir                                                   --
                -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
                ''')
            provCuit= self.val.numero('CUIT',9999999999,99999999999)
            proveedorAMod = self.base.hacerConsulta("Proveedores","CUIL_CUIT_Prov",provCuit)
            if not type(proveedorAMod) == str and proveedorAMod[6]!='I':  
                subMenu = self.menu.menuNum(printModiProv,8)
                if subMenu == 1:
                    nuevoCuit = self.val.numero('Nuevo CUIT',9999999999,99999999999)
                    proveedorAMod[0] = nuevoCuit
                    self.gestProv.modificarProv(provCuit,proveedorAMod)
                if subMenu == 2:
                    nuevoNom = self.val.stringSinNum('Nuevo Nombre del Proveedor')
                    proveedorAMod[1] = nuevoNom
                    self.gestProv.modificarProv(provCuit,proveedorAMod)
                if subMenu == 3:
                    nuevaDir = self.val.string30('la nueva dirección del proveedor')
                    proveedorAMod[2] = nuevaDir
                    self.gestProv.modificarProv(provCuit,proveedorAMod)
                if subMenu == 4:
                    nuevoTel = self.val.numero('Nuevo Teléfono',1099999999,11099999999)
                    proveedorAMod[3] = nuevoTel
                    self.gestProv.modificarProv(provCuit,proveedorAMod)
                if subMenu == 5:
                    nuevoEmail = self.val.email()
                    proveedorAMod[4] = nuevoEmail
                    self.gestProv.modificarProv(provCuit,proveedorAMod)
                if subMenu == 6:
                    selIVA = self.menu.menuSel(self.estadoIVa,3)
                    if selIVA == 1:
                        nuevoEstadoIva = 'Inscripto'
                    elif selIVA == 2:
                        nuevoEstadoIva = 'Exento'
                    else:
                        nuevoEstadoIva = 'Final'
                    proveedorAMod[5] = nuevoEstadoIva
                    self.gestProv.modificarProv(provCuit,proveedorAMod)
                if subMenu == 7:
                    nuevoCuit = self.val.numero('Nuevo CUIT',9999999999,99999999999)
                    nuevoNom = self.val.stringSinNum('Nuevo Nombre del Proveedor')
                    nuevaDir = self.val.string30('la nueva dirección del proveedor')
                    nuevoTel = self.val.numero('Nuevo Teléfono',1099999999,11099999999)
                    nuevoEmail = self.val.email()
                    selIVA = self.menu.menuSel(self.estadoIVa,3)
                    if selIVA == 1:
                        nuevoEstadoIva = 'Inscripto'
                    elif selIVA == 2:
                        nuevoEstadoIva = 'Exento'
                    else:
                        nuevoEstadoIva = 'Final'
                    estado = 'A'
                    nuevoProv = [nuevoCuit,nuevoNom,nuevaDir,nuevoTel,nuevoEmail,nuevoEstadoIva,estado]
                    self.gestProv.modificarProv(provCuit,nuevoProv)
                else:
                    print("\nSe salió del menu de modificación de proveedor.")
            else:
                os.system("cls")
                print("\nEl CUIT ingresado no corresponde a un proveedor registrado.")
        elif seleccion == 4:
            pedidoCodBarra = self.val.numero('Código de barra',99999999999,999999999999)
            artASolicitar = self.base.hacerConsulta("Articulos","codigoBarra",pedidoCodBarra)
            if not type(artASolicitar) == str:
                validarProv = self.base.hacerConsulta('Proveedores','CUIL_CUIT_Prov',artASolicitar[5])
                if validarProv[6] != 'I':
                    pedidoCantidad = self.val.numero('Cantidad',1,1000)
                    pedidoFecha = self.val.tiempoAhora()
                    nuevoPedido=[pedidoCodBarra,pedidoCantidad,artASolicitar[1],pedidoFecha,artASolicitar[5]]
                    self.gestProv.pedidoProveedor(nuevoPedido)
                else:
                    os.system("cls")
                    print("\nEl proveedor para el artículo seleccionado no se encuentra activo.")
            else:
                os.system("cls")
                print("\nEl articulo solicitado no esta registrado en la base de datos. Genere el alta primero.")
        elif seleccion == 5:
            devolucionCodBarra = self.val.numero('Código de barra del artículo a devolver',99999999999,999999999999)
            existeArt = self.base.hacerConsulta('Articulos','codigoBarra',devolucionCodBarra)
            if not type(existeArt) == str:
                validarProv = self.base.hacerConsulta('Proveedores','CUIL_CUIT_Prov',existeArt[5])
                if validarProv[6] != 'I':
                    devolucionCantidad = self.val.numero('Cantidad del artículo a devolver',1,1000)
                    devolucionMotivo = self.val.stringSinNum('Motivo de la devolución')
                    devolucionFecha = self.val.tiempoAhora()
                    nuevaDevolucion = [devolucionCodBarra,devolucionCantidad,existeArt[5],devolucionMotivo,devolucionFecha]
                    self.gestProv.devolucionProveedor(nuevaDevolucion)
                else:
                    os.system("cls")
                    print("\nEl proveedor para el artículo seleccionado no se encuentra activo.")
            else:
                print("\nEl artículo que se intenta devolver no está registrado en la base de datos.")
        else:
            print("\n...Saliendo del menu Proveedor.")      
    def menuClientes(self):
        seleccion = self.menu.menuNum(self.menuCli,4)
        if seleccion == 1:
            nuevoDNI = self.val.numero('DNI',1000000,99999999)
            clienteACrear = self.base.hacerConsulta("Clientes","DNI_Cli",nuevoDNI)
            if type(clienteACrear) == str or clienteACrear[7] == 'I':   
                nuevoNom = self.val.stringSinNum('Nombre del cliente')
                nuevoApe = self.val.stringSinNum('Apellido del cliente')
                nuevaDir = self.val.string30('la dirección del cliente')
                nuevoTel = self.val.numero('Teléfono',1099999999,11099999999)
                nuevoEmail = self.val.email()
                selIVA = self.menu.menuSel(self.estadoIVa,3)
                if selIVA == 1:
                    nuevoEstadoIva = 'Inscripto'
                elif selIVA == 2:
                    nuevoEstadoIva = 'Exento'
                else:
                    nuevoEstadoIva = 'Final'
                estado = 'A'
                nuevoCli = [nuevoDNI,nuevoNom,nuevoApe,nuevaDir,nuevoTel,nuevoEmail,nuevoEstadoIva,estado]
                self.gestCli.altaCliente(nuevoDNI,nuevoCli)
            else:
                print("""\nEl DNI corresponde a un cliente ya registrado.""")
        elif seleccion == 2:
            dniCliente = self.val.numero('DNI',1000000,99999999)
            self.gestCli.borrarCliente(dniCliente)
        elif seleccion == 3:
            os.system("cls")
            printModiCli=(f'''
                -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
                --                    "Modificación de Cliente"                --
                -----------------------------------------------------------------
                --  1: Modificar DNI                                           --
                --  2: Modificar Nombre                                        --
                --  3: Modificar Apellido                                      --
                --  4: Modificar Dirección                                     --
                --  5: Modificar Teléfono                                      --
                --  6: Modificar Email                                         --
                --  7: Modificar Estado de IVA                                 --
                --  8: Modificar Todo                                          --
                --  9: Salir                                                   --
                -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
                ''')
            dniCliente = self.val.numero('DNI',1000000,99999999)
            cliente = self.base.hacerConsulta("Clientes","DNI_Cli",dniCliente)
            if not type(cliente) == str and cliente[7] != 'I':
                subMenu = self.menu.menuNum(printModiCli,9)
                if subMenu == 1:
                    nuevoDNI = self.val.numero('Nuevo DNI',1000000,99999999)
                    cliente[0] = nuevoDNI
                    self.gestCli.modiClientes(dniCliente,cliente)
                if subMenu == 2:
                    nuevoNom = self.val.stringSinNum('Nuevo Nombre del cliente')
                    cliente[1] = nuevoNom
                    self.gestCli.modiClientes(dniCliente,cliente)
                if subMenu == 3:
                    nuevoApe = self.val.stringSinNum('Nuevo Apellido del cliente')
                    cliente[2] = nuevoApe
                    self.gestCli.modiClientes(dniCliente,cliente)
                if subMenu == 4:
                    nuevaDir = self.val.string30('la nueva dirección del cliente')
                    cliente[3] = nuevaDir
                    self.gestCli.modiClientes(dniCliente,cliente)
                if subMenu == 5:
                    nuevoTel = self.val.numero('Nuevo Teléfono',1099999999,11099999999)
                    cliente[4] = nuevoTel
                    self.gestCli.modiClientes(dniCliente,cliente)
                if subMenu == 6:
                    nuevoEmail = self.val.email()
                    cliente[5] = nuevoEmail
                    self.gestCli.modiClientes(dniCliente,cliente)
                if subMenu == 7:
                    selIVA = self.menu.menuSel(self.estadoIVa,3)
                    if selIVA == 1:
                        nuevoEstadoIva = 'Inscripto'
                    elif selIVA == 2:
                        nuevoEstadoIva = 'Exento'
                    else:
                        nuevoEstadoIva = 'Final'
                    cliente[6] = nuevoEstadoIva
                    self.gestCli.modiClientes(dniCliente,cliente)
                if subMenu == 8:
                    nuevoDNI = self.val.numero('Nuevo DNI',1000000,99999999)
                    nuevoNom = self.val.stringSinNum('Nuevo Nombre del cliente')
                    nuevoApe = self.val.stringSinNum('Nuevo Apellido del cliente')
                    nuevaDir = self.val.string30('la nueva dirección del cliente')
                    nuevoTel = self.val.numero('Nuevo Teléfono',1099999999,11099999999)
                    nuevoEmail = self.val.email()
                    selIVA = self.menu.menuSel(self.estadoIVa,3)
                    if selIVA == 1:
                        nuevoEstadoIva = 'Inscripto'
                    elif selIVA == 2:
                        nuevoEstadoIva = 'Exento'
                    else:
                        nuevoEstadoIva = 'Final'
                    estado = 'A'
                    nuevoCli = [nuevoDNI,nuevoNom,nuevoApe,nuevaDir,nuevoTel,nuevoEmail,nuevoEstadoIva,estado]
                    self.gestCli.modiClientes(dniCliente,nuevoCli)
                else:
                    pass
            else:
                print("\nEl DNI ingresado no corresponde a un cliente registrado.\nSe salio del menu de modificación de cliente.")
        else:
            print("\n...Saliendo del menu Clientes.")     
    def menuVentas(self):
        seleccion = self.menu.menuNum(self.ventaDirecta,3)
        if seleccion == 1:
            nuevoDNI = self.val.numero('DNI',1000000,99999999)
            agregarConsFinal = self.base.hacerConsulta('Clientes','DNI_Cli',nuevoDNI)
            if type(agregarConsFinal) == str or agregarConsFinal[7] == 'I':
                nuevoNom = self.val.stringSinNum('Nombre del cliente')
                nuevoApe = self.val.stringSinNum('Apellido del cliente')
                nuevaDir = self.val.string30('la dirección del cliente')
                nuevoTel = self.val.numero('Teléfono',1099999999,11099999999)
                nuevoEmail = self.val.email()
                selIVA = self.menu.menuSel(self.estadoIVa,3)
                if selIVA == 1:
                    nuevoEstadoIva = 'Inscripto'
                elif selIVA == 2:
                    nuevoEstadoIva = 'Exento'
                else:
                    nuevoEstadoIva = 'Final'
                estado = 'A'
                nuevoCli = [nuevoDNI,nuevoNom,nuevoApe,nuevaDir,nuevoTel,nuevoEmail,nuevoEstadoIva,estado]
                self.gestCli.altaCliente(nuevoDNI,nuevoCli)
                
               
            else:
                os.system("cls")
                print(f"""
                ---------------------------------------------------
                -  El DNI corresponde a un cliente ya registrado  -
                -      (verifique los datos con el cliente)       -
                ---------------------------------------------------""")
            
            self.gestVentas.mostrarComprador(nuevoDNI)

            
        elif seleccion==2:
            fecha = self.val.fecha()
            registros = self.base.cantidadVentas('Ventas',fecha)
            if len(registros)>0:
                self.gestVentas.listadoVentas(fecha)
            else:
                print("\nNo existen registros para mostrar. Intente de nuevo más tarde.")
        else:
            print("\n...Saliendo del menu Ventas.")      
    def menuGeneral(self):
        seleccion = self.menu.menuNum(self.menuGral,5)
        if seleccion == 1:
            self.menuProveedores()
        elif seleccion == 2:
            self.menuClientes()
        elif seleccion == 3:
            self.menuArticulos()
        elif seleccion == 4:
            self.menuVentas()
        else:
            print("\n        Cerrando el 'Sistema y Gestión de Abastecimiento'\n                 SUPPLY TECHNOLOGY PLG.SA.")
            print("\n\n...Programa Finalizado.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            exit()
    def menuLoop(self):
        validar=""
        while True:
            try:
                while validar!="NO":
                    self.menuGeneral()
                    self.base.inicializacionBase()
                    validar = input("\nDesea Realizar algo más? si/no: ").upper()
                    if validar!="SI" and validar!="NO":
                        print(f' Por favor ingrese Si o No.')
                    elif validar=="NO":
                        os.system("cls")
                        print("\n       Gracias por usar el 'Sistema y Gestión de Abastecimiento'\n              SUPPLY TECHNOLOGY PLG.SA.")
                        print("\n\n...Programa Finalizado.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                break
            except ValueError:
                print(f'Hubo un error en su ingreso.')

gestionCom = GestionComercial()
gestionCom.menuLoop()