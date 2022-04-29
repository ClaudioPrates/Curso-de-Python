

class Pessoa(object):
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
            print(f"Meu nome é {self.nome} e tenho {self.idade} anos.")


    def __str__(self):
        return (f"Meu nome é {self.nome} e tenho {self.idade} anos.")

    def __call__(self, *args, **kwargs):
        print('Isso é realmente importante!')

    def __del__(self):
        print('Terminamos o nosso trabalho')



p1 = Pessoa("Cláudio",36)
p1.mostrar_dados()
print(p1)
p1()







