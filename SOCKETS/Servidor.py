from socket import *

servidor = socket(AF_INET, SOCK_STREAM)
servidor.bind(("0.0.0.0", 1234))
servidor.listen(5)

# Servidor aceita as conexoes
cliente,endereco = servidor.accept()
print(f'Bem Vindo {endereco} ')


# colocar a conexão em um loop while

while True:
    #recebendo dados de forma binaria
        dados= cliente.recv(2048).decode()
        print(f'Recebido do Cliente: {dados}')
        if dados == "sair":
            cliente.close()
            break

        cliente.sendall('Obrigado'.encode())

# fechar servidor
servidor.close()









