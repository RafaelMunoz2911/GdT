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

#___________ menu
img_contratos = Image.open('event.png')
img_contratos = img_contratos.resize((18,18))
img_contratos = ImageTk.PhotoImage(img_contratos)
b_usuario = Button(frameEsquerda, image=img_contratos, compound=LEFT, anchor=NW, text=' Cadastrar um novo evento', bg= co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=10)

img_ativ = Image.open('task.png')
img_ativ = img_ativ.resize((18,18))
img_ativ = ImageTk.PhotoImage(img_ativ)
b_usuario = Button(frameEsquerda, image=img_ativ, compound=LEFT, anchor=NW, text=' Cadastrar nova atividade', bg= co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_usuario.grid(row=1, column=0, sticky=NSEW, padx=5, pady=10)

img_terc = Image.open('terc.png')
img_terc = img_terc.resize((18,18))
img_terc = ImageTk.PhotoImage(img_terc)
b_usuario = Button(frameEsquerda, image=img_terc, compound=LEFT, anchor=NW, text=' Cadastrar novo funcionario', bg= co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_usuario.grid(row=2, column=0, sticky=NSEW, padx=5, pady=10)

img_ver_terc = Image.open('verTerc.png')
img_ver_terc = img_ver_terc.resize((18,18))
img_ver_terc = ImageTk.PhotoImage(img_ver_terc)
b_usuario = Button(frameEsquerda, image=img_ver_terc, compound=LEFT, anchor=NW, text=' Ver tos funcionários ', bg= co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_usuario.grid(row=3, column=0, sticky=NSEW, padx=5, pady=10)

img_presencas = Image.open('presen.png')
img_presencas = img_presencas.resize((18,18))
img_presencas = ImageTk.PhotoImage(img_presencas)
b_usuario = Button(frameEsquerda, image=img_presencas, compound=LEFT, anchor=NW, text=' Gerar lista de presença', bg= co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_usuario.grid(row=4, column=0, sticky=NSEW, padx=5, pady=10)

img_pagamentos = Image.open('pag.png')
img_pagamentos = img_pagamentos.resize((18,18))
img_pagamentos = ImageTk.PhotoImage(img_pagamentos)
b_usuario = Button(frameEsquerda, image=img_pagamentos, compound=LEFT, anchor=NW, text=' Registro de pagamentos', bg= co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_usuario.grid(row=5, column=0, sticky=NSEW, padx=5, pady=10)

janela.mainloop()