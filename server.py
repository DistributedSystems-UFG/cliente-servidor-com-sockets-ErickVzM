from socket  import *
from constCS import * #-
import pickle

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
  msg = conn.recv(1024)    # receive data from client
  if not msg: break        # stop if client stopped 
  print(msg)
  data = pickle.loads(msg)
  print(data)
  if data["OP"] == "sum":
    res = data["V1"] + data["V2"]
    status = "OK"
  elif data["OP"] == "sub":
    res = data["V1"] - data["V2"]
    status = "OK"
  else:
    status = "NOK"
    res = 1
  data = {"STATUS":status, "RES":res}
  msg = pickle.dumps(data)
  conn.send(msg)
  
conn.close()               # close the connection
