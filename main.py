'''
Versao: Beta 1.0! 
Criado: Liedosnrm'''

name = "Liedson"
a = 0
frasecalculo = "Digite o calculo: "
ajuda = "Funções do bot:\n   Saudações -'oi' ou 'ola'\n   Frases motivacioanis - 'motivacao'\n   Contar piada - 'me conte uma piada'\n   Contas simples - 'quero fazer um calculo'\n   Ajuda - veja essa tabela\n  Sair - digite 'exit'     "

class Bot():
    def __init__(self, name, ajuda):
        self.name = name
        self.ajuda = ajuda

    def pegar(self):
        self.entradas = input("-> ").lower().split()

    def resposta(self):
        if self.entradas[0] == "ola" or self.entradas[0] == "oi":
            print(f"Ola {self.name}, como vai você?")

        elif self.entradas[0] == 'exit':
            exit()

        elif self.entradas[0] == 'help':
            print("help")
        
        elif self.entradas[0] == 'bem' or self.entradas[0] == 'bom':
            print("Que bom!! O que você deseja?")

        elif len(self.entradas) >= 4:
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

        else:
            print("Não entendi, repita, por favor.")


while True:
    bot = Bot(name, ajuda)
    bot.pegar()
    bot.resposta()
