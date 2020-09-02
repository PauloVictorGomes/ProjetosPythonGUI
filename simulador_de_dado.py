# Simulador de dado
# Simula o uso de um dado, gerando um valor de 1 até 6
import random
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor?'
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'), sg.Button('não')]
        ]

    def Iniciar(self):
        # criar uma janela
        self.janela = sg.Window('Simulador de Dado',layout = self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # fazer alguma coisa com esse valores
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValordoDado()
            elif self.eventos == 'não' or self.eventos == 'n':
                print('OK! Volte sempre.')
            else:
                print('Por Favor digitar sim ou não.')
        except:
                print('Ocorreu um erro ao receber sua respostass')

    def GerarValordoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()
