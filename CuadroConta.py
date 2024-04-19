from tkinter import ttk
import tkinter as tk


# poniendo un comentario en esto que todavia no sirve
#Yo tambien voy a poner un comentario
#otro mas
class cuadro(ttk.Treeview):
    def __init__(self):
        super().__init__()
        self.config(self, columns= ("col1", "col2", "col3"))
        w = 80
        columnas =["#0","col1", "col2", "col3"]
        for i in range(0,len(columnas)-1):
            self.column(columnas[i], width=w, anchor="center")
        nombres_columnas = ["Ventas", "Pagos", "Ingresos", "Egresos"]
        for i in range(0,len(columnas)-1):
            self.heading(columnas[i], text= nombres_columnas[i], anchor= "center")
