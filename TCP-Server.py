#Topic          :       TCP服务器
#File Name      :       TCP-Server.py
#Author         :       Jack Cui
#Created        :       23 April 2016

import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9997

#create an object of socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#bind the socket to the local IP and port 
server.bind((bind_ip,bind_port))
#listening for connections
server.listen(5)
#print informations of IP and port 
print("[*] Listening on %s:%d" % (bind_ip,bind_port))

#process client thread
def handle_client(client_socket):
#print the data which is form client
    request = client_socket.recv(1024)
    print("[*] Received: %s" % request)
#send data pack to client
    client_socket.send("ACK!")
#close the socket after transfer is completed
    client_socket.close()
    
while True:
#save the information of client when the connection is established
    client,addr = server.accept()
#print client detail  
    print("[*] Accepted connection from: %s:%d" % (addr[0],addr[1]))
#create a new tread to process client
    client_handler = threading.Thread(target = handle_client,args =(client,))
#start the thread
    client_handler.start()
    
    


