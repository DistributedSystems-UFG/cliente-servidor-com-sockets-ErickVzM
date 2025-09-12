from socket  import *
from constCS import *
import pickle

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
print("Conectado ao servidor.")

while True:
  string_para_enviar = input("Digite a string (ou 'sair' para encerrar): ")
  if string_para_enviar.lower() == 'sair':
      break
      
  print("\nEscolha uma opção:")
  print("upper - converter para maiúsculas")
  print("lower - converter para minúsculas")
  print("invert - inverter a string")
  
  op = input("Digite a operação: ")
  
  data = {"OP": op, "STR": string_para_enviar}
  msg = pickle.dumps(data)

  s.send(msg)
  
  try:
    msg_resposta = s.recv(1024)
    data_resposta = pickle.loads(msg_resposta)
    
    if data_resposta["STATUS"] == "OK":
      print("Resultado: ", data_resposta["RES"])
    elif data_resposta["STATUS"] == "NOK":
      print("Erro: ", data_resposta["RES"])
    else:
      print("Resposta inesperada do servidor.")
      
  except (pickle.UnpicklingError, IndexError):
    print("Erro ao receber a resposta do servidor.")

s.close()
