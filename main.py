
from tkinter import *
from tkinter import Tk, messagebox, ttk 
import tkinter as tk

from Clases.compras import Compras
from Clases.destinos import Destinos
from Clases.usuario import Usuario
from Clases.viajes import Viajes


def inicioSesion():
    
    c = Usuario(rut = rutI.get(), password= passwI.get())
    
    resultado = c.iniciarSesion()

    if etrUser.get() == '' or etrPassw.get() == '':
        messagebox.showerror('Error', 'Debe ingresar el usuario y contraseña.')
    else:
        try:
            if resultado is None:
                messagebox.showwarning('Advertencia', 'Rut o contraseña incorrectos.')
            else:
                messagebox.showinfo('Información', 'Se ha iniciado sesión.')
                openApp()
                btn_login.config(state='disabled')
        except:
            messagebox.showerror('Error', 'Se ha producido un error.')

def botonCrearUsuario():
    frmContenedor2.grid(column=1,row=0, sticky='nsew')
    etrUser.delete(0, 'end')
    etrPassw.delete(0,'end')
    etr_rRut.focus()
    
def regUsuario():

    user = Usuario(rut=rRut.get(), nombre= rNombre.get().title(), email= rEmail.get(), password=rPass1.get())

    if rRut.get() == '' or rNombre.get() == '' or rEmail.get() == '' or  rPass1.get() == '' or rPass2.get() == '':
        messagebox.showerror('Error', 'Todos los campos son obligatorios.')
    else:

        bRut = user.buscarRut()
        bEmail = user.buscarEmail()

        if rPass1.get() != rPass2.get():
            messagebox.showerror('Error', 'Las contraseñas deben ser iguales.')

        if bRut == True and bEmail == True and  rPass1.get() == rPass2.get():
            mensaje = user.registarUsuario()
            limpiarRegistrar()
            messagebox.showinfo('Información', mensaje)
            
def limpiarRegistrar():

    etr_rRut.delete(0, 'end')
    etr_rNombre.delete(0, 'end')
    etr_rEmail.delete(0, 'end')
    etr_rPass1.delete(0, 'end')
    etr_rPass2.delete(0, 'end')
    frmContenedor2.grid_forget()
    etrUser.focus()

def openApp():
    # --------------------------------------------------------------- VENTANA MYAPP
    myLogin.withdraw()

    def mPlanVuelo():
        for widget in myApp.winfo_children():
            widget.pack_forget()

        frmVuelos.pack()
        frmReservas.pack_forget()

        limpiar()

    def mAdministraVuelo():
        for widget in myApp.winfo_children():
            widget.pack_forget()

        frmAdmVuelo.pack()
        limpiarAdm()

    def listarBusqueda():

        if ciudadOrigen.get() == '' or ciudadDestino.get() == '':
            cbox_ciuOrigen.focus()
            messagebox.showerror('Error', 'Antes de realizar la busqueda de su viaje, debes llenar Origen y Destino.')
        
        else:

            v = Viajes(ciuInicio = ciudadOrigen.get(), ciuDestino = ciudadDestino.get())
            viajes = v.buscarViajes()

            for i in tabla.get_children():
                tabla.delete(i)

            if len(viajes) == 0: 
            
                limpiar()
                
                messagebox.showwarning('Lo sentimos', 'No hay covertura de vuelo para su destino.')
                cbox_ciuOrigen.focus()
            
            elif len(viajes) > 0:
                
                contador = 0

                for v in viajes:

                    tabla.insert(
                        parent = "", 
                        index = "end", 
                        iid = contador, 
                        values = (
                            v[0],
                            v[1], 
                            v[2],
                            v[3],
                            v[4],
                            v[5],
                            v[6]
                            )
                        )

                    contador += 1
                frmVuelosDisp.pack()
                etr_vID.focus()

    def efectuarCompra():

        if idVuelo.get() == '':
            limpiar()
            messagebox.showerror('Error', 
        ''' Antes de realizar la compra: 

        1. Debe realizar la búsqueda del viaje. 
        2. Luego ingresar los datos: 

                codigo de vuelo  

        de antemano gracias por preferirnos.''')
        

        else:

            v = Viajes(idViaje = idVuelo.get(), ciuInicio= ciudadOrigen.get(), ciuDestino = ciudadDestino.get())
            c = Compras(idCompra = idVuelo.get(), rut = sRut.get())

            lviaje = v.buscarViajes()
            print(len(lviaje))

            verificarID = v.verificarID()
            
            if verificarID == []:
                etr_vID.delete(0, 'end')
                messagebox.showerror('Error', 'El número de vuelo no existe.')
                etr_vID.focus()
            
            else:
                v.rCantidad()
                compra = c.registrarCompra()
                messagebox.showinfo('Informacion', compra)

                if len(lviaje) > 0:
                    listarBusqueda()
                else:
                    limpiar()

    def limpiar():

        if cbox_ciuOrigen != '' or cbox_ciuDestino != '':
            cbox_ciuOrigen['state'] = 'normal' 
            cbox_ciuDestino['state'] = 'normal' 
            cbox_ciuDestino.delete(0, 'end')
            cbox_ciuOrigen.delete(0, 'end')
            cbox_ciuOrigen.focus()
            cbox_ciuOrigen['state'] = 'readonly'
            cbox_ciuDestino['state'] = 'readonly'

            for i in tabla.get_children():
                tabla.delete(i)
            
            frmVuelosDisp.pack_forget()

        if  etr_vID != '':
            etr_vID.delete(0, 'end')

    def buscarReservas():

        c = Compras(rut = delRut.get())
        u = Usuario(rut = delRut.get())
        listar = c.listarCompras()

        if len(listar) == 0:
            messagebox.showinfo('Informacion', 'Estimado cliente no tiene reservas.')
        
        else:
                
            for i in tabla_eli.get_children():
                    tabla_eli.delete(i)

            contador = 0

            for l in listar:

                tabla_eli.insert(parent = '', index = 'end', iid = contador, values = (
                    l[0],
                    l[1],
                    l[2],
                    l[3],
                    l[4],
                    l[5],
                    l[6]
                )
                
            )

                contador += 1
            frmReservas.pack()

    def eliminarCompra(): 

        if nroTicket.get() != '':

            c = Compras(nroTicket = nroTicket.get(), rut = delRut.get())

            id = c.buscarCodViaje()
            if id is None:
                messagebox.showerror('Error', 'El numero de Ticket no existe.')
            else:
                id = id[0]
                v = Viajes(idViaje = id)
                v.sCantidad()
                eCompra = c.eliminarCompra()
                messagebox.showinfo('Información', eCompra)
            
                resultado = c.listarCompras()

                if len(resultado) > 0:
                    buscarReservas()
                    etr_delTicket.delete(0, 'end')
                    etr_delTicket.focus()
                else:
                    limpiarAdm()
        else:
            messagebox.showerror('Error', 

        ''' Antes de eliminar la Reserva: 

        1. Debe realizar la búsqueda de reserva. 
        2. Luego ingresar los datos: 

                Numero de Ticket 

        Los campos son obligatorios.''')

    def limpiarAdm():

        if  etr_delTicket != '':
            etr_delTicket.delete(0, 'end')
            etr_delTicket.focus()

            for i in tabla_eli.get_children():
                tabla_eli.delete(i)
            
            frmReservas.pack_forget() 

    def cerrarSesion():

        etrUser.delete(0, 'end')
        etrPassw.delete(0,'end')
        etrUser.focus()
        btn_login.config(state='normal')
        myApp.destroy()
        myLogin.deiconify()

    ciudades = Destinos()
    
    myApp = tk.Toplevel(myLogin)
    myApp.title('Febos Airline')
    myApp.iconbitmap('Favicon/febos_icon.ico')

    # .......................................... ESTRUCTURA MENU y SubMENU
    menubar = Menu(myApp)
    myApp.config(menu = menubar)

    sMenu = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'Vuelos',  menu = sMenu)
    menubar.add_cascade(label = 'Logout', command = cerrarSesion)

    sMenu.add_cascade(label = 'Planifica tu Viaje', command = mPlanVuelo, background='white')
    sMenu.add_cascade(label = 'Administra tu Vuelo', command = mAdministraVuelo, background = 'white')


    # .......................................... ESTRUCTURA BUSCAR/COMPRAR VUELO

    """ FRAMES ----------------------- """
    frmVuelos = Frame(myApp, bg='white')
    frmVuelos.pack()

    frmPlanVuelo = Frame(frmVuelos, bg='white')
    frmPlanVuelo.pack(side = 'left', fill = 'y')

    frmPanelVuelo = Frame(frmPlanVuelo)
    frmPanelVuelo.pack()

    """ LABEL  BUSCAR ---------------- """

    lbl_Buscar = Label(
        frmPanelVuelo, 
        text = 'Planifica tu Viaje', 
        font = ('Arial', 15),
        bg = '#fe0197',
        fg = 'white',
        borderwidth = 0
        )

    lbl_Buscar.grid(
        column = 0,
        row =   0,
        sticky = 'nsew',
        columnspan = 2
    )

    """ LABEL ----------------------- """

    lbl_ciuOrigen = Label(
        frmPanelVuelo, 
        text = 'Origen', 
        font = 'Arial'
        )

    lbl_ciuOrigen.grid(
        column = 0,
        row =   1,
        sticky = 'w',
        padx=2,
    )

    lbl_ciuDestino = Label(
        frmPanelVuelo, 
        text = 'Destino', 
        font = 'Arial'
        )

    lbl_ciuDestino.grid(
        column = 0,
        row =   2,
        sticky = 'w',
        padx=2,
    )

    """ COMBOBOX -------------------- """

    ciudadOrigen = StringVar()
    ciudadDestino = StringVar()

    cbox_ciuOrigen = ttk.Combobox(frmPanelVuelo, width = 15, state = 'readonly', values = ciudades.mostrarDestinos(), textvariable = ciudadOrigen)
    cbox_ciuOrigen.grid(
        column = 1,
        row = 1,
        sticky = 'ew',
        padx = 2,
        pady = 2
    )

    cbox_ciuDestino = ttk.Combobox(frmPanelVuelo, width = 15, state = 'readonly', values = ciudades.mostrarDestinos(), textvariable = ciudadDestino)
    cbox_ciuDestino.grid(
        column = 1,
        row = 2,
        sticky = 'ew',
        padx = 2,
        pady =2
    )

    """ BUTTON -------------------- """

    btn_buscarViaje = Button(
        frmPanelVuelo,
        text = 'Buscar Viaje',
        fg = 'white',
        bg = '#671e75',
        relief = 'groove',
        borderwidth = 0,
        command = listarBusqueda
    )

    btn_buscarViaje.grid(
        columnspan = 2,
        column = 0,
        row = 3,
        sticky = 'ew'
    )

    """ LABEL REGISTRAR COMPRA ---- """

    lbl_rCompra = Label(
        frmPanelVuelo, 
        text = 'Registra tu compra', 
        font = ('Arial', 15),
        bg = '#339900',
        fg = 'white',
        borderwidth = 0
        )

    lbl_rCompra.grid(
        column = 0,
        row =   4,
        sticky = 'nsew',
        columnspan = 2
    )

    """ LABEL ----------------------- """


    lbl_rut = Label(
        frmPanelVuelo, 
        text = 'Rut', 
        font = 'Arial'
        )

    lbl_rut.grid(
        column = 0,
        row =   5,
        sticky = 'w',
        padx=2
    )

    lbl_nombre = Label(
        frmPanelVuelo, 
        text = 'Nombre', 
        font = 'Arial'
        )

    lbl_nombre.grid(
        column = 0,
        row =   6,
        sticky = 'w',
        padx=2
    )

    lbl_vID = Label(
        frmPanelVuelo, 
        text = 'Vuelo', 
        font = 'Arial'
        )

    lbl_vID.grid(
        column = 0,
        row =   7,
        sticky = 'w',
        padx=2
    )

    """ ENTRY ------------------- """

    u = Usuario(rut=rutI.get())
    busqueda = u.buscarSesion()

    idVuelo = StringVar()
    sRut = StringVar()
    sNombre = StringVar()

    sRut.set(busqueda[0])
    sNombre.set(busqueda[1])

    etr_rut = Entry(frmPanelVuelo, width = 15, textvariable = sRut, state='readonly')
    etr_rut.grid(
        column = 1,
        row = 5,
        sticky = 'ew',
        pady=2,
        padx=2
    )

    etr_nombre = Entry(frmPanelVuelo, width = 15, textvariable = sNombre, state='readonly')
    etr_nombre.grid(
        column = 1,
        row = 6,
        sticky = 'ew',
        padx=2,
        pady=2
    )

    etr_vID = Entry(frmPanelVuelo, width = 15, textvariable = idVuelo)
    etr_vID.grid(
        column = 1,
        row = 7,
        sticky = 'ew',
        padx=2,
        pady=2
    )

    """ BUTTON -------------------- """

    btn_compra = Button(
        frmPanelVuelo,
        text = 'comprar',
        fg = 'white',
        bg = '#671e75',
        relief = 'groove',
        borderwidth = 0,
        command = efectuarCompra
    )

    btn_compra.grid(
        columnspan = 1,
        column = 0,
        row = 8,
        sticky = 'ew'
    )

    btn_cancelar = Button(
        frmPanelVuelo,
        text = 'cancelar',
        fg = 'white',
        bg = '#fe0197',
        relief = 'groove',
        borderwidth = 0,
        command = limpiar
    )

    btn_cancelar.grid(
        columnspan = 1,
        column = 1,
        row = 8,
        sticky = 'ew'
    )

    """ ESTRUCTURA TABLA ------------- """

    frmVuelosDisp = Frame(frmVuelos, bg = 'white')
    frmVuelosDisp.pack(side = 'left', fill = 'y')
    frmVuelosDisp.pack_forget()

    frmTabla = Frame(frmVuelosDisp)
    frmTabla.pack()
    frmTabla.configure(borderwidth=0)

    lbl_tabla = Label(
        frmTabla, 
        text    = "Vuelos Disponibles",
        font    = ("Arial", 15),
        bg      = "#339900",
        fg      = "white",
        borderwidth = 0
    ).pack(expand = True, fill = "x")


    tabla = ttk.Treeview(frmTabla, height = 8, selectmode ='browse') 
    tabla["columns"] = ("ID", "Hora Salida", "Hora Llegada", "Origen", "Destino", "Precio", "Cantidad") 

    tabla.column("#1", width = 80, anchor = 'e')
    tabla.column("#2", width = 80, anchor = 'e')
    tabla.column("#3", width = 80, anchor = 'e')
    tabla.column("#4", width = 80, anchor = 'e' )
    tabla.column("#5", width = 85, anchor = 'e')
    tabla.column("#6", width = 85, anchor = 'e')
    tabla.column("#7", width = 70, anchor = 'e')

    tabla.heading("ID", text = "Nro. Vuelo", anchor = CENTER) 
    tabla.heading("Hora Salida", text = "HoraSalida", anchor = CENTER) 
    tabla.heading("Hora Llegada", text = "Hora Llegada", anchor = CENTER) 
    tabla.heading("Origen", text = "Origen", anchor = CENTER) 
    tabla.heading("Destino", text = "Destino", anchor = CENTER) 
    tabla.heading("Precio", text = "Precio", anchor = CENTER) 
    tabla.heading("Cantidad", text = "Cantidad", anchor = CENTER) 

    tabla.pack(side = LEFT)
    tabla.configure(show = 'headings')


    """ ESTRUCTURA SCROLLBAR VERTICAL """

    scrollbar  = Scrollbar(frmTabla, orient = "vertical", command=tabla.yview)
    scrollbar.pack(side = 'right', fill = "both")
    tabla.configure(yscroll=scrollbar.set)

    # .......................................... ESTRUCTURA ADMINISTRA TU VUELO

    """ FRAMES ----------------------- """
    frmAdmVuelo = Frame(myApp, bg='white')
    frmAdmVuelo.pack_forget()

    frmPanelEliminar = Frame(frmAdmVuelo)
    frmPanelEliminar.pack(side='left', fill='y')


    """ LABEL ------------------------ """

    lbl_AdmVuelo = Label (
        frmPanelEliminar,
        text = 'Administra tu vuelo',
        font = ('Arial', 15),
        bg = '#fe0197',
        fg = 'white',
        borderwidth = 0,
        )
    lbl_AdmVuelo.grid(
        column = 0,
        row =   0,
        sticky = 'nsew',
        columnspan = 2,
        ipadx=2
    )

    lbl_delRut = Label (
        frmPanelEliminar,
        text = 'Rut',
        font = 'Arial'
        )
    lbl_delRut.grid(
        column = 0,
        row =   1,
        sticky = 'w',
        padx=2
    )

    lbl_delNombre = Label (
        frmPanelEliminar,
        text = 'Nombre',
        font = 'Arial'
        )
    lbl_delNombre.grid(
        column = 0,
        row =   2,
        sticky = 'w',
        padx=2
    )

    lbl_delTicket = Label (
        frmPanelEliminar,
        text = 'Ticket',
        font = 'Arial'
        )
    lbl_delTicket.grid(
        column = 0,
        row =   4,
        sticky = 'w',
        padx=2
    )

    """ TEXTBOX  --------------- """

    u = Usuario(rut = etrUser.get())
    busq = u.buscarSesion()
    
    delRut = StringVar()
    delNombre = StringVar()
    nroTicket = StringVar()

    delRut.set(busq[0])
    delNombre.set(busq[1])

    etr_delRut = Entry(frmPanelEliminar, width = 15, textvariable = delRut, state = 'readonly')
    etr_delRut.grid(
        column = 1,
        row = 1,
        sticky = 'ew',
        padx=2,
        pady=2
    )

    etr_delNombre = Entry(frmPanelEliminar, width = 15, textvariable = delNombre, state = 'readonly')
    etr_delNombre.grid(
        column = 1,
        row = 2,
        sticky = 'ew',
        padx=2,
        pady=2
    )

    etr_delTicket = Entry(frmPanelEliminar, width = 15, textvariable = nroTicket)
    etr_delTicket.grid(
        column = 1,
        row = 4,
        sticky = 'ew',
        padx=2,
        pady=2
    )

    """ BUTTON BUSCAR RESERVAS, ELIMINAR, CANCELAR  ------ """

    btn_buscarReservas = Button(
        frmPanelEliminar,
        text = 'Buscar Reservas',
        fg = 'white',
        bg = '#671e75',
        relief = 'groove',
        borderwidth = 0,
        command = buscarReservas
    )
    btn_buscarReservas.grid(
        columnspan = 2,
        column = 0,
        row = 3,
        sticky = 'ew'
    )

    btn_eliminar = Button(
        frmPanelEliminar,
        text = 'eliminar',
        fg = 'white',
        bg = '#671e75',
        relief = 'groove',
        borderwidth = 0,
        command = eliminarCompra
    )
    btn_eliminar.grid(
        columnspan = 1,
        column = 0,
        row = 5,
        sticky = 'ew'
    )

    btn_delCancelar = Button(
        frmPanelEliminar,
        text = 'cancelar',
        fg = 'white',
        bg = '#fe0197',
        relief = 'groove',
        borderwidth = 0,
        command = limpiarAdm
    )
    btn_delCancelar.grid(
        columnspan = 1,
        column = 1,
        row = 5,
        sticky = 'ew'
    )

    """ ESTRUCTURA TABLA ------------- """

    frmReservas = Frame(frmAdmVuelo, bg = 'white')
    frmReservas.pack(side='left', fill = 'both', expand = True)
    frmReservas.pack_forget()

    frmTablaEliminar = Frame(frmReservas, bg = 'white')
    frmTablaEliminar.pack(expand = True, fill= 'both')

    tabla_eli   = Label(
        frmTablaEliminar, 
        text    = "Reservas",
        font    = ("Arial", 15),
        bg      = "#339900",
        fg      = "white",
        borderwidth = 0
    ).pack(expand = True, fill = "x")

    tabla_eli = ttk.Treeview(frmTablaEliminar, height = 4, selectmode ='browse') 
    tabla_eli["columns"] = ("Nro Ticket", "Rut", "Hora Salida", "Hora Llegada", "Origen", "Destino", "Precio")


    tabla_eli.column("#1", width = 80, anchor= 'e')
    tabla_eli.column("#2", width = 80, anchor= 'e')
    tabla_eli.column("#3", width = 80, anchor= 'e')
    tabla_eli.column("#4", width = 85, anchor= 'e')
    tabla_eli.column("#5", width = 85, anchor= 'e')
    tabla_eli.column("#6", width = 85, anchor= 'e')
    tabla_eli.column("#7", width = 60, anchor= 'e')

    tabla_eli.heading("Nro Ticket", text="Nro Ticket", anchor=CENTER)
    tabla_eli.heading("Rut", text="Rut", anchor=CENTER)
    tabla_eli.heading("Hora Salida", text="Hora salida", anchor=CENTER)
    tabla_eli.heading("Hora Llegada", text="Hora Llegada", anchor=CENTER)
    tabla_eli.heading("Origen", text="Origen", anchor=CENTER)
    tabla_eli.heading("Destino", text="Destino", anchor=CENTER)
    tabla_eli.heading("Precio", text="Precio", anchor=CENTER)

    tabla_eli.pack(side = LEFT)
    tabla_eli.configure(show = 'headings')


    """ ESTRUCTURA SCROLLBAR VERTICAL """

    scrollbar_eli  = Scrollbar(frmTablaEliminar, orient = "vertical", command=tabla_eli.yview)
    scrollbar_eli.pack(side = 'right', fill = "both")
    tabla_eli.configure(yscroll=scrollbar_eli.set)

    myApp.resizable(0, 0)

myLogin = Tk()
myLogin.eval('tk::PlaceWindow . center')
myLogin.title('Febos Airline')
myLogin.iconbitmap('Favicon/febos_icon.ico')



#------------------------- ESTRUCTURA LOGIN

''' IMAGEN LOGIN -------------- '''

logo = PhotoImage(file="Favicon/logo100x100.png")


''' FRAME LOGIN -------------- '''

frmContenedor1 = Frame(myLogin)
frmContenedor1.grid(column=0, row=0, pady=2)

frm_btncCuenta =  Frame(frmContenedor1, bg='white')
frm_btncCuenta.pack(fill='x')

frmLogo = Frame(frmContenedor1)
frmLogo.pack()

frmLogin = Frame (frmContenedor1)
frmLogin.pack(expand=1, fill='x')

frmPanelLogin = LabelFrame(frmLogin, text='Login', font= ('Arial', 20))
frmPanelLogin.pack(expand=True, fill='x', padx=20, ipady=3)

frm_btnLogin  = Frame(frmLogin)
frm_btnLogin.pack(expand=True, fill='x') 


''' LABEL LOGIN -------------- '''

lbl_logo = Label(frmLogo, image=logo)
lbl_logo.grid(column=0, row=0, pady=5)

lbl_user = Label(frmPanelLogin, text='Rut:', anchor='w')
lbl_user.grid(column=0, row=1, sticky='nsew', padx=3)

lbl_passw = Label(frmPanelLogin, text= 'Contraseña:', anchor = 'w')
lbl_passw.grid(column=0, row=3, sticky='nsew', padx=3)

''' ENTRY LOGIN -------------- '''

rutI = StringVar()
passwI = StringVar()

etrUser = Entry(frmPanelLogin, width=24, textvariable = rutI, relief='flat')    
etrUser.grid(column=0, row=2, padx=3)
etrUser.focus()
etrPassw = Entry(frmPanelLogin, width=24, textvariable = passwI, show='*', relief='flat')
etrPassw.grid(column=0, row=4, padx=3) 

''' BUTTON LOGIN -------------- '''

btn_cCuenta = Button(frm_btncCuenta, text='Crear Cuenta', height=1, border=0, bg='white', fg= '#671e75', activebackground='white', command=botonCrearUsuario)
btn_cCuenta.pack(side=RIGHT, padx=2)

btn_login = Button(frm_btnLogin, text='LOG IN', height=1, relief=GROOVE, bg='#671e75', fg='white', border=0, command=inicioSesion)
btn_login.pack(expand=True, fill=X, padx=20, pady=8)


#------------------------- ESTRUCTURA REGISTRAR CUENTA

''' FRAME -------------- '''

frmContenedor2 = Frame(myLogin, bg='white')
frmContenedor2.grid_forget()

frm_Registrar = Frame(frmContenedor2, bg='white')
frm_Registrar.pack(expand=True, fill=BOTH, padx=20)

frm_btnRegCan = Frame(frmContenedor2, bg='white', width=24)
frm_btnRegCan.pack(expand=True, fill=BOTH, padx=20)


''' LABEL -------------- '''

lbl_Registrarse = Label(frm_Registrar, text='Registro', font = ('Arial', 20), anchor='w', bg='white', fg='#671e75')
lbl_Registrarse.grid(column=0, row=0, sticky='we')

lbl_rRut = Label(frm_Registrar, text='Rut:', anchor='w', bg='white')
lbl_rRut.grid(column=0, row=1, sticky='w')

lbl_rNombre = Label(frm_Registrar, text='Nombre:', anchor='w', bg='white')
lbl_rNombre.grid(column=0, row=3, sticky='w')

lbl_rEmail = Label(frm_Registrar, text='Email:', anchor='w', bg='white')
lbl_rEmail.grid(column=0, row=5, sticky='w')

lbl_rPass1 = Label(frm_Registrar, text='Contraseña:', anchor='w', bg='white')
lbl_rPass1.grid(column=0, row=7, sticky='w')

lbl_rPass2 = Label(frm_Registrar, text='Repita Contraseña:', anchor='w', bg='white')
lbl_rPass2.grid(column=0, row=9, sticky='w')


''' ENTRY -------------- '''

rRut = StringVar()
rNombre = StringVar()
rEmail = StringVar()
rPass1 = StringVar()
rPass2 = StringVar()

etr_rRut = Entry(frm_Registrar, width=24, relief='flat', bg='#f0f0f0', textvariable= rRut)
etr_rRut.grid(column=0, row=2)

etr_rNombre = Entry(frm_Registrar, width=24, relief='flat', bg='#f0f0f0', textvariable= rNombre)
etr_rNombre.grid(column=0, row=4)

etr_rEmail = Entry(frm_Registrar, width=24, relief='flat', bg='#f0f0f0', textvariable=rEmail)
etr_rEmail.grid(column=0, row=6)

etr_rPass1 = Entry(frm_Registrar, width=24, relief='flat', bg='#f0f0f0', textvariable=rPass1)
etr_rPass1.grid(column=0, row=8)

etr_rPass2 = Entry(frm_Registrar, width=24, relief='flat', bg='#f0f0f0', textvariable= rPass2)
etr_rPass2.grid(column=0, row=10)


''' BUTTON -------------- '''

btn_Reg = Button(frm_btnRegCan, text='REGISTRAR', relief=GROOVE, bg='#671e75', fg='white', border=0, command=regUsuario)
btn_Reg.grid(column=0, row=0, sticky='ew', ipadx=2)

btn_Can = Button(frm_btnRegCan, text='CANCELAR', relief=GROOVE, bg='#fe0197', fg='white', border=0, command=limpiarRegistrar)
btn_Can.grid(column=1, row=0, sticky='ew', ipadx=6)


myLogin.resizable(0, 0)
myLogin.mainloop()