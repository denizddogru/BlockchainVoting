# TO-DO LIST


import socket
import threading
import sys
import time
from random import randint
import gui


class Server:
    connections = []
    peers = []
    
    def __init__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('0.0.0.0', 8080))
        sock.listen(5)
        print("Server running...")
        print("**** WELCOME TO THE E-VOTING SYSTEM ****")
        print("Please login to vote!")

        gui.main_screen()

        while True:
            c, a = sock.accept()
            cThread = threading.Thread(target=self.handler, args=(c, a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            self.peers.append(a[0])
            print("USER: ",str(a[0]) + ':' + str(a[1]), " connected.")
            print(len(self.peers)+1,"online user(s) now!")
            self.send_peers()

    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                connection.send(data)                
                
            if not data:
                print("USER: ",str(a[0]) + ':' + str(a[1]), " disconnected.")
                self.connections.remove(c)
                self.peers.remove(a[0])
                print(len(self.peers)+1,"online user(s) left now!")
                c.close()
                self.send_peers()                
                break           

    def send_peers(self):
        p = ""
        for peer in self.peers:
            p = p + peer + ","
         

        for connection in self.connections:
            connection.send(b'\x11' + bytes(p, 'utf-8'))   

class Client:
    list1 =[]    
    def send_msg(self, sock):
        while True:
            sock.send(bytes(input(""), 'utf-8'))      

            
    def __init__(self, address):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect((address, 8080))

        iThread = threading.Thread(target=self.send_msg, args=(sock,))
        iThread.daemon = True
        iThread.start()
        
        print("Please login to vote!")
        gui.main_screen()

        while True:
            data = sock.recv(1024)           
            
            if not data:
                break
            if data[0:1] == b'\x11':
                self.update_peers(data[1:])
            else:                           
                print(str(data, 'utf-8'))
                 

    def update_peers(self, peer_data):
        p2p.peers = str(peer_data, 'utf-8').split(",")[:-1]
        
class p2p:
    peers = ['127.0.0.1']

while True:
    try:
        print("Trying to connect to the E-VOTING SYSTEM...")                
        for peer in p2p.peers:
            try:
                client = Client(peer)  
                                          
            except KeyboardInterrupt:
                sys.exit(0)
            except:
                try:
                    server = Server()
                              
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    print("Couldn't start the server...")
    except KeyboardInterrupt:
        sys.exit(0)
