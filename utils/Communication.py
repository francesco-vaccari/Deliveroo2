import time
import socket
import threading
from utils.Logger import ExperimentLogger

class Communication:
    def __init__(self, folder, HOST, PORT, SERVER_PORT = None):
        self.logger = ExperimentLogger(folder, 'communication.log')
        self.HOST = HOST
        self.PORT = PORT
        self.SERVER_PORT = SERVER_PORT
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((HOST, PORT))
        self.is_open = True
        self.buffer = []

        self.server_thread = threading.Thread(target=self.server_listen, args=())
        self.server_thread.start()
    
    def receive(self):
        if self.is_open:
            data, addr = self.server_socket.recvfrom(8192)
            self.logger.log_info(f"[{self.PORT}] Received message from {addr}: {data.decode('utf-8')}")
            return data.decode('utf-8'), addr
        else:
            return None, None
    
    def send_to_server(self, data):
        if self.is_open and self.SERVER_PORT is not None:
            try:
                self.server_socket.sendto(data.encode('utf-8'), (self.HOST, self.SERVER_PORT))
                self.logger.log_info(f"[{self.PORT}] Sent message to {self.HOST}:{self.SERVER_PORT}: {data}")
            except Exception as e:
                print(e)
    
    def send_to_agent(self, data, port, id):
        if self.is_open:
            try:
                self.server_socket.sendto(data.encode('utf-8'), (self.HOST, port))
                self.logger.log_info(f"[{self.PORT}] Sent message to agent (ID:{id}) {self.HOST}:{port}: {data}")
            except Exception as e:
                print(e)
    
    def close(self):
        self.logger.log_debug(f"[{self.PORT}] Closing connection on {self.HOST}:{self.PORT}")
        self.server_socket.sendto("exit".encode('utf-8'), (self.HOST, self.PORT))

    def server_listen(self):
        self.logger.log_debug(f"[{self.PORT}] Started listening on {self.HOST}:{self.PORT}")
        while self.is_open:
            msg, addr = self.receive()
            if msg == "exit":
                self.is_open = False
                self.server_socket.close()
                self.logger.log_debug(f"[{self.PORT}] Connection closed")
            self.buffer.append((msg, addr))

