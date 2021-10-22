import Message_Client_DB
import socket
import threading
PORT_FILE_NAME = "port.info"


def handle_client(client):
    pass


def main():
    #get port number
    port_file = open(PORT_FILE_NAME)
    port = int(port_file.readline()[:-1])
    #get local ip
    local_ip = socket.gethostbyname(socket.gethostname())

    #intiallize server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((local_ip,port))
    server.listen(5)


    #accepting clients
    while True:
        client, addr = server.accept()
        handle_client(client)








if __name__ == "__main__":
    main()