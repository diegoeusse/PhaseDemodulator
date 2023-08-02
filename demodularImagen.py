import cv2
import imutils
import numpy as np
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog
import subprocess as sp
from PIL import Image, ImageTk
from keras.models import load_model, Model
import matplotlib.pyplot as plt
import home as hm
import entrenarModelo as eM
import demodularColeccion as dC
from FuncionesCosto.Perera import tv_loss_plus_var_loss

class DemodularImagen:

    def __init__(self, master):

        self.master = master
        self.master.title("Demodular imagen")
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
        
        # Selector del modelo
        arquitecturas = sp.getoutput("ls 'Modelos/'").split('\n')
        
        texto_selector = tk.Label(self.master, text = 'Selecciona un modelo: ', fg = 'black', font = ('arial', 16), width = 24, height = 1, bg = 'white', anchor = 'w')
        texto_selector.place(x = 40, y = 180)

        selector = ttk.Combobox(self.master, values = arquitecturas)
        selector.config(width = 30)
        selector.set(arquitecturas[0])
        selector.place(x = 250, y = 180)

        def cargar_modelo():
            selected = selector.get()
            output.delete(1.0, tk.END)
            global modelo
            url = 'Modelos/' + selected

            if ('Model8' in selected):
                custom_objects = {'tv_loss_plus_var_loss': tv_loss_plus_var_loss}
                modelo = load_model(url, custom_objects=custom_objects)
            else:
                modelo = load_model(url)

            if selected == "":
                output.insert(tk.END, "No ha seleccionado nada, modelo cargado: " + arquitecturas[0] + "\n")
            else:
                output.insert(tk.END, "Ha cargado: " + selected + "\n")

        BotonCargarModelo = tk.Button(self.master, text = "Cargar modelo", command = cargar_modelo, fg = 'black', width = 20, font = ('arial', 16), bg = 'white', highlightbackground = 'white')
        BotonCargarModelo.place(x = 600, y = 180)

        output = tk.Text(self.master, height=1, fg = 'black', font = ('arial', 12), bg = 'white', highlightbackground = 'white')
        output.place(x = 550, y = 210)

        # Imagen a comparar
        texto_imagen_comparar = tk.Label(self.master, text = 'Cuentas con una imagen para comparar: ', fg = 'black', font = ('arial', 16), height = 1, bg = 'white', anchor = 'w')
        texto_imagen_comparar.place(x = 40, y = 230)

        BotonSi = tk.Button(self.master, text = "Sí", fg = 'black', font = ('arial', 16), bg = 'white', highlightbackground = 'white')
        BotonSi.place(x = 370, y = 230)

        BotonNo = tk.Button(self.master, text = "No", fg = 'black', font = ('arial', 16), bg = 'white', highlightbackground = 'white')
        BotonNo.place(x = 450, y = 230)

        def button_click(event):
            try:
                btn_carga_gt.place_forget()
                self.master.update()
            except:
                pass

            btn_carga_original.place(x = 120, y = 310)

            btn_correr.place(x = 630, y = 310)
            btn_correr.config(state = 'disabled')

            if event.widget["text"] == "Sí":
                btn_carga_gt.place(x = 375, y = 310)
                btn_carga_gt.config(state = 'disabled')              
                
        BotonSi.bind("<Button-1>", button_click)
        BotonNo.bind("<Button-1>", button_click)

        def Boton_Cargue():
            global ruta_original
            global imagen_original
            global img_original
            ruta_original = tkinter.filedialog.askopenfilename(filetypes = [('Archivos NPY','.npy')])
            img_original = np.load(ruta_original)

            # Crea un canvas en la ventana tkinter y establece su tamaño
            canvas = tk.Canvas(self.master, width=img_original.shape[1], height=img_original.shape[0], borderwidth=0, bg='white', highlightbackground='white')
            canvas.place(x = 60, y = 370)

            # Muestra la imagen en el canvas utilizando Matplotlib
            plt.figure(figsize=(img_original.shape[1]/85, img_original.shape[0]/85))
            plt.imshow(img_original)
            plt.axis("off")
            plt.title("Imagen de entrada")
            plt.savefig("temp.png", bbox_inches="tight")

            # Carga la imagen desde el archivo temporal como una imagen tkinter
            imagen_original = tk.PhotoImage(file="temp.png")
            canvas.create_image(0, 0, image=imagen_original, anchor=tk.NW)

            btn_correr.config(state = 'normal')
            btn_carga_gt.config(state = 'normal')
            
        def Boton_Cargue_gt():
            global ruta_gt
            global imagen_gt
            global img_original
            ruta_gt = tk.filedialog.askopenfilename(filetypes = [('Archivo de texto','.txt')])
            img_gt = np.loadtxt(ruta_gt)
            img_gt = img_gt.reshape((256,256,1))

            # Crea un canvas en la ventana tkinter y establece su tamaño
            canvas_gt = tk.Canvas(self.master, width=img_gt.shape[1], height=img_gt.shape[0], borderwidth=0, bg='white', highlightbackground='white')
            canvas_gt.place(x = 360, y = 370)

            # Muestra la imagen en el canvas utilizando Matplotlib
            plt.figure(figsize=(img_gt.shape[1]/85, img_gt.shape[0]/85))
            plt.imshow(img_gt, cmap = 'gray')
            plt.axis("off")
            plt.title("Ground truth")
            plt.savefig("temp_gt.png", bbox_inches="tight")

            # Carga la imagen desde el archivo temporal como una imagen tkinter
            imagen_gt = tk.PhotoImage(file="temp_gt.png")
            canvas_gt.create_image(0, 0, image=imagen_gt, anchor=tk.NW)


        #Botón de ejecución de algoritmo
        def Boton_Correr():
            global img_pred
            global imagen_pred
            img_original_expand = np.expand_dims(img_original, axis=0)

            img_pred = modelo.predict(img_original_expand)
            img_pred = np.reshape(img_pred, (256, 256,1))

            # Crea un canvas en la ventana tkinter y establece su tamaño
            canvas_pred = tk.Canvas(self.master, width=img_pred.shape[1], height=img_pred.shape[0], borderwidth=0, bg='white', highlightbackground='white')
            canvas_pred.place(x = 660, y = 370)

            # Muestra la imagen en el canvas utilizando Matplotlib
            plt.figure(figsize=(img_pred.shape[1]/85, img_pred.shape[0]/85))
            plt.imshow(img_pred, cmap = 'gray')
            plt.axis("off")
            plt.title("Predicción")
            plt.savefig("temp_pred.png", bbox_inches="tight")

            # Carga la imagen desde el archivo temporal como una imagen tkinter
            imagen_pred = tk.PhotoImage(file="temp_pred.png")
            canvas_pred.create_image(0, 0, image=imagen_pred, anchor=tk.NW)


        #Botones F4
        btn_carga_original = tk.Button(self.master, text = 'Carga imagen de entrada', command = Boton_Cargue, fg = 'black', font = ('arial', 14), bg = 'white', width = 24, highlightbackground = 'white')

        btn_correr = tk.Button(self.master, text = 'Demodular', command = Boton_Correr, fg = 'black', font = ('arial', 14), bg = 'white', width = 24, highlightbackground = 'white')

        btn_carga_gt = tk.Button(self.master, text = 'Carga ground truth', command = Boton_Cargue_gt, fg = 'black', font = ('arial', 14), bg = 'white', width = 24, highlightbackground = 'white')
        
        self.master_btn = tk.Button(self.master, text = 'Regresar al Home', command = self.open_home, fg = 'black', width = 20, font = ('arial', 16), bg = 'white', highlightbackground = 'white')
        self.master_btn.place(x = 680, y = 680)

    def open_home(self):
        self.master.destroy()
        home = tk.Tk()
        hm.Home(home)
        home.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    DemodularImagen(root)
    root.mainloop()