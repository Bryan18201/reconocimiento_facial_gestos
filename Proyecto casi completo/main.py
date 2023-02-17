import tkinter as tk
from tkinter import filedialog,messagebox
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import Guardar_Rostro as GR
import Entrenamiento as Entre
import Reconocimiento as Rec
import ReconociminetoGestos as gestos
import os

window=tk.Tk()
window.title("Proyecto Final Reconocimiento")
l1=tk.Label(window,text="Nombre",font=("Algerian",20))
l1.grid(column=0, row=0)
t1=tk.Entry(window,width=50,bd=5)
t1.grid(column=1, row=0)

def entrenar():
    if os.path.exists('./Data'):
        messagebox.showinfo('Result','Iniciando entrenamiento')
        Entre.entrenamiento()
        messagebox.showinfo('Result','Entrenamiento terminado')
    else:
        messagebox.showinfo('Result','No existen rostros registrados')
        
def NuevoRostro():
    if (t1.get() == ""):
        messagebox.showinfo('Result','Por favor digite un nombre')
    else:
        GR.guardar_Rostro(t1.get())
def Reconocer():
    if os.path.exists('modeloEigenFace.xml'):
        Rec.Reconocimiento()
    else:
        messagebox.showinfo('Result','Por favor primero entrene el modelo')

def manos():
    messagebox.showinfo('Result','Presione (i) para que se le muestre un cuadro donde se hara el reconocimiento de gestos')
    gestos.gestos_mano()
        


b1=tk.Button(window,text="Entrenamiento de rostro",font=("Algerian",20),bg='green',fg='white',command=entrenar)
b1.grid(column=0, row=4)

b2=tk.Button(window,text="Nuevo rostro",font=("Algerian",20),bg='orange',fg='red',command=NuevoRostro)
b2.grid(column=1, row=4)

b3=tk.Button(window,text="Detectar rostro",font=("Algerian",20),bg='blue',fg='white',command=Reconocer)
b3.grid(column=2, row=4)

b4=tk.Button(window,text="Reconocimiento de gestos",font=("Algerian",20),bg='red',fg='white',command=manos)
b4.grid(column=1, row=8, pady=(20))



window.geometry("1050x300")
window.mainloop()

