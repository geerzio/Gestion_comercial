from baseDeDatos import BaseDeDatos
from OpcMenu import *
from validaciones import *
from gestionCliente import *
from gestionArticulos import *
import os
from decimal import Decimal

class gestionVentas(object):
    
    def __init__(self):
        self.gestArt = GestionArticulos()
        self.base = BaseDeDatos()
        self.base.inicializacionBase()
        self.menu = opcMenu()
        self.val = Validacion()
        self.gestCli = GestionCliente()
        self.estadoIVa = (f'''
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            --                      "Estado de IVA"                        --
            -----------------------------------------------------------------
            --  1: Inscripto                                               --
            --  2: Excento                                                 --
            --  3: Final                                                   -- 
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            ''')
    def mostrarComprador(self,nuevoDNI):
        nuevoCli = self.base.hacerConsulta("Clientes","DNI_Cli",nuevoDNI)  
        print(f'''Registro de Comprador:
                DNI de cliente______: {nuevoCli[0]}
                Nombre de cliente___: {nuevoCli[1]}
                Apellido cliente____: {nuevoCli[2]}
                Direccion cliente___: {nuevoCli[3]}
                Telefono cliente____: {nuevoCli[4]}
                Email de cliente____: {nuevoCli[5]}
                Situación IVA cli___: {nuevoCli[6]}
                ''')
        print("\nArtículo Requerido para la Venta:")
        listaArt=[]
        lista=[]
        cantADescontar=0
        cantArt=self.val.numero('la cantidad de codigos de barra a facturar',1,10)
        for ind in range(0,cantArt):
            nuevoCodBarra = self.val.numero('Código de Barra',99999999999,999999999999)
            artVenta = self.base.hacerConsulta("Articulos","codigoBarra",nuevoCodBarra)
            if not type(artVenta) == str and artVenta[6] != 'I':
                print(f'''\nArtículo solicitado para la venta...
                    Código de barra_______: {artVenta[0]}
                    Nombre de artículo____: {artVenta[1]}
                    Categoría de artículo_: {artVenta[2]}
                    Precio Unitario art___: {artVenta[3]}
        --------►   Unidades Disp. stock__: {artVenta[4]}
                    Cuit de proveedor_____: {artVenta[5]}
                    ''')
                cantADescontar=0
                print("\nPuede cancelar ingreso de artículo presionando 'ENTER' de lo contrario...")
                cantADescontar = self.val.numero("número de unidades a vender",1,100)
                totalCompra=artVenta[3]*cantADescontar
                os.system("cls")
                artVenta[4]=cantADescontar            
                listaArt.append(artVenta)
            else:
                print(input("\nEl código de barra ingresado no corresponde a un artículo registrado, genere el alta primero.\nPresione ENTER para continuar...."))
                break
        codBarraVerif=[]
        repetidos = []
        for articulo in listaArt:
            codBarraVerif.append(articulo[0])
        for ind in range(0,len(listaArt)):
            if listaArt[ind][0] in codBarraVerif:
                if listaArt[ind][0] not in repetidos:
                    repetidos.append(listaArt[ind][0])
        if len(repetidos) == cantArt:
            if len(repetidos)==len(codBarraVerif):
                for articulo in listaArt:
                    art = self.base.hacerConsulta('Articulos','codigoBarra',articulo[0])
                    if articulo[4] > art[4]:
                        print("\nLas cantidades seleccionadas superan las existencias")
                        listaArt=[]
                if len(listaArt)!=0:         
                    print("\nCompra Exitosa.\nArtículo solicitado al sector Depósito(descontado del stock)")
                    print("\nArtículos Completos para realizar Factura")

                    print2 = input(f'''
                    •-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•
                        Venta Exitosa...Presione 'ENTER' para terminar Factura
                    •-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•
                    ''')
                
                    os.system("cls")
                        
                    menuFactura=(f'''
                        ELIJA OPCIÓN DE FACTURA
                        Recuerde que el cliente es "{nuevoCli[6]}"
                        ----------------------------------------------
                        -    1: FACTURA (A)  ----►  Inscripto        -
                        -    2: FACTURA (B)  ----►  Final / Exento   -
                        ----------------------------------------------
                        ''')
                    seleccion = self.menu.menuNum(menuFactura,2)
                    os.system("cls")
                    if seleccion==1:
                        print("\nINGRESE DATOS ADICIONALES PARA TERMINAR FACTURACIÓN\n")

                        now = self.val.tiempoAhora()
                        print("\nformato de fecha automática: ",now)

                        numeroFactura1= self.base.ultimaFactura()
                        lista.append(totalCompra)
                        
                        cutiCliente=input("\nIngrese CUIT de cliente: ")
                        os.system("cls")
                        artvendidos = []
                        print(f'''
                                            ♦============================================================♦
                                                                    N° {numeroFactura1}
                                            ♦      ♦                  FACTURA (A)                 ♦      ♦
                                                                                    Fecha: {now}
                                            ♦============================================================♦
                                            ♦ tel: 011-5175-9042       EMPRESA: SUPPLY TECHNOLOGY PLG.SA ♦
                                            ♦      011-6522-1397       Cuit: 30-24769651-2               ♦
                                            ♦                          Dirección: Av.Corrientes 3492     ♦
                                            ♦============================================================♦
                                            Cliente Inscripto (Cuit: {cutiCliente})                   
                                            --------------------------------------------------------------

                                            Nombre Cliente                         {nuevoCli[1]}
                                            Dirección Cliente                      {nuevoCli[3]}
                                            Estado IVA Cliente                     {nuevoCli[6]}
                                            DNI del Cliente                        {nuevoCli[0]}           

                                            ==============================================================
                                            -  ARTICULO/S                                                -
                                            --------------------------------------------------------------
                                ''')
                        
                        resultado=[]
                        total=[]
                        for contar in listaArt:
                            print(f'''
                                            Código de Artículo                     {contar[0]}
                                            Nombre de Artículo                     {contar[1]}
                                            Unidades de Artículo                   {contar[4]}
                                            Precio Unitario                      $ {contar[3]}''')
                            resultado=contar[4]*contar[3]
                            resultado2=float(resultado)
                            total.append(resultado2)
                            artvendidos.append(contar)
                        listaArt=+1
                        resultadoTotal=0
                        resultadoIva=0
                        for contar in total:
                            resultadoTotal=resultadoTotal+contar
                        resultadoIva=resultadoTotal*10.5/100
                        print(f'''    
                                            ♦============================================================♦ 
                            
                        
                                            Montos de compra__SubTotal__Iva 10.5%  $ {"{:.2f}".format(resultadoIva)}
                                                            Total______________$ {"{:.2f}".format(resultadoTotal)}
                                            ♦============================================================♦
                                                    ''')
                        for articulo in artvendidos:
                            precioArticulo = articulo[3]*articulo[4]
                            iva=round(float(precioArticulo)*10.5/100,2)                              
                            vendido=[now,numeroFactura1,articulo[0],articulo[1],articulo[4],nuevoCli[0],precioArticulo,iva,nuevoCli[1],nuevoCli[2],nuevoCli[6]]
                            self.base.descuentaArticulos(articulo[0],articulo[4])
                            self.base.registrarVenta(vendido)
                        




                        
                    else:
                        print("\nINGRESE DATOS ADICIONALES PARA TERMINAR FACTURACIÓN\n")
                        print("\nformato de solicitud fecha: año:0000 - mes:00 - día:00")
                        now = self.val.tiempoAhora()
                        numeroFactura1= self.base.ultimaFactura()
                        
                        os.system("cls")
                        artvendidos = []
                        print(f'''
                                            ==============================================================
                                                                    N° {numeroFactura1}
                                            -      ♦                  FACTURA (B)                 ♦      -
                                                                                Fecha: {now}
                                            ==============================================================
                                            - tel: 011-5175-9042       EMPRESA: SUPPLY TECHNOLOGY PLG.SA -
                                            -      011-6522-1397       Cuit: 30-24769651-2               -
                                            -                          Dirección: Av.Corrientes 3492     -
                                            ==============================================================
                                            -  Cliente Final/Exento                                      -
                                            ==============================================================

                                            Nombre Cliente                         {nuevoCli[1]}
                                            Dirección Cliente                      {nuevoCli[3]}
                                            Estado IVA Cliente                     {nuevoCli[6]}
                                            DNI del Cliente                        {nuevoCli[0]}       

                                            --------------------------------------------------------------
                                            -  ARTICULO/S                                                -
                                            --------------------------------------------------------------
                            ''')
                        
                        resultado=[]
                        total=[]
                        for contar in listaArt:
                            print(f'''
                                            Código de Artículo                     {contar[0]}
                                            Nombre de Artículo                     {contar[1]}
                                            Unidades de Artículo                   {contar[4]}
                                            Precio Unitario                      $ {contar[3]}''')
                            resultado=contar[4]*contar[3]
                            resultado2=float(resultado)
                            total.append(resultado2)
                            artvendidos.append(contar)
                        listaArt=+1
                        resultadoTotal=0
                        for contar in total:
                            resultadoTotal=resultadoTotal+contar
                        print(f'''    
                                            ♦============================================================♦ 
                                                            Total______________$ {"{:.2f}".format(resultadoTotal)}
                                            ♦============================================================♦
                                                        ''')
                        for articulo in artvendidos:                              
                            vendido=[now,numeroFactura1,articulo[0],articulo[1],articulo[4],nuevoCli[0],articulo[4]*articulo[3],0,nuevoCli[1],nuevoCli[2],nuevoCli[6]]
                            self.base.descuentaArticulos(articulo[0],articulo[4])
                            self.base.registrarVenta(vendido)


                else:
                    print("\nOperación cancelada.")
                
            else:
                print("\nSe han ingresado códigos de barra repetidos.\nVerifique las cantidades y vuelva a intentarlo.")
        else:
            os.system('cls')
            print("\nOcurrio un error durante la facturación: Ingreso de artículo no registrado.\nSe canceló la operación.")

    def listadoVentas(self,fecha):
            listaRegistros = []
            registros= self.base.cantidadVentas('Ventas',fecha)
            datos = []
            mlist = []
            for lista in range(0,len(registros)):
                for elemento in range(0,len(registros[lista])):
                    if elemento != 1 and elemento < 11:
                        mlist.append(registros[lista][elemento])
                    elif elemento == 1:
                        mlist.append(str(registros[lista][elemento]))
                    else:
                        mlist.append(str(registros[lista][elemento]))
                        datos.append(mlist)
                        mlist=[]
                    
            for registro in datos:
                listaRegistros.append(list(registro))
                tablaVentas = """\
                                                                
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|     FECHA FACT.        N°FACTURA        COD.BARRA                NOMBRE ART              CANT.ART.          MONTO TOT.              IVA             DNI CLI.    IVA ClIENTE |   
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
{}                                                                                                                                                                                                                   
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+\
"""
                tablaVentas = (tablaVentas.format('\n'.join("| {1:^18} | {2:^12} | {3:^16} | {4:^30} | {5:^10} | {6:^20} | {7:^20} | {8:^10} | {11:^11} |".format(*fila)
                for fila in listaRegistros)))
            print(tablaVentas)