import random
import time
import keyboard
#Victor Miguel
class Bingo:
    def __init__(self):
        self.jog1_lista = [] 
        self.jog2_lista = []  
        self.list_contagem = []  

    def gerar_cartela(self):
        "Gera uma cartela de bingo sem repetir números dentro da mesma cartela."
        cartela = []
        numeros_usados = set()

        for _ in range(2):
            linha = []
            while len(linha) < 3:  
                num = random.randint(1, 30)  
                if num not in numeros_usados: 
                    linha.append(num)
                    numeros_usados.add(num)  
            cartela.append(linha)
        
        return cartela

    def start(self):
        "Inicia o jogo e define as cartelas."
        print("Indique o modo de Jogo:\n 0 - RÁPIDO \n 1 - DEMORADO")
        try:
            escolha = int(input("Escolha: "))
            if escolha == 0:
                self.rapido()
            elif escolha == 1:
                self.demorado()
            else:
                print("Número inválido, tente novamente.\n")
                self.start()
        except ValueError:
            print("Erro: Digite um número válido.\n")
            self.start()

    def rapido(self):
        "Configura e exibe as cartelas dos jogadores no modo rápido."
        self.jog1_lista = self.gerar_cartela()
        self.jog2_lista = self.gerar_cartela()

        print("\nJogador 1:")
        for linha in self.jog1_lista:
            print(linha)

        print("\n---------------------\n")
        print("Jogador 2:")
        for linha in self.jog2_lista:
            print(linha)
        
        self.run()

    def demorado(self):
        print("Modo Demorado ainda não implementado.")

    def run(self):
        "Sorteia números e marca os que forem encontrados nas cartelas."
        while True:
            escolha_pc = random.randint(1, 30)
            if escolha_pc not in self.list_contagem:  
                self.list_contagem.append(escolha_pc)

                time.sleep(1)
                print(f"\n=> Última dezena sorteada: {escolha_pc}")
                print("Dezenas Sorteadas até o momento:", ' '.join(map(str, self.list_contagem)))

                self.marcar_numero(self.jog1_lista, escolha_pc, "Jogador 1")
                self.marcar_numero(self.jog2_lista, escolha_pc, "Jogador 2")

                print("\nJogador 1:")
                for linha in self.jog1_lista:
                    print(linha)

                print("\n---------------------\n")
                print("Jogador 2:")
                for linha in self.jog2_lista:
                    print(linha)
                print("Pressione Enter para continuar")
                keyboard.wait("enter")

    def marcar_numero(self, cartela, numero, jogador):
        "Marca o número sorteado dentro da cartela colocando parênteses ao redor."
        for i in range(len(cartela)):
            for j in range(len(cartela[i])):
                if cartela[i][j] == numero:
                    cartela[i][j] = f"({numero})"
                    if self.verificar_vitoria(cartela, jogador):
                        return True
        return False

    def verificar_vitoria(self, cartela, jogador):
        "Verifica se o jogador completou a cartela."
        acertos = sum([1 for linha in cartela for num in linha if isinstance(num, str) and num.startswith('(')])
        if acertos == 6 or acertos == 12:
            print(f"{jogador} ganhou \o/")
            print(self.jog1_lista)
            quit('Obrigado por Jogar!')
        return False

if __name__ == '__main__':
    jogo = Bingo()
    jogo.start()

