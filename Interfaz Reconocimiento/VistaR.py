import tkinter
from tkinter import *

ventana = tkinter.Tk()
ventana.geometry("860x484")


Fondo = PhotoImage(file="dwtokio.gif")
lblFondo = Label(ventana, image=Fondo).place(x=0,y=0)


etiqueta = tkinter.Label(ventana, text="Programa de Reconocimiento Facial/Gestos" ).place(x=620, y=15)


Boton1= tkinter.Button(ventana, text = "Entrenamiento de rostro", bg="aquamarine").place(x=640, y=140)
Boton2= tkinter.Button(ventana, text = "Detectar nuevo rostro", bg="SteelBlue1").place(x=640, y= 200)
Boton3= tkinter.Button(ventana, text = "Nuevo Rostro ", bg="bisque2").place(x=640, y=260)
Boton4= tkinter.Button(ventana, text = "Reconocimiento de Gestos", bg="aquamarine").place(x=640, y=320)


ventana.mainloop()



