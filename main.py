'''
Versao: Beta 1.0! 
Criado: Liedosnrm'''
import wikipedia


a = 0
frasecalculo = "Digite o calculo: "
ajuda = "Funções do bot:\n   Saudações -'oi' ou 'ola'\n   Contas simples - 'quero fazer um calculo'\n   Pesquisar na wikipedia - 'wikipedia'\n   Ajuda - veja essa tabela\n   Sair - digite 'exit'     \n"

class Bot():
    
    def __init__(self, name, ajuda):
        self.name = name
        self.ajuda = ajuda

    def pegar(self):
        self.entradas = input("-> ").lower().split()

    def wiki_research(self):
        wikipedia.set_lang('pt')
        assunto = str(input("O que você deseja pesquisar? "))
    
        try:
            wiki = wikipedia.page(assunto)
    
        except:
            retorno = input('Resultado não encontrado!\nDeseja fazer outras pesquisa?(s/n) ')
            if retorno == 's':
                self.wiki_research()

            else:
                pass

        else:
            print(wiki.title+"\n__________________________________________________________________________________________________________________________________________________\n" +wiki.summary+"\n__________________________________________________________________________________________________________________________________________________")


    def calculo(self):
        
        for palavra in self.entradas:
        
                if palavra == 'calculo':
                    tipo = input('Digite o tipo de calculo:\n--Mutiplicacao = x\n--Divisao = /\n--Subtracao = -\n--Soma = +\n-> ')
        
                    if tipo == 'soma':
                        calculo = input(frasecalculo + "\n>>> ").split('+')
                        print(int(calculo[0]) + int(calculo[1]))
                    
                    elif tipo == 'mutiplicacao':
                        calculo = input(frasecalculo + "\n>>>").split('x')
                        print(int(calculo[0]) * int(calculo[1]))
                    
                    elif tipo == "divisao":
                        calculo = input(frasecalculo + "\n>>>").split('/')
                        print(int(calculo[0]) / int(calculo[1]))
                    
                    elif tipo == "subtracao":
                        calculo = input(frasecalculo + "\n>>>").split('-')
                        print(int(calculo[0]) - int(calculo[1]))
                   
                    else:
                        print("Error: Tente novamente digitando 'Calculadora'")   

    def resposta(self):
        if self.entradas[0] == "ola" or self.entradas[0] == "oi":
            print(f"Ola {self.name}, como vai você?")


        elif self.entradas[0] == 'wikipedia':
            self.wiki_research()


        elif self.entradas[0] == 'exit':
            exit()

        elif self.entradas[0] == 'help':
            print("help")
        
        elif self.entradas[0] == 'bem' or self.entradas[0] == 'bom':
            print("Que bom!! O que você deseja?")

        elif len(self.entradas) >= 4:
            self.calculo()

        else:
            print("Não entendi, repita, por favor.")


try:
    with open('dados.txt', 'r') as dados:
        da = dados.read()
        name = da

except:
    with open('dados.txt', 'a') as dados:
        name = input("Seja bem vindo, qual é seu nome? ")
        dados.write(name)

while True:
    if a == 0:
        a += 1
        print(ajuda)
    bot = Bot(name, ajuda)
    bot.pegar()
    bot.resposta()
