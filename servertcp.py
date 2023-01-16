from socket import *

serverName='DESKTOP-U0O0BE1'
serverPort = 12012
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")
while 1:
      connectionSocket, addr = serverSocket.accept()
      sentence = connectionSocket.recv(1024).decode()

      file-open(sentence,"r")
      l=file.read(1024)

      connectionSocket.send(l.encode())
      file.close()
      connectionSocket.close()
