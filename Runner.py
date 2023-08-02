# Librerías generales
import tkinter
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import matplotlib.pyplot as plt #Para graficar
import tkinter.filedialog
import numpy as np # Para cálculo de matrices
import imutils
from keras.preprocessing import image
from keras.models import Model, load_model
import subprocess as sp


#  --------------------------------------------------------------------- FRONT -------------------------------------------------------------------------------------

def show_frame(frame):
    frame.tkraise()

#Creando ventana
root = tkinter.Tk()           # Inicializa una ventana nueva
root.title('Runner')       # Título de la ventana
root.geometry('960x720') 

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

f1 = tkinter.Frame(root)
f2 = tkinter.Frame(root)
f3 = tkinter.Frame(root)
f4 = tkinter.Frame(root)

for frame in (f1, f2, f3, f4):
    frame.grid(row=0,column=0,sticky='nsew')

# ======================================================================= Frame 1 code =======================================================================
#Configurando mensaje superior
f1.configure(bg = 'white')
Espacio = tkinter.Label(f1, text = '', fg = 'black', font = ('arial', 25), width = 5, height = 1, bg = 'white')
Espacio.pack()
Etiqueta_Sup = tkinter.Label(f1, text = 'Runner', fg = 'black', font = ('arial', 35), width = 30, height = 1, bg = 'white')
Etiqueta_Sup.pack()
Espacio = tkinter.Label(f1, text = '', fg = 'black', font = ('arial', 25), width = 5, height = 1, bg = 'white')
Espacio.pack()
Etiqueta_Dos = tkinter.Label(f1, text = 'Demodulación de imágenes multipolarizadas en fotoelasticidad digital', fg = 'black', font = ('arial', 24), width = 70, height = 1, bg = 'white')
Etiqueta_Dos.pack()

#Configurando imágenes iniciales
Archivo1 = Image.open('Esquema_multipolarizado.png')#Imagen Esquema multipolarizado
Imagen1 = ImageTk.PhotoImage(Archivo1)
Lienzo_1 = tkinter.Label(f1, image = Imagen1, borderwidth = 0).place(x = 310, y = 190)

UNAL = cv2.imread('Logo_UNAL.png')
UNAL = imutils.resize(UNAL, height = 210)
UNAL = imutils.resize(UNAL, width = 210)
UNAL = cv2.cvtColor(UNAL, cv2.COLOR_BGR2RGB)
im = Image.fromarray(UNAL)
Imagen_UNAL = ImageTk.PhotoImage(image = im)
Lienzo_2 = tkinter.Label(f1, image = Imagen_UNAL, borderwidth = 0).place(x = 740, y = 8)

#Botones de la f1

Etiqueta_A1 = tkinter.Label(f1, text = '¿Qué deseas hacer?', fg = 'red', font = ('arial', 16), width = 24, height = 1, bg = 'white', anchor = 'center')
Etiqueta_A1.place(x = 50, y = 220)

btn = tkinter.Button(f1, text = 'Entrenar modelo', command = lambda: show_frame(f2), fg = 'black', font = ('arial', 14), bg = 'white', width = 24, highlightbackground = 'white')
btn.place(x = 50, y = 290)
btn.config(state = 'disabled')

btn2 = tkinter.Button(f1, text = 'Demodular colección', command = lambda: show_frame(f3), fg = 'black', font = ('arial', 14), bg = 'white', width = 24, highlightbackground = 'white')
btn2.place(x = 50, y = 370)
btn2.config(state = 'disabled')

btn3 = tkinter.Button(f1, text = 'Demodular imagen', command = lambda: show_frame(f4), fg = 'black', font = ('arial', 14), bg = 'white', width = 24, highlightbackground = 'white')
btn3.place(x = 50, y = 450)

btn4 = tkinter.Button(f1, text = 'Salir', command = root.destroy, fg = 'black', font = ('arial', 16), bg = 'white', width = 10, highlightbackground = 'white')
btn4.place(x = 810, y = 650)

## Autores
Etiqueta_A1 = tkinter.Label(f1, text = 'Desarrollado por:', fg = 'black', font = ('arial', 14), width = 20, height = 1, bg = 'white', anchor = 'w')
Etiqueta_A1.place(x = 15, y = 600)
Etiqueta_A2 = tkinter.Label(f1, text = 'Diego Eusse-Naranjo', fg = 'black', font = ('arial', 14), width = 20, height = 1, bg = 'white', anchor = 'w')
Etiqueta_A2.place(x = 37, y = 620)
Etiqueta_A3 = tkinter.Label(f1, text = 'Alejandro Restrepo-Martínez', fg = 'black', font = ('arial', 14), height = 1, bg = 'white', anchor = 'w')
Etiqueta_A3.place(x = 37, y = 640)

# ======================================================================= Frame 2 code =======================================================================
#Configurando mensaje superior
f2.configure(bg = 'white')
f2_title = tkinter.Label(f2, text='Page 2', font='times 35', bg='blue')
f2_title.pack(fill='both', expand=True)

f2_btn = tkinter.Button(f2, text='Enter',command=lambda:show_frame(f3))
f2_btn.pack(fill='x', ipady=15)

# ======================================================================= Frame 3 code =======================================================================
#Configurando mensaje superior
f3.configure(bg = 'white')
f3_title = tkinter.Label(f3, text='Page 3', font='times 35', bg='red')
f3_title.pack(fill='both', expand=True)

f3_btn = tkinter.Button(f3, text='Enter',command=lambda:show_frame(f4))
f3_btn.pack(fill='x', ipady=15)

# ======================================================================= Frame 4 code =======================================================================
#Configurando mensaje superior
f4.configure(bg = 'white')
Espacio = tkinter.Label(f4, text = '', fg = 'black', font = ('arial', 25), width = 5, height = 1, bg = 'white')
Espacio.pack()
Etiqueta_Sup = tkinter.Label(f4, text = 'Runner', fg = 'black', font = ('arial', 35), width = 30, height = 1, bg = 'white')
Etiqueta_Sup.pack()
Espacio = tkinter.Label(f4, text = '', fg = 'black', font = ('arial', 25), width = 5, height = 1, bg = 'white')
Espacio.pack()
Etiqueta_Dos = tkinter.Label(f4, text = 'Demodulación de imágenes multipolarizadas en fotoelasticidad digital', fg = 'black', font = ('arial', 24), width = 70, height = 1, bg = 'white')
Etiqueta_Dos.pack()

# Configurando imágenes iniciales
Lienzo = tkinter.Label(f4, image = Imagen_UNAL, borderwidth = 0).place(x = 740, y = 8)

arquitecturas = sp.getoutput("ls 'Modelos/'").split('\n')
# Selección del modelo
Etiqueta_A1 = tkinter.Label(f4, text = 'Selecciona un modelo: ', fg = 'black', font = ('arial', 16), width = 24, height = 1, bg = 'white', anchor = 'w')
Etiqueta_A1.place(x = 40, y = 180)

def cargar_modelo():
    selected = combo.get()
    output.delete(1.0, tkinter.END)
    global modelo
    url = 'Modelos/' + selected
    modelo = load_model(url)
    BotonCargarModelo.config(state = 'disabled')

    if selected == "":
        output.insert(tkinter.END, "No ha seleccionado nada, modelo cargado: " + arquitecturas[0] + "\n")
    else:
        output.insert(tkinter.END, "Ha cargado: " + selected + "\n")

combo = ttk.Combobox(f4, values = arquitecturas)
combo.config(width = 30)
combo.set(arquitecturas[0])
combo.place(x = 250, y = 180)

BotonCargarModelo = tkinter.Button(f4, text = "Cargar modelo", command = cargar_modelo, fg = 'black', width = 20, font = ('arial', 16), bg = 'white', highlightbackground = 'white')
BotonCargarModelo.place(x = 600, y = 180)

output = tkinter.Text(f4, height=1, fg = 'black', font = ('arial', 12), bg = 'white', highlightbackground = 'white')
output.place(x = 550, y = 210)

# Imagen a comparar
Etiqueta_A1 = tkinter.Label(f4, text = 'Cuentas con una imagen para comparar: ', fg = 'black', font = ('arial', 16), height = 1, bg = 'white', anchor = 'w')
Etiqueta_A1.place(x = 40, y = 230)

#Botón de búsqueda de imagen de entrada

ArchivoW=Image.open('Waiting.bmp') #Imagen temporal de espera
ImagenW = ImageTk.PhotoImage(ArchivoW)

def button_click(event):

    def Boton_Cargue():
        global Ruta
        global Input
        global Imagen
        Ruta = tkinter.filedialog.askopenfilename(filetypes = [('Archivos NPY','.npy')])
        Archivo = Image.open(Ruta)
        Imagen = ImageTk.PhotoImage(image = Archivo)
        Input = cv2.imdecode(np.fromfile(Ruta, dtype = np.uint8), cv2.IMREAD_UNCHANGED)
        Input2 = imutils.resize(Input, height = 224)
        ImageToShow = imutils.resize(Input2, width = 224)
        ImageToShow = cv2.cvtColor(ImageToShow, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(ImageToShow )
        Imagen = ImageTk.PhotoImage(image=im)
        tkinter.Label(f4,image = Imagen).place(x = 120, y = 350)
        tkinter.Label(f4,image = ImagenW).place(x = 630, y = 350)
        btn_correr.config(state = 'normal')
        btn_carga.config(state = 'disabled')
    
    def Boton_Cargue_gt():
        global Ruta_gt
        global Input_gt
        global Imagen_gt
        Ruta_gt = tkinter.filedialog.askopenfilename(filetypes = [('Archivo de texto','.txt')])
        Archivo = Image.open(Ruta)
        Imagen = ImageTk.PhotoImage(image = Archivo)
        Input = cv2.imdecode(np.fromfile(Ruta, dtype = np.uint8), cv2.IMREAD_UNCHANGED)
        Input2 = imutils.resize(Input, height = 224)
        ImageToShow = imutils.resize(Input2, width = 224)
        ImageToShow = cv2.cvtColor(ImageToShow, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(ImageToShow )
        Imagen = ImageTk.PhotoImage(image=im)
        tkinter.Label(f4,image = Imagen).place(x = 120, y = 350)
        tkinter.Label(f4,image = ImagenW).place(x = 630, y = 350)
        btn_correr.config(state = 'normal')
        btn_carga.config(state = 'disabled')

    #Botón de ejecución de algoritmo
    def Boton_Correr():
        global Ruta
        global Input
        global resultado
        image_list = np.zeros((1,256, 256, 4))
        img = image.load_img(Ruta, target_size = (256, 256, 4))
        x = image.img_to_array(img).astype('float32')
        x = x / 255.0
        image_list[0] = x
        preds = modelo.predict(image_list)
        preds_0 = preds[0]* 255.0
        resultado = preds_0.reshape(224, 224)
        im = Image.fromarray(resultado)
        btn3.config(state = 'normal')
        btn2.config(state = 'disabled')
        Imagen = ImageTk.PhotoImage(image=im)
        Lienzo_2=tkinter.Label(f4,image=Imagen).place(x=630,y=350)
        Lienzo_2.pack()


    btn_carga = tkinter.Button(f4, text = 'Carga imagen de entrada', command = Boton_Cargue, fg = 'black', font = ('arial', 12),bg = 'gray',width = 24)
    btn_carga.place(x = 120, y = 310)
    btn_carga_gt = tkinter.Button(f4, text = 'Carga ground truth', command = Boton_Cargue_gt, fg = 'black', font = ('arial', 12),bg = 'gray',width = 24)
    btn_correr = tkinter.Button(f4, text = 'Demodular', command = Boton_Correr, fg = 'black', font = ('arial', 12),bg = 'gray',width = 24)

    if event.widget["text"] == "Sí":
        btn_carga_gt.place(x = 375, y = 310)
        btn_carga_gt.config(state = 'disabled')

        btn_correr.place(x = 630, y = 310)
        btn_correr.config(state = 'disabled')

    elif event.widget["text"] == "No":
        btn_correr.place(x = 375, y = 310)
        btn_correr.config(state = 'disabled')

        btn_carga_gt.place_forget()

    f4.update()


BotonSi = tkinter.Button(f4, text = "Sí", fg = 'black', font = ('arial', 16), bg = 'white', highlightbackground = 'white')
BotonSi.place(x = 370, y = 230)

BotonNo = tkinter.Button(f4, text = "No", fg = 'black', font = ('arial', 16), bg = 'white', highlightbackground = 'white')
BotonNo.place(x = 450, y = 230)

BotonSi.bind("<Button-1>", button_click)
BotonNo.bind("<Button-1>", button_click)

#Botones F4
f4_btn = tkinter.Button(f4, text = 'Regresar al Home', command = lambda: show_frame(f1), fg = 'black', width = 20, font = ('arial', 16), bg = 'white', highlightbackground = 'white')
f4_btn.place(x = 680, y = 650)


show_frame(f1)
root.mainloop()
