import mariadb

class BaseDeDatos(object):
    def __init__(self):
        self.bd = mariadb.connect(
        host="localhost",
        port=4005,
        user="root",
        password="",
        autocommit=True
        )
        self.cursor = self.bd.cursor()
    def crearBase(self):
        try:
            self.cursor.execute("CREATE DATABASE Gestion_Comercial")
        except mariadb.Error:
            return(f"\nLa base de datos Gestión Comercial, ya habia sido creada.")
    def conectarBaseDeDatos(self):
        self.bd =mariadb.connect(
        host="localhost",
        port=4005,
        user="root",
        password="",
        db = "Gestion_Comercial"
        )
        self.cursor = self.bd.cursor()
    def clientesTabla(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Clientes(DNI_Cli INT PRIMARY KEY,NombreCli VARCHAR (30),ApellidoCli VARCHAR(30),direccionCli VARCHAR(30),telefonoCli BIGINT,mailCli VARCHAR(40),estadoIvaCli VARCHAR(30),estado VARCHAR (1))")
    def proveedoresTabla(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Proveedores(CUIL_CUIT_Prov BIGINT PRIMARY KEY,Nombre_Prov VARCHAR(30),Direccion_Prov VARCHAR(30),Telefono_Prov BIGINT,Mail_Prov VARCHAR(30),estadoIvaProv VARCHAR(30),estado VARCHAR (1))")
    def articulosTabla(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Articulos(codigoBarra BIGINT PRIMARY KEY,nombreArticulo VARCHAR(30),categoriaArt VARCHAR(30),precioArt DECIMAL(8,2),cantidadArt INT,CUIL_CUIT_Prov BIGINT,estado VARCHAR (1),CONSTRAINT `FK_Cuil_Cuit` FOREIGN KEY (`CUIL_CUIT_Prov`) REFERENCES `proveedores` (`CUIL_CUIT_Prov`) ON UPDATE CASCADE ON DELETE RESTRICT)")
    def devolucionesTabla(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Devoluciones(codigoDevolucion INT AUTO_INCREMENT PRIMARY KEY, codigoBarra1 BIGINT,cantidadArt INT,CUIL_CUIT_Prov1 BIGINT,motivoDev VARCHAR(30),fecha DATE, CONSTRAINT `FK2_Cuil_Cuit` FOREIGN KEY (`CUIL_CUIT_Prov1`) REFERENCES `proveedores` (`CUIL_CUIT_Prov`) ON UPDATE CASCADE ON DELETE RESTRICT, CONSTRAINT `FK_Cod_Barra` FOREIGN KEY (`codigoBarra1`) REFERENCES `articulos` (`codigoBarra`) ON UPDATE CASCADE ON DELETE RESTRICT)")
    def ventasTabla(self):
         self.cursor.execute("CREATE TABLE IF NOT EXISTS Ventas(CodigoVent INT AUTO_INCREMENT PRIMARY KEY,fechaVenta DATE,Factura INT,codigoBarraVent BIGINT,nombreArticuloVent VARCHAR(30),CantidadVent INT,Precio_TotalArt DECIMAL(20,2),IVA DECIMAL(20,2),DNI_Cli_Vent INT,NombreCli VARCHAR(30),ApellidoCli VARCHAR(30),estadoIvaCli VARCHAR(30),CONSTRAINT `FK_CodBarraVent` FOREIGN KEY (`codigoBarraVent`) REFERENCES `articulos` (`codigoBarra`) ON UPDATE CASCADE ON DELETE RESTRICT,CONSTRAINT `FK_DNI_Cli` FOREIGN KEY (`DNI_Cli_Vent`) REFERENCES `Clientes` (`DNI_Cli`) ON UPDATE CASCADE ON DELETE RESTRICT)")
    def reposicionTabla(self):
         self.cursor.execute("CREATE TABLE IF NOT EXISTS ordenesDeArticulos(nroOrden INT AUTO_INCREMENT PRIMARY KEY,codigoBarra BIGINT,cantidad INT,nombreArticulo VARCHAR(30),fechaSolicitud DATE,CUIL_CUIT_Prov BIGINT, CONSTRAINT `FK_CodBarraArt` FOREIGN KEY (`codigoBarra`) REFERENCES `articulos` (`codigoBarra`) ON UPDATE CASCADE ON DELETE RESTRICT, CONSTRAINT `FK_Cuil_Cuit_Prov` FOREIGN KEY (`CUIL_CUIT_Prov`) REFERENCES `proveedores` (`CUIL_CUIT_Prov`) ON UPDATE CASCADE ON DELETE RESTRICT)")
    def agregarValores(self):
        sql = "INSERT INTO Clientes (DNI_Cli, NombreCli, ApellidoCli, direccionCli, telefonoCli, mailCli, estadoIvaCli,estado) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)"
        val = [
            (40123033,'Antonella', 'Lopez','Superi 1111',1512345678,'antonella.lopez@hotmail.com','Inscripto','A'),
            (38526847,'Camila', 'Gomez','Monreo 2587',1599887766,'camila.gomez@hotmail.com','Exento','A'),
            (35554845,'Laura', 'Diaz','Cabildo 3333',1522334455,'laura.diaz@hotmail.com','Inscripto','A'),
            (36355478,'Luis', 'Ruiz','Juramento 1300',1154585978,'luis.ruiz@hotmail.com','Final','A'),
            ]
        self.cursor.executemany(sql,val)
        self.bd.commit()
        sql = "INSERT INTO Proveedores (CUIL_CUIT_Prov, Nombre_Prov, Direccion_Prov, Telefono_Prov, Mail_Prov, estadoIvaProv,estado) VALUES (%s, %s, %s, %s, %s,%s,%s)"
        val = [
            (30234568879,'Astro','Montana 125',1168674500,'carla.suarez@astro.com','Inscripto','A'),
            (20369552458,'SMG e hijos','Peron 4500',1123258744,'diego.gregorio@smg.com.ar','Inscripto','A'),
            (20159753354,'Fabian Quinteros','Piedras 25',1145587454,'fabian_1987@hotmail.com','Inscripto','A'),
            (30225474136,'Percant','Brasil 600',1169874521,'juan.perez@percant.com.ar','Inscripto','A')
        ]
        self.cursor.executemany(sql,val)
        self.bd.commit()
        sql = "INSERT INTO Articulos (codigoBarra, nombreArticulo, categoriaArt, precioArt, cantidadArt, CUIL_CUIT_Prov,estado) VALUES (%s, %s, %s, %s, %s,%s,%s)"
        val = [
            (125547888888,'MEMORIA RAM ASTRO 8GB','Memorias',2300.50,4,30234568879,'A'),
            (203500002554,'CPU CORE I3 INTEL','Procesadores',33000.98,3,20159753354,'A'),
            (725547866666,'GABINETE SMG 2300','Gabinetes',12000.00,3,20369552458,'A'),
            (825547877777,'FUENTE 650W PERCANT','Fuentes',6000.00,3,30225474136,'A')
        ]
        self.cursor.executemany(sql,val)
        self.bd.commit()
    def altaCliente(self,nuevoCliente):
        sql = "INSERT INTO Clientes (DNI_Cli, NombreCli, ApellidoCli, direccionCli, telefonoCli, mailCli, estadoIvaCli,estado) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)"
        self.cursor.execute(sql,nuevoCliente)
        self.bd.commit()
    def modificarCliente(self,dniCliente,clienteModificado):
        self.cursor.execute(f"UPDATE Clientes SET estado = '{clienteModificado[7]}',estadoIvaCli = '{clienteModificado[6]}',mailCli = '{clienteModificado[5]}',telefonoCli = '{clienteModificado[4]}',direccionCli = '{clienteModificado[3]}',ApellidoCli = '{clienteModificado[2]}',NombreCli = '{clienteModificado[1]}',DNI_Cli = '{clienteModificado[0]}' WHERE DNI_Cli = {dniCliente}")
        self.bd.commit()
    def altaProveedor(self,nuevoProveedor):
        sql = "INSERT INTO Proveedores (CUIL_CUIT_Prov, Nombre_Prov, Direccion_Prov, Telefono_Prov, Mail_Prov, estadoIvaProv,estado) VALUES (%s, %s, %s, %s, %s,%s,%s)"
        self.cursor.execute(sql,nuevoProveedor)
        self.bd.commit()
    def modificarProveedor(self,cuitProveedor,proveedorModificado):
        self.cursor.execute(f"UPDATE Proveedores SET estado='{proveedorModificado[6]}',EstadoIvaProv = '{proveedorModificado[5]}',Mail_prov = '{proveedorModificado[4]}',Telefono_Prov = '{proveedorModificado[3]}',Direccion_Prov = '{proveedorModificado[2]}',Nombre_Prov = '{proveedorModificado[1]}',CUIL_CUIT_Prov = '{proveedorModificado[0]}' WHERE CUIL_CUIT_Prov = {cuitProveedor}")
        self.bd.commit()
    def altaArticulo(self,nuevoArticulo):
        sql = "INSERT INTO Articulos (codigoBarra, nombreArticulo, categoriaArt, precioArt, cantidadArt, CUIL_CUIT_Prov,estado) VALUES (%s, %s, %s, %s, %s,%s,%s)"
        self.cursor.execute(sql,nuevoArticulo)
        self.bd.commit()
    def ingresarArticulos(self,codigoDeBarraArticulo,CantidadAIngresar):
        self.cursor.execute(f"SELECT * FROM Articulos where codigoBarra = {codigoDeBarraArticulo}")
        resultado = self.cursor.fetchone()
        registro = []
        for campo in resultado:
            registro.append(campo)
        cantidad = registro[4] + CantidadAIngresar
        self.cursor.execute(f"UPDATE Articulos SET cantidadArt = '{cantidad}' WHERE codigoBarra = {codigoDeBarraArticulo}")
        self.bd.commit()
    def modificarArticulo(self,codBarra,articuloModificado):
        self.cursor.execute(f"UPDATE Articulos SET estado ='{articuloModificado[6]}',CUIL_CUIT_Prov='{articuloModificado[5]}',cantidadArt = '{articuloModificado[4]}',precioArt = '{articuloModificado[3]}',categoriaArt = '{articuloModificado[2]}',nombreArticulo= '{articuloModificado[1]}',codigoBarra = '{articuloModificado[0]}' WHERE codigoBarra = {codBarra}")
        self.bd.commit()
    def cambioEstado(self,tabla,campopk,pk,estado):
        self.cursor.execute(f"UPDATE {tabla} SET estado = '{estado}' WHERE {campopk} = {pk}")
        self.bd.commit()
    def registrarVenta(self,nuevaVenta):
        sql = "INSERT INTO Ventas (fechaVenta,Factura,codigoBarraVent,nombreArticuloVent,CantidadVent,DNI_Cli_Vent,Precio_TotalArt,IVA,NombreCli,ApellidoCli,estadoIvaCli) VALUES (%s, %s, %s, %s,%s, %s, %s,%s,%s,%s,%s)"
        self.cursor.execute(sql,nuevaVenta)
        self.bd.commit()
    def registraDevolucion(self,nuevaDevolucion):
        sql = "INSERT INTO Devoluciones (codigoBarra1,cantidadArt,CUIL_CUIT_Prov1,motivoDev,fecha) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql,nuevaDevolucion)
        self.bd.commit()
    def descuentaArticulos(self,codigoArt,cantADescontar):
        self.cursor.execute(f"SELECT * FROM Articulos where codigoBarra = {codigoArt}")
        resultado = self.cursor.fetchone()
        registro = []
        for campo in resultado:
            registro.append(campo)
        cantidad = registro[4] - cantADescontar
        self.cursor.execute(f"UPDATE Articulos SET cantidadArt = '{cantidad}' WHERE codigoBarra = {codigoArt}")
        self.bd.commit()
    def registrarReposicion(self,nuevaReposicion):
        sql = "INSERT INTO ordenesdearticulos (codigoBarra,cantidad,nombreArticulo,fechaSolicitud,CUIL_CUIT_Prov) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql,nuevaReposicion)
        self.bd.commit()
    def borrarRegistro(self,tabla,campo,PK):
        sql = f"DELETE FROM {tabla} WHERE {campo} = '{PK}'"
        self.cursor.execute(sql)
        self.bd.commit()
    def hacerConsulta(self,tabla,campo,dato):
        self.cursor.execute(f"SELECT * FROM {tabla} where {campo} = {dato}")
        resultado = self.cursor.fetchone()
        if not (resultado) is None:
            listaResultado = []
            for registro in resultado:
                listaResultado.append(registro)
            return listaResultado
        else:
            return("\nNo hay registros para el dato consultado.")
    def consultarStock(self,tabla,campo,dato):
        self.cursor.execute(f"SELECT * FROM {tabla} where {campo} = {dato}")
        resultado = self.cursor.fetchall()
        if not (resultado) is None:
            listaResultado = []
            for registro in resultado:
                listaResultado.append(registro)
            return listaResultado
        else:
            return("\nNo hay registros para el dato consultado.")
    def cantidadDeRegistros(self,tabla):
        self.cursor.execute(f"SELECT * FROM {tabla} LIMIT 100")
        registros = self.cursor.fetchall()
        return(list(registros))
    def cantidadVentas(self,tabla,fecha):
        self.cursor.execute(f"SELECT * FROM {tabla} where fechaVenta = '{fecha}'")
        registros = self.cursor.fetchall()
        return(list(registros))
    def inicializacionBase(self):
        self.crearBase()
        self.conectarBaseDeDatos()
        self.clientesTabla()
        self.proveedoresTabla()
        self.articulosTabla()
        self.ventasTabla()
        self.devolucionesTabla()
        self.reposicionTabla()
    def ultimaFactura(self):
        self.cursor.execute("SELECT * FROM Ventas WHERE Factura = (SELECT MAX(Factura) FROM Ventas)")
        registro = self.cursor.fetchone()
        if not (registro) is None:
            return registro[2] + 1 
        else:
            return 0