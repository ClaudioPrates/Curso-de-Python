from socket import *

cliente = socket(AF_INET,SOCK_STREAM)
cliente.connect(("192.168.0.2",4444))


while True:
    # Cliente envia os dados para o Servidor
    dados = input('Cliente:')
    cliente.sendall(dados.encode())

    if dados == "sair":
        cliente.close()
        break


    # Cliente recebe os dados do Servidor
    dados = cliente.recv(2048).decode()
    print(f'Servidor {dados}')





