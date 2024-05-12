import socket
import threading

class Communication:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((HOST, PORT))
        self.is_open = True
        self.buffer = []

        self.server_thread = threading.Thread(target=self.server_listen, args=())
        self.server_thread.start()
    
    def receive(self):
        data, addr = self.server_socket.recvfrom(1024)
        return data.decode('utf-8'), addr
    
    def send(self, data, addr):
        self.server_socket.sendto(data.encode('utf-8'), addr)

    def close(self):
        self.server_socket.close()
        print("Server socket closed.")

    def server_listen(self):
        while self.is_open:
            msg, addr = self.receive()
            if msg.split()[0] == 'exit':
                self.is_open = False
                self.close()
            self.buffer.append((msg, addr))
        print("Server thread listening closed.")
        exit()

