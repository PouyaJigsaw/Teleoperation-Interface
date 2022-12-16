import socket

def server_program():
    hostname = socket.gethostname()
    print(hostname)
    # host = socket.gethostbyname('hp-green')
    # print(host)

    #server socket
    s = socket.socket()
    s.bind(('192.168.2.15',9999))
    s.listen(2)
    print("waiting for connection")
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024).decode()
        print(data)


if __name__=='__main__':
    server_program()