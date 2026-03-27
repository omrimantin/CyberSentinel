import socket
from shared.encryptor import Encryptor
from shared.protocol import Protocol

class Agent:
    def __init__(self, host, port):
        KEY = "7f026d24873b44fad78c46955d44fea914112f4edb7ba1159b1ce78a784e5959"
        self.encryptor = Encryptor(KEY)
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send_alert(self, alert_type, details_dict):
        packed = Protocol.pack(alert_type, details_dict)
        encrypted = self.encryptor.encrypt(packed)
        self.sock.send(encrypted.encode())

        
        