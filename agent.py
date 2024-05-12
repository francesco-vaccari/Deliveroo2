from communication import Communication
import signal

HOST = '127.0.0.1'
SERVER_PORT = 8080
PORT = int(input("Enter the server port: "))

server = Communication(HOST, PORT)

server.send("connect", (HOST, SERVER_PORT))


# Gracefully terminate
def signal_handler(sig, frame):
    server.send("disconnect", (HOST, SERVER_PORT))
    server.send("exit", (HOST, PORT))
    server.server_thread.join()
    print("Exited correctly.")
    exit()

signal.signal(signal.SIGINT, signal_handler)






while server.is_open:
    # consume events that arrive from environment and process them into a belief set
    # send actions to the environment
    
    msg = input("msg to send: ")
    server.send(msg, (HOST, SERVER_PORT))

    # if len(server.buffer) > 0:
    #     msg, addr = server.buffer.pop(0)
    #     temp = msg.split()
        
    #     if temp[0] == 'error':
    #         print("An error occured with the server.")
    #     elif temp[0] == 'connected':
    #         print("Connected as agent: ", temp[1])
    #     else:
    #         print(msg)







server.server_thread.join()
print("Exited correctly.")
exit()