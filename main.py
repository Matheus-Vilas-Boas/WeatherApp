import tkinter
from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image
import requests
import datetime
from datetime import datetime
import time
import pytz
import json
import pycountry_convert as pc

black = "#444466"
white = "#feffff"
blue = "#6f9fbd"

fundoDia = "#6cc4cc"
fundoNoite = "#484f60"
fundoTarde = "#bfb86d"

fundo = fundoDia

window = Tk()
window.title('Weather App')
window.geometry('350x350')

window.configure(bg=fundo)

ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

mainFrame = Frame(window, width=350, height=50, bg=white,pady=0,padx=0,)
mainFrame.grid(row=1, column=0)

frameFrame = Frame(window, width=350, height=300,bg=fundo, pady=12, padx=0,)
frameFrame.grid(row=2, column=0, sticky=NW)
style = ttk.Style(window)
style.theme_use("clam")

def info():
    key = 'd480270a23934caae59d14e5165533a1'
    
    cidade = eLocal.get()

    apiLink = (f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key}')

    request = requests.get(apiLink)

    dados = request.json()

    codPais = dados['sys'] ['country']

    fusoHorarioZona = pytz.country_timezones[codPais]

    pais = pytz.country_names[codPais]

    zona = pytz.timezone(fusoHorarioZona[0])
    print(dados)
    
    fusoHorario = datetime.now(zona)

    fusoHorario = fusoHorario.strftime("%d %m %Y | %H:%M:%S %p")


    tempo = dados['main']['temp']
    pressaoAtmosferica = dados['main']['pressure']
    Umidade = dados['main']['humidity']
    velocidadeDoVento = dados['wind']['speed']
    detalhe = dados['weather'][0]['description']

    def countryTocontinent(i):
        country_alpha2 = pc.country_name_to_country_alpha2(i)
        country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
        return country_continent_name
    
    continente = countryTocontinent(pais)
    
    city['text'] = cidade + " - " + pais +" / "+ continente
    
    data['text'] = fusoHorario
    
    pressao['text'] = "Pressão : "+ str(pressaoAtmosferica)
    
    umidade['text'] = Umidade
    simbolo['text'] = "%"
    nomeUmidade['text'] = "Umidade"
    
    velocidadeVento['text'] = "velocidade do vento : "+ str(velocidadeDoVento)
    
    detalhes['text'] = detalhe
    

    
    zona_priodo = datetime.now(zona)
    zona_priodo = zona_priodo.strftime("%H")
    
    
    global imagem
    
    zona_priodo = int(zona_priodo)
    if zona_priodo <= 5:
        imagem = Image.open('imagens/moon-nigth.png')
        fundo = fundoNoite
    elif zona_priodo <= 11:
        imagem = Image.open('imagens/sun.png')
        fundo = fundoDia
    elif zona_priodo <= 17:
        imagem = Image.open('imagens/sun.png')
        fundo = fundoTarde
    elif zona_priodo <= 23:
        imagem = Image.open('imagens/moon-nigth.png')
        fundo= fundoNoite
    else: 
        pass  
    
    
    imagem = imagem.resize((120, 120), Image.ANTIALIAS)
    imagem = ImageTk.PhotoImage(imagem)
    l_icon1 = Label(frameFrame,image=imagem, compound=LEFT,  bg=fundo, fg="white",font=('Ivy 10 bold'), anchor="nw", relief=FLAT)
    l_icon1.place(x=190, y=50)
    
    # -- Mudando cor do fundo
    
    window.configure(bg=fundo)
    frameFrame.configure(bg=fundo)
    mainFrame.configure(bg=fundo)
    
    city['bg'] = fundo
    data['bg'] = fundo
    pressao['bg'] = fundo
    umidade['bg'] = fundo
    simbolo['bg'] =fundo
    nomeUmidade['bg'] = fundo
    velocidadeVento['bg'] = fundo
    detalhes['bg'] = fundo

eLocal = Entry(mainFrame, width=20, justify='left', font=('', 14), highlightthickness=1, relief='solid')
eLocal.place(x=15, y=10)
verify = Button(mainFrame,command=info,text='Ver cilma',bg=white,fg='black', font=('Calibri 9'), relief='raised',overrelief=RIDGE)
verify.place(x=250, y=10)

city = Label(frameFrame, text="", height=1, padx=0, relief="flat", anchor="center",fg=white, font=('Arial 10 '))
city.place(x=10, y=4)

data = Label(frameFrame, text='', anchor='center', bg = fundo, fg = white, font=("Arial 10"))
data.place(x=10, y=54)
      
umidade = Label(frameFrame, text='', anchor='center', bg = fundo, fg = white, font=("Arial 45"))
umidade.place(x=-5, y=100)
       
simbolo = Label(frameFrame, text='', anchor='center', bg = fundo, fg = white, font=("Arial 15 bold"))
simbolo.place(x=79, y=110)
   
nomeUmidade = Label(frameFrame, text="", height=1, padx=0, relief="flat",fg=white, anchor="center", font=('Arial 10 '))
nomeUmidade.place(x=75, y=137)
 
pressao = Label(frameFrame, text="", height=1, padx=0, relief="flat",fg=white, anchor="center", font=('Arial 10 '))
pressao.place(x=10, y=170)

velocidadeVento = Label(frameFrame, text="", height=1,fg=white, padx=0, relief="flat", anchor="center", font=('Arial 10 '))
velocidadeVento.place(x=10, y=200)

detalhes = Label(frameFrame,text="", height=1, padx=0,fg=white, relief="flat", anchor="center", font=('Arial 10 '))
detalhes.place(x=230, y=200)



window.mainloop()