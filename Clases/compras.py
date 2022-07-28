
from Clases.conectardb import Conectardb


class Compras:

    def __init__(self, nroTicket = 0, idCompra = 0, rut = '') -> None:
        self.__nroTicket = nroTicket
        self.__idCompra  = idCompra
        self.__rut       = rut
        self.__conectar  = Conectardb()

    def registrarCompra(self):
        sql = f'''
        INSERT INTO compra (id, rut)
        VALUES ({self.__idCompra}, "{self.__rut}")
        '''

        rCompra = self.__conectar.ejecutar(sql)

        if rCompra == 1:
            return 'Su compra fue aceptada, gracias por su preferencia.'
        elif rCompra == 0:
            return 'Lo sentimos, su compra fue rechazada.'
        else:
            return rCompra

    def listarCompras(self):

        sql = f'''
        SELECT c.nroTicket, c.rut, v.horaInicio, v.horaFin, v.ciudadInicio, v.ciudadFin, v.precio
        FROM compra c JOIN viaje v
        USING (id)
        WHERE c.rut = "{self.__rut}" 
        '''

        listar = self.__conectar.listarTodo(sql)

        return listar

    def buscarCodViaje(self):
        sql = f'''
        SELECT id
        FROM compra
        WHERE nroTicket = {self.__nroTicket}
        '''

        buscar = self.__conectar.listarUno(sql)

        return buscar

    def eliminarCompra(self):
        sql = f'''
        DELETE
        FROM compra
        WHERE nroTicket = {self.__nroTicket};
        '''

        eliminar = self.__conectar.ejecutar(sql)

        if eliminar == 1:
            return 'La compra fue eliminada.'
        elif eliminar == 0:
            return 'La compra no se pudo eliminar.' 
        else:
            return eliminar   