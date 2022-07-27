import os
from Funcoes import get_ip,scanner
import threading

meu_ip = (get_ip())
rede = meu_ip[:meu_ip.rfind(".")+1]
clientes = []
threads = []

lock = threading.Lock()

for item in range(1,255):
    teste = rede + str(item)
    t = threading.Thread(target=scanner,args =(teste,clientes,lock,))
    t.start()
    threads.append(t)

for thread in threads:
        thread.join()

print(clientes)


2º modo:
    
    import os



for k in range(1, 254):

    ip = "192.168.0.7.{0}".format(k)
response = os.popen(f"ping {ip} -c 1").read()
if "Host Unreachable" in response:
    print( ip, ": inativo")
else:
        print(ip, ": ativo")
