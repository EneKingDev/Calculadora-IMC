import tkinter as tk
from tkinter import ttk

import sv_ttk

ventana = tk.Tk()
ventana.title("Calculo IMC V0.1")
ventana.geometry("280x265")
ventana.resizable(0,0)

icono = tk.PhotoImage(file = "imc.png")
ventana.iconphoto(True, icono)

etiqueta = ttk.Label(ventana, text = "Calculo IMC")
etiqueta.grid(column = 1, row = 0)

lblEspacioBlanco1 = ttk.Label(ventana, text = "  ")
lblEspacioBlanco1.grid(column = 1, row = 1)

lblEspacioBlanco2 = ttk.Label(ventana, text = "  ")
lblEspacioBlanco2.grid(column = 1, row = 2)
#etiqueta.pack(fill = tk.X)


def calculoIMC():
    peso = float(txtPeso.get())
    altura = float(txtAltura.get())
    IMC = peso / altura ** 2
    IMC = round(IMC, 1)
    clasificacion = " "

    if IMC >= 0 and IMC < 18.5:
        clasificacion = "Bajo peso"
    elif IMC >= 18.5 and IMC <= 24.9:
        clasificacion = "Adecuado"
    elif IMC >= 25.0 and IMC <= 29.9:
        clasificacion = "Sobrepeso"
    elif IMC >= 30.0 and IMC <= 34.9:
        clasificacion = "Obesidad grado 1"
    elif IMC >= 35.0 and IMC <= 39.9:
        clasificacion = "Obesidad grado 2"
    elif IMC >= 40.0:
        clasificacion = "Obesidad grado 2"

    resLbl["text"] =   "Tu IMC es de:"  
    resImc["text"] = IMC
    resClas["text"] = clasificacion

lblPeso = ttk.Label(ventana, text = "Ingresa tu peso (Kg)")
lblPeso.grid(column = 1, row = 3)

txtPeso = ttk.Entry(ventana, font = "Helvetica 10")
txtPeso.grid(column = 1, row = 4)
#txtPeso.pack()

lblEspacioBlanco4 = ttk.Label(ventana, text = "               ")
lblEspacioBlanco4.grid(column = 0, row = 5)

lblAltura = ttk.Label(ventana, text = "Ingresa tu altura (Mt)")
lblAltura.grid(column = 1, row = 6)

txtAltura = ttk.Entry(ventana, font = "Helvetica 10")
txtAltura.grid(column = 1, row = 7)
#txtAltura.pack()

lblEspacioBlanco3 = ttk.Label(ventana, text = "  ")
lblEspacioBlanco3.grid(column = 1, row = 8)

btnCalcular = ttk.Button(ventana, text = "Calcular", command = calculoIMC)
btnCalcular.grid(column = 1, row = 9)
#btnCalcular.pack()

resLbl = tk.Label(ventana)
resLbl.grid(column = 1, row = 10)
#resImc.pack()

resImc = tk.Label(ventana)
resImc.grid(column = 1, row = 11)
#resImc.pack()

resClas = tk.Label(ventana)
resClas.grid(column = 1, row = 12)
#resClas.pack()

lblEspacioBlanco5 = ttk.Label(ventana, text = "               ")
lblEspacioBlanco5.grid(column = 0, row = 2)

sv_ttk.set_theme("dark")

ventana.mainloop()
