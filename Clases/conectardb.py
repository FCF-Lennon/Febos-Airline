
import mysql.connector

class Conectardb:
    
    def __init__(self) -> None:
        self.__conectar = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'proyectovb50'
        )

        self.__cursor = self.__conectar.cursor()


    def ejecutar(self, sql):
        try:
            self.__cursor.execute(sql)
            self.__conectar.commit()
            valor = self.__cursor.rowcount
            return valor

        except mysql.connector.Error as e:
            return 'Error: '+str(e)

    def listarTodo(self, sql):
        try:
            self.__cursor.execute(sql)
            lista = self.__cursor.fetchall()
            return lista

        except mysql.connector.Error as e:
            return 'Error: '+str(e)

    def listarUno(self,sql):
        try:
            self.__cursor.execute(sql)
            lista = self.__cursor.fetchone()
            return lista

        except mysql.connector.Error as e:
            return 'Error: '+str(e)