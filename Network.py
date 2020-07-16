import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.43.195"
        self.port = 9999
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode("utf-8")
        except:
            return "Error in connecting"

    def p_num(self):
        return self.p

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

    def send_object(self, obj):
        try:
            self.client.send(pickle.dumps(obj))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)