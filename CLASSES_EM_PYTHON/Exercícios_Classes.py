import random



class adivinhaONumero(object):
    contador = 0

    def __init__(self):
        adivinhaONumero.contador +=1
        self.numero = random.randint(1,1000)
        self.tentativas = 0

    def __call__(self, *args, **kwargs):
        numero =  kwargs ["numero"]
        if numero > self.numero:
            print("Seu numero eh maior")
            self.tentativas = 0
            return False


        elif numero < self.numero:
            print("Seu numero eh menor")
            self.tentativas +=1
            return False

        else:
            return True

while True:

    numero = int(input("[+] Digite um numero de 1 a 1000: (digite -1 para sairdo jogo)"))
    if numero == -1:
        break

    jogo = adivinhaONumero()

    while not jogo(numero=numero):
        numero = int(input("[+] Digite um numero de 1 a 1000: (digite -1 para sair do jogo)"))
    else:
        print(f"Você acertou em {jogo.tentativas} tentativas")
print(f"jogo encerrado em {jogo.contador}")





