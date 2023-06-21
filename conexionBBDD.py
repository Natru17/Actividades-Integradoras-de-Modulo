import mysql.connector

class Conexion:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            user='root',
            password='****',
            host='localhost',
            database='big_bread_production',
            port='3306'
        )

    def conectar(self):
        try:
            self.conexion.connect()
            print("Conexión exitosa a la base de datos")
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos:", error)

    def cerrar_conexion(self):
        self.conexion.close()
        print("Conexión cerrada")

conexion = Conexion()

conexion.conectar()

conexion.cerrar_conexion()
