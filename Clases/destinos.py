from Clases.conectardb import Conectardb

class Destinos:
    
    def __init__(self) -> None:
        self.__conectar = Conectardb()

    def mostrarDestinos(self):

        sql = '''
        SELECT nombre 
        FROM ciudades;
        '''

        ciudades = self.__conectar.listarTodo(sql)

        return ciudades
