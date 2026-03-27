import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from shared.encryptor import Encryptor

import socket
import threading


class Server:
    def __init__(self, host, port):
        KEY = "7f026d24873b44fad78c46955d44fea914112f4edb7ba1159b1ce78a784e5959"
        self.encryptor = Encryptor(KEY)
        self.host = host
        self.port = port
        
    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.host, self.port))
        s.listen()
        print("Server listening on port ", self.port)  
        while True:
            conn, addr = s.accept() # blocks until a client connects
            print("Client connected from ", addr)
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()

    def handle_client(self, conn, addr):
        while True:
            data = conn.recv(1024)
            if not data:
                break
            decrypted = self.encryptor.decrypt(data.decode())
            print(f"Received data from {addr}: {decrypted}")

        conn.close()
        print("Client disconnected from ", addr)
    
        
              
        
        
        

        

        