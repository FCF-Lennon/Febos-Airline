from Clases.conectardb import Conectardb


class Viajes:
    
    def __init__(self, idViaje = 0, ciuInicio = '', ciuDestino = '') -> None:
        self.__idViaje = idViaje
        self.__ciuInicio = ciuInicio
        self.__ciuDestino = ciuDestino
        self.__conectar = Conectardb()

    def buscarViajes(self):
        sql = f'''
        SELECT *
        FROM viaje
        WHERE ciudadInicio = "{self.__ciuInicio}"
        AND ciudadFin = "{self.__ciuDestino}"
        AND cantidad > 0;
        '''

        listarViajes = self.__conectar.listarTodo(sql)
                
        return listarViajes 

    def rCantidad(self):
        sql = f'''
        UPDATE viaje
        SET cantidad = cantidad - 1
        WHERE id = {self.__idViaje};
        '''
        resultado = self.__conectar.ejecutar(sql)

        return resultado
    
    def sCantidad(self):
        sql = f'''
        UPDATE viaje
        SET cantidad = cantidad + 1
        WHERE id = {self.__idViaje};
        '''
        resultado = self.__conectar.ejecutar(sql)

        return resultado

    def verificarID(self):
        sql = f'''
        SELECT id
        FROM viaje
        WHERE ciudadInicio = "{self.__ciuInicio}"
        AND ciudadFin = "{self.__ciuDestino}"
        AND cantidad > 0
        AND id = {self.__idViaje};
        '''
        mostarViaje = self.__conectar.listarTodo(sql)

        return mostarViaje