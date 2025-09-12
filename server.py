from socket  import *
from constCS import *
import pickle

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))
s.listen(1)
(conn, addr) = s.accept()
print(f"Conectado a {addr}")

while True:
  msg = conn.recv(1024)
  if not msg:
    break
  
  try:
    data = pickle.loads(msg)
    
    if "OP" in data and "STR" in data:
      op = data["OP"]
      string_recebida = data["STR"]
      
      if op == "upper":
        res = string_recebida.upper()
        status = "OK"
      elif op == "lower":
        res = string_recebida.lower()
        status = "OK"
      elif op == "invert":
        res = string_recebida[::-1]
        status = "OK"
      else:
        status = "NOK"
        res = "Operação inválida"
    else:
      status = "NOK"
      res = "Formato de dados inválido."
      
    data_resposta = {"STATUS": status, "RES": res}
    msg_resposta = pickle.dumps(data_resposta)
    conn.send(msg_resposta)
    
  except (pickle.UnpicklingError, IndexError):
    status = "NOK"
    res = "Erro ao processar a mensagem."
    data_resposta = {"STATUS": status, "RES": res}
    msg_resposta = pickle.dumps(data_resposta)
    conn.send(msg_resposta)

conn.close()         # close the connection
