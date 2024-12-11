from tkinter .ttk import *
from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

from tkinter import messagebox

#_-_- importando as funcoes da view

from view import *


#____ cores 
co0 = "#2e2d2b"
co1 = "#feffff"
co2 = "#4fa882"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "#3fbfb9"
co6 = "#263238"
co7 = "#e9edf5"
co8 = "#6e8faf"
co9 = "#f2f4f2"

#------ fontes

font1 = ('Verdana 15 bold')
font2 = ('Ivy 10')
fontLinha =('Verdanda 1')


#------ criando a janela 
janela = Tk()
janela.title("")
janela.geometry('770x330')
janela.configure(background=co1)
janela.resizable(False, False)

style = Style(janela)
style.theme_use("clam")

#------- manipulando frames

frameCima = Frame(janela, width=770, height=50, bg=co2, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameEsquerda = Frame(janela, width=150, height=265, bg=co4, relief="solid")
frameEsquerda.grid(row=1, column=0, sticky=NSEW)

frameDireita = Frame(janela, width=600, height=265, bg=co1, relief="raised")
frameDireita.grid(row=1, column=1, sticky=NSEW) 

#_____ logo
#__________ abrindo a imagem 

app_img = Image.open('hotel.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=1000, compound=LEFT, pady=5, anchor=NW,bg=co2, fg=co1)
app_logo.place(x=5, y=0)

app_ = Label(frameCima, text="Gestão de Terceiros", font=('Verdana 15 bold'), compound=LEFT, pady=5, anchor=NW, bg=co2, fg=co1)
app_.place(x=50, y=7)

app_linha = Label(frameCima, width=770, height=1, padx=5, anchor=NW, font=('Verdanda 1'), bg=co3, fg=co1)
app_linha.place(x=0, y=47)

janela.mainloop()