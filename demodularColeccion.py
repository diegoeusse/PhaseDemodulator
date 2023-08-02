import tkinter as tk

class DemodularColeccion:

    def __init__(self, master):

        self.master = master
        self.master.title("Demodular coleccion")
        self.master.geometry('960x720')
        self.master.resizable(False, False)
        
        self.label = tk.Label(self.master, text="This is the second window.")
        self.label.pack()