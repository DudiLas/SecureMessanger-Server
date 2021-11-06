from  Message_Client_DB import *
import socket
import threading
from Client_Handler import *
PORT_FILE_NAME = "port.info"


def handle_client(client):
    print("client connected")
    myClient = Client(client)
    while True:
        msg = myClient.recvMsg()
        myClient.handleMsg(msg)







def main():
    #get port number
    port_file = open(PORT_FILE_NAME)
    port = int(port_file.readline())
    #get local ip
    local_ip = socket.gethostbyname(socket.gethostname())
    print(local_ip)
    #intiallize server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(port)
    server.bind((local_ip,port))
    server.listen(5)


    #accepting clients
    while True:
        client, addr = server.accept()
        t = threading.Thread(target = handle_client, args = (client,))
        t.start()








if __name__ == "__main__":
    main()