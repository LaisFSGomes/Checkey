from tkinter import *
import requests
import json
import datetime
#from Tela02_Sobre import *
chave = 0
inform = ' '
pesquisa = ' '
class Janela:
    def __init__(self, master=None):
        self.janela = Tk() #Definição e construção da Janela Inicial
        self.primeiroContainer = Frame(master)
        self.janela.title("Checkey")
        self.janela["background"] = "orange"
        self.janela.geometry("600x500+350+100")  #Define as dimensões da nossa Janela Inicial, tais medidas serâo replicadas para as demais janelas

        self.lb = Label(
        self.janela, text="PROJETO DE ENG.SOFTWARE", bg = "orange", fg='#2B0A37') #Definindo o primeiro campo de texto
        self.lb["font"]=("Arial", "18", "bold")
        self.lb.place(x=115, y=80)  #Define a posição do elemento na janela

        self.lb9 = Label(
        self.janela, text = "CHECKEY", bg = "orange", fg='#2B0A37')
        self.lb9["font"] = ("Arial", "20", "bold")
        self.lb9.place(x=220, y=120)  # Define a posição do elemento na janela


        self.bt1 = Button(
        self.janela,text = "Autenticar", bg = "purple", fg= 'white', height= 1) #Definindo o primeiro botão
        self.bt1["font"] = ("Arial", "12","bold")
        self.bt1["width"] = 9
        self.bt1["command"] = self.lb1_click  #Chama a função que será responsavel por verificar a autenticidade da chave e em seguida depois de validade abrirá a Tela de busca
        self.bt1.place(x=380, y=225)

        self.bt2 = Button(
        self.janela,text = "Sobre", bg = "purple", fg= 'white', height= 1) #Definindo o segundo botão, responsável por abrir a janela com as informações sobre a ferramenta
        self.bt2["font"] = ("Arial", "12","bold")
        self.bt2["width"] = 10
        self.bt2["command"] = self.Sobre #Chama a função que após o click abrirá a janela com as informações
        self.bt2.place(x=100, y=400)

        self.bt3 = Button(
        self.janela,text = "Dúvidas", bg = "purple", fg= 'white', height= 1) #Definindo o terceiro botão, responsável por abrir a janela tira duvidas
        self.bt3["font"] = ("Arial", "12","bold")
        self.bt3["width"] = 10
        self.bt3["command"] = self.Duvidas #Responsável por abrir a janela tira duvidas após a mesma ter sido clicada
        self.bt3.place(x=400, y=400)

        self.ent = Entry(
        self.janela, font= "Arial", width= 25)  #Criando e definindo o nosso primeiro campo de entrada de dados
        self.ent.place(x=140, y=230)
        self.ent.insert(0, 'AIzaSyD8GC7dfcNtPCKOes-HepvWdKgF8RiaLf4')


        self.mensagem = Label(
        self.janela,text ="", font= "Arial", bg="orange", fg='white')
        self.mensagem.place(x= 170, y=260)

    def Sobre(self):
        self.sobre = Sobre()
        self.janela.destroy()  #Destroi a janela anterior quando a atual for requisitada através do click

    def Duvidas(self):
        self.duvidas = Duvidas()
        self.janela.destroy()

    def lb1_click(self):           #Será responsável por validar o acesso da chave
        global chave
        chave = self.ent.get()
        testeChave = requests.get('https://factchecktools.googleapis.com/v1alpha1/claims:search?query='+'test'+'&key='+chave)
        status = testeChave.status_code
        if status >= 200 and status <= 226:
            self.mensagem["text"] = "Autenticado"
            win = Check(self)
            self.janela.destroy()
        else:
            self.mensagem["text"] = "Desculpe, mas houve um erro!\nVerifique sua conecção com a internet ou sua chave"
            self.ent.delete(0,END)


#Classe Sobre, referente a nossa segunda janela
class Sobre:
    def __init__(self, master=None):
        self.janela02 = Tk()
        self.janela02.title("Sobre ")
        self.janela02["background"] = "orange"
        self.janela02.geometry("600x500+350+100")

        self.lb2 = Label(
        self.janela02, text="Sobre a ferramenta Checkey", width=30, height=2, bg ="orange")
        self.lb2["font"] = ("Arial", "14", "bold")
        self.lb2.place(x=100, y=50)

        self.lb3 = Label(
        self.janela02,text="Checkey é uma ferramenta de verificação de veracidade de informações\ndesenvolvido por alguns estudantes da disciplina de Engenharia de\nSoftware.\n\nCréditos:\nDesenvolvedores: Alice Sousa, Lais Gomes\nIntermediador: Daniel Alves\nMarkertin: Maxela Martins\n\n", bg="white", fg= 'purple')
        self.lb3["width"]=60
        self.lb3["height"] =10
        self.lb3["font"] = ("Arial", "12")
        self.lb3.place(x=30, y=100)



        self.bt4 = Button(
        self.janela02, text="Voltar", width="8", height="1", bg="purple")
        self.bt4["font"] = ("Arial", "12", "bold")
        self.bt4.place(x=100, y=400)
        self.bt4["command"] = self.voltar

    def voltar(self):
        self.voltar = Janela()
        self.janela02.destroy()



#Classe dúvidas referente a nossa terceira janela
class Duvidas:
    def __init__(self, master=None):
        self.janela03 = Tk()
        self.janela03.title("Duvidas")
        self.janela03["background"]= "orange"
        self.janela03.geometry("600x500+350+100")

        self.lb4 = Label(
        self.janela03, text="Como adquirir a Chave", width=30, height=2, bg ="orange")
        self.lb4["font"] = ("Arial", "14", "bold")
        self.lb4.place(x=100, y=100)

        self.lb5 = Label(
        self.janela03,text="Como o software foi criado com uma API do Google,\npara criar uma chave você precisa de uma conta no Google Cloud.", bg="white", fg= 'purple')
        self.lb5["width"]=60
        self.lb5["height"] = 10
        self.lb5["font"] = ("Arial", "12")
        self.lb5.place(x=30, y=150)

        self.scrollbar = Scrollbar(self.janela03)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.mylist = Listbox(self.janela03, yscrollcommand=self.scrollbar.set)
        self.mylist.insert(END, "AIzaSyD8GC7dfcNtPCKOes-HepvWdKgF8RiaLf4")


        self.bt5 = Button(
        self.janela03, text="Voltar", width="8", height="1", bg="purple")
        self.bt5["font"] = ("Arial", "12", "bold")
        self.bt5.place(x=400, y=400)
        self.bt5["command"] = self.voltar

    def voltar(self):
        self.voltar = Janela()
        self.janela03.destroy()

#Classe de chegagem, referente a nossa quarta janela
class Check:
    def __init__(self, master=None):
        self.janela04 = Tk()
        self.janela04.title("Check")
        self.janela04["background"]= "orange"
        self.janela04.geometry("600x500+350+100")

        self.lb6 = Label(
        self.janela04, text="Digite o assunto que você deseja que a CHECKEY analise:", bg = "orange")
        self.lb6["font"]=("Arial", "12", "bold")
        self.lb6.place(x=80, y=80)

        self.bt6 = Button(
        self.janela04,text = "Check", bg = "purple", fg= 'white', height= 1)
        self.bt6["font"] = ("Arial", "12","bold")
        self.bt6["width"] = 9
        self.bt6.place(x=380, y=240)
        self.bt6["command"] = self.verificar

        self.bt7 = Button(
        self.janela04, text="Reincerir Chave", width="15", height="1", bg="purple", fg= 'white')
        self.bt7["font"] = ("Arial", "12", "bold")
        self.bt7.place(x=400, y=400)
        self.bt7["command"] = self.voltar

        self.ent = Entry(
        self.janela04, font="Arial", width=30)
        self.ent.place(x=100, y=245)


    def voltar(self):
        self.voltar = Janela()
        self.janela04.destroy()

    def verificar (self):
        global chave
        global pesquisa
        pesquisa = self.ent.get()
        requisicao = requests.get('https://factchecktools.googleapis.com/v1alpha1/claims:search?query='+pesquisa+'&key='+chave)
        global inform
        inform = json.loads(requisicao.text)       #se der certo, retorna isso
        win = Info(self)
        self.janela04.destroy()

class Info:
    def __init__(self, master=None):
        self.janela05 = Tk()
        self.janela05.protocol("WM_DELETE_WINDOW", self.on_close)
        self.janela05.title("Informações ")
        self.janela05["background"] = "orange"
        self.janela05.geometry("600x500+350+100")

        self.lb8 = Label(
        self.janela05, text="Fatos checados:", width=15, height=3, bg ="orange")
        self.lb8["font"] = ("Arial", "15", "bold")
        self.lb8.place(x=20, y=18)

        self.bt9 = Button(
        self.janela05, text="Voltar", width="8", height="1", bg="purple", fg='white')
        self.bt9["font"] = ("Arial", "12", "bold")
        self.bt9.place(x=440, y=440)
        self.bt9["command"] = self.voltar

        self.scrollbar = Scrollbar(self.janela05)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.mylist = Listbox(self.janela05, yscrollcommand=self.scrollbar.set)
        self.verificarfato()

        self.mylist["width"]=300
        self.mylist["height"]= 35
        self.mylist.pack(padx=50, pady=70,side=LEFT, fill=BOTH)
        self.scrollbar.config(command=self.mylist.yview)

    def voltar(self):
            self.voltar = Check()
            self.janela05.destroy()

    def verificarfato(self):
        try:
            informacoes = inform['claims']
            # informacoes é uma lista
            for elem in informacoes:
                # elem sao dicionarios)
                for elemenkey in elem.items():
                    if elemenkey[0] == 'text':
                        texto = elemenkey[1]
                        self.mylist.insert(END,"TEXTO: ", texto)
                    elif elemenkey[0] == 'claimant':
                        requeredor = elemenkey[1]
                        self.mylist.insert(END, "REQUEREDOR: ", requeredor)
                    elif elemenkey[0] == 'claimDate':
                        DataReclamacao = elemenkey[1]
                        date_format = "%Y-%m-%dT%H:%M:%SZ"
                        dt = datetime.datetime.strptime(DataReclamacao, date_format)
                        self.mylist.insert(END, "DATA DA RECLAMAÇÃO: ", dt)
                    elif elemenkey[0] == 'claimReview':
                        for elemkeysdicts in elemenkey[1]:
                            for dici in elemkeysdicts.items():
                                if dici[0] == 'url':
                                    fonte = dici[1]
                                    self.mylist.insert(END, "Fonte: ", fonte)
                                elif dici[0] == 'title':
                                    titulo = dici[1]
                                    self.mylist.insert(END, "Revisão: ", titulo)

                                elif dici[0] == 'reviewDate':
                                    DataRevisao = dici[1]
                                    date_format = "%Y-%m-%dT%H:%M:%SZ"
                                    dt = datetime.datetime.strptime(DataReclamacao, date_format)
                                    self.mylist.insert(END, "Data de Revisão: ", dt)
                                elif dici[0] == 'textualRating':
                                    veracidade = dici[1]
                                    self.mylist.insert(END, "Veracidade: ", veracidade)
                print('\n')
                self.mylist.insert(END, '----------------------------------------------------------------------')
        except Exception as erro:
            global pesquisa
            self.mylist.insert(END, 'a sua pesquisa', pesquisa, 'ainda não foi vericada pela Fact Checker Tools API')

    def on_close(self):
        self.janela05.destroy()
        root.destroy()

root = Tk()

root.withdraw()
Janela(root)

root.mainloop()
