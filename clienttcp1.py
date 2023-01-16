from socket import *

serverName='DESKTOP-U0O0BE1'
serverPort=12012
clientSocket=socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input("Enter file name")
clientSocket.send(sentence.encode())
filecontents = clientSocket.recv(1024).decode()
print ("From Server:",filecontents)
clientSocket.close()
