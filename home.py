import cv2
import imutils
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
import entrenarModelo as eM
import demodularColeccion as dC
import demodularImagen as dI

class Home:

    def __init__(self, master):

        self.master = master
        self.master.title("Home")
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        window_width = 960
        window_height = 720
        x_coordinate = (screen_width/2) - (window_width/2)
        y_coordinate = (screen_height/2) - (window_height/2)
        self.master.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))
        self.master.resizable(False, False)
        self.master.configure(bg = 'white')

        # Header
        espacio = tk.Label(self.master, text = '', fg = 'black', font = ('arial', 25), width = 5, height = 1, bg = 'white')
        espacio.pack()
        titulo_home = tk.Label(self.master, text = 'Runner', fg = 'black', font = ('arial', 35), width = 30, height = 1, bg = 'white')
        titulo_home.pack()
        espacio2 = tk.Label(self.master, text = '', fg = 'black', font = ('arial', 25), width = 5, height = 1, bg = 'white')
        espacio2.pack()
        subtitulo_home = tk.Label(self.master, text = 'Demodulación de imágenes multipolarizadas en fotoelasticidad digital', fg = 'black', font = ('arial', 24), width = 70, height = 1, bg = 'white')
        subtitulo_home.pack()

        # Imagen UNAL
        unal = cv2.imread('Logo_UNAL.png')
        unal = imutils.resize(unal, height = 210, width = 210)
        unal = ImageTk.PhotoImage(image = Image.fromarray(cv2.cvtColor(unal, cv2.COLOR_BGR2RGB)))
        unal_label = tk.Label(self.master, image = unal, borderwidth = 0)
        unal_label.image = unal
        unal_label.place(x = 740, y = 8)

        #Configurando imágenes iniciales
        # Imagen Esquema multipolarizado
        imagen = Image.open('Esquema_multipolarizado.png')
        imagen = imutils.resize(np.array(imagen), height = 371, width = 618)
        imagen = ImageTk.PhotoImage(image = Image.fromarray(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)))
        imagen_esquema = tk.Label(self.master, image = imagen, borderwidth = 0)
        imagen_esquema.image = imagen
        imagen_esquema.place(x = 310, y = 190)

        #Botones de la Home page

        titulo_actividad = tk.Label(self.master, text = '¿Qué deseas hacer?', fg = 'red', font = ('arial', 16), width = 24, height = 1, bg = 'white', anchor = 'center')
        titulo_actividad.place(x = 50, y = 220)

        btn_entrenar_modelo = tk.Button(self.master, text = 'Entrenar modelo', command = self.open_entrenar_modelo, fg = 'black', font = ('arial', 14), bg = 'white', width = 24, highlightbackground = 'white')
        btn_entrenar_modelo.place(x = 50, y = 290)
        btn_entrenar_modelo.config(state = 'disabled')

        btn_demodular_coleccion = tk.Button(self.master, text = 'Demodular colección', command = self.open_demodular_coleccion, fg = 'black', font = ('arial', 14), bg = 'white', width = 24, highlightbackground = 'white')
        btn_demodular_coleccion.place(x = 50, y = 370)
        btn_demodular_coleccion.config(state = 'disabled')

        btn_demodular_imagen = tk.Button(self.master, text = 'Demodular imagen', command = self.open_demodular_imagen, fg = 'black', font = ('arial', 14), bg = 'white', width = 24, highlightbackground = 'white')
        btn_demodular_imagen.place(x = 50, y = 450)

        btn_salir = tk.Button(self.master, text = 'Salir', command = self.master.destroy, fg = 'black', font = ('arial', 16), bg = 'white', width = 10, highlightbackground = 'white')
        btn_salir.place(x = 810, y = 650)

        ## Autores
        titlo_autores = tk.Label(self.master, text = 'Desarrollado por:', fg = 'black', font = ('arial', 14), width = 20, height = 1, bg = 'white', anchor = 'w')
        titlo_autores.place(x = 15, y = 600)
        autor1 = tk.Label(self.master, text = 'Diego Eusse-Naranjo', fg = 'black', font = ('arial', 14), width = 20, height = 1, bg = 'white', anchor = 'w')
        autor1.place(x = 37, y = 620)
        autor2 = tk.Label(self.master, text = 'Alejandro Restrepo-Martínez', fg = 'black', font = ('arial', 14), height = 1, bg = 'white', anchor = 'w')
        autor2.place(x = 37, y = 640)
    
    def open_entrenar_modelo(self):
        self.master.destroy()
        entrenarModelo = tk.Tk()
        eM.EntrenarModelo(entrenarModelo)
        entrenarModelo.mainloop()
    
    def open_demodular_imagen(self):
        self.master.destroy()
        demodularImagen = tk.Tk()
        dI.DemodularImagen(demodularImagen)
        demodularImagen.mainloop()

    def open_demodular_coleccion(self):
        self.master.destroy()
        demodularColeccion = tk.Tk()
        dC.DemodularColeccion(demodularColeccion)
        demodularColeccion.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    Home(root)
    root.mainloop()