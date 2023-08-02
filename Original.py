# Librerías generales
import tkinter
import cv2
from PIL import Image, ImageTk
import matplotlib.pyplot as plt #Para graficar
import tkinter.filedialog
import numpy as np # Para cálculo de matrices
import imutils
from keras.preprocessing import image

Input = None

#Boton de búsqueda de imagen de entrada
def Boton_Cargue():
	global Ruta
	global Input
	global Imagen
	Ruta = tkinter.filedialog.askopenfilename(filetypes=[('image','.bmp'),('image','.jpg'),('image','.png'),('image','.jpeg')])
	Archivo=Image.open(Ruta)
	Imagen=ImageTk.PhotoImage(image=Archivo)
	Input = cv2.imdecode(np.fromfile(Ruta, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
	Input2= imutils.resize(Input, height=224)
	ImageToShow= imutils.resize(Input2, width=224)
	ImageToShow = cv2.cvtColor(ImageToShow, cv2.COLOR_BGR2RGB)
	im = Image.fromarray(ImageToShow )
	Imagen = ImageTk.PhotoImage(image=im)
	Lienzo_1 = tkinter.Label(Interfaz,image=Imagen).place(x = 120,y = 350)
	Lienzo_2 = tkinter.Label(Interfaz,image=ImagenW).place(x = 630,y = 350)
	btn2.config(state = 'normal')
	btn.config(state = 'disabled')

#Boton de ejecucion de algoritmo
def Boton_correr():
	global Ruta
	global Input
	global resultado

	image_list = np.zeros((1,224, 224, 3))
	img = image.load_img(Ruta, target_size=(224, 224,3))
	x = image.img_to_array(img).astype('float32')
	x = x / 255.0
	image_list[0] = x
	preds = MODEL.predict(image_list)
	preds_0 = preds[0]* 255.0
	resultado = preds_0.reshape(224, 224)
	im = Image.fromarray(resultado)
	btn3.config(state = 'normal')
	btn2.config(state = 'disabled')
	Imagen = ImageTk.PhotoImage(image=im)
	Lienzo_2 = tkinter.Label(Interfaz,image=Imagen).place(x = 630,y = 350)
	Lienzo_2.pack()

#Funcion para guardar resultado
def Guardar():
	global Ruta
	global Result
	global resultado
	cv2.imwrite('Resultado.bmp',resultado)
	btn.config(state = 'normal')
	btn3.config(state = 'disabled')

## Cargar el modelo CNN
def Boton_modelo():
	from keras.models import Model
	from keras.models import load_model

	global MODEL
	MODEL = load_model('./model.h5')
	btn.config(state = 'normal')
	btn5.config(state = 'disabled')

#Boton de salida
def Boton_cerrar():
	Interfaz.destroy()


#  --------------------------------------------------------------------- FRONT -------------------------------------------------------------------------------------

#Creando ventana
Interfaz = tkinter.Tk()           # Inicializa una ventana nueva
Interfaz.title('Runner')       # Título de la ventana
Interfaz.geometry('960x720')      # Tamaño de la ventana
Interfaz.configure(bg = 'white')

#Configurando mensaje superior
Espacio = tkinter.Label(Interfaz, text = '', fg = 'black', font = ('arial', 25), width = 5, height = 1, bg = 'white')
Espacio.pack()
Etiqueta_Sup = tkinter.Label(Interfaz, text = 'Runner', fg = 'black', font = ('arial', 35), width = 30, height = 1, bg = 'white')
Etiqueta_Sup.pack()
Espacio = tkinter.Label(Interfaz, text = '', fg = 'black', font = ('arial', 25), width = 5, height = 1, bg = 'white')
Espacio.pack()
Etiqueta_Dos = tkinter.Label(Interfaz, text = 'Demodulacion de imágenes multipolarizadas en fotoelasticidad digital', fg = 'black', font = ('arial', 24), width = 70, height = 1, bg = 'white')
Etiqueta_Dos.pack()

#Configurando imágenes iniciales
Archivo1 = Image.open('Esquema_multipolarizado.png')#Imagen Esquema multipolarizado
Imagen1 = ImageTk.PhotoImage(Archivo1)
Lienzo_1 = tkinter.Label(Interfaz, image = Imagen1).place(x = 310, y = 190)

UNAL = cv2.imread('Logo_UNAL.png')
UNAL = imutils.resize(UNAL, height = 210)
UNAL = imutils.resize(UNAL, width = 210)
UNAL = cv2.cvtColor(UNAL, cv2.COLOR_BGR2RGB)
im = Image.fromarray(UNAL)
Imagen_UNAL = ImageTk.PhotoImage(image = im)
Lienzo_2 = tkinter.Label(Interfaz, image = Imagen_UNAL, borderwidth = 0).place(x = 740, y = 8)

#Botones de la interfaz

Etiqueta_A1 = tkinter.Label(Interfaz, text = '¿Qué deseas hacer?', fg = 'red', font = ('arial', 16), width = 24, height = 1, bg = 'white', anchor = 'center')
Etiqueta_A1.pack()
Etiqueta_A1.place(x = 50, y = 220)

btn = tkinter.Button(Interfaz, text = 'Entrenar modelo', command = Boton_modelo, fg = 'black', font = ('arial', 14), bg = 'gray', width = 24)
btn.place(x = 50, y = 290)
btn.config(state = 'disabled')

btn2 = tkinter.Button(Interfaz, text = 'Demodular colección', command = Boton_correr, fg = 'black', font = ('arial', 14), bg = 'gray', width = 24)
btn2.place(x = 50, y = 370)
btn2.config(state = 'disabled')

btn3 = tkinter.Button(Interfaz, text = 'Demodular imagen', command = Guardar, fg = 'black', font = ('arial', 14), bg = 'gray', width = 24)
btn3.place(x = 50, y = 450)
btn3.config(state = 'disabled')

btn4 = tkinter.Button(Interfaz, text = 'Salir', command = Boton_cerrar, fg = 'black', font = ('arial', 16), bg = 'gray', width = 10)
btn4.place(x = 810, y = 650)

## Autores
Etiqueta_A1 = tkinter.Label(Interfaz, text = 'Desarrollado por:', fg = 'black', font = ('arial', 12), width = 20, height = 1, bg = 'white', anchor = 'w')
Etiqueta_A1.pack()
Etiqueta_A1.place(x = 15, y = 600)
Etiqueta_A2 = tkinter.Label(Interfaz, text = 'Diego Eusse-Naranjo', fg = 'black', font = ('arial', 11), width = 20, height = 1, bg = 'white', anchor = 'w')
Etiqueta_A2.pack()
Etiqueta_A2.place(x = 37, y = 620)
Etiqueta_A3 = tkinter.Label(Interfaz, text = 'Alejandro Restrepo-Martínez', fg = 'black', font = ('arial', 11), width = 20, height = 1, bg = 'white', anchor = 'w')
Etiqueta_A3.pack()
Etiqueta_A3.place(x = 37, y = 640)

Interfaz.mainloop()
