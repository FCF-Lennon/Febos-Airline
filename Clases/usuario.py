
from tkinter import messagebox
from Clases.conectardb import Conectardb

class Usuario:
    def __init__(self, rut = '', nombre = '', password = '', email = '') -> None:
        self.__rut = rut
        self.__nombre = nombre
        self.__password = password
        self.__email = email
        self.__conectar = Conectardb()
        

    def iniciarSesion(self):
        sql = f'''
        SELECT rut, nombre 
        FROM usuarios 
        WHERE rut = "{self.__rut}"
        AND password = "{self.__password}"; 
        '''
        resultado = self.__conectar.listarUno(sql)

        return resultado

    def registarUsuario(self):
        sql = f'''
        INSERT INTO usuarios (rut, nombre, email, password)
        VALUES ("{self.__rut}","{self.__nombre}", "{self.__email}", "{self.__password}")
        '''

        rUsuario = self.__conectar.ejecutar(sql)

        if rUsuario == 1:
            return f'La cuenta fue registrada, {self.__nombre} puedes iniciar sesión.'
        elif rUsuario == 0:    
            return 'No fue posible registrar la cuenta.'
        else:
            return rUsuario

    def buscarEmail(self):
        sql = f'''
        SELECT *
        FROM usuarios
        WHERE email = "{self.__email}"
        ''' 
        e = self.__conectar.listarUno(sql)

        if e == None:
            e = True
        else:
            if len(e) > 0:
                return messagebox.showerror('Error', 'El email tiene una cuenta registrada.')
        return e

    def buscarRut(self):
        sql = f'''
        SELECT rut
        FROM usuarios
        WHERE rut = "{self.__rut}"
        ''' 
        r = self.__conectar.listarUno(sql)

        if r == None:
            r = True
        else:
            if len(r) > 0:
                return messagebox.showerror('Error', 'El rut ya tiene una cuenta registrada.')
        return r

    def buscarSesion(self):
        sql = f'''
        SELECT rut, nombre
        FROM usuarios
        WHERE rut = "{self.__rut}" 
        '''

        listar = self.__conectar.listarUno(sql)

        return listar