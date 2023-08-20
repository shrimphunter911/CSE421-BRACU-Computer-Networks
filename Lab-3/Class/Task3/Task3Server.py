import socket
import threading
header = 16
port = 10232
server = socket.gethostbyname(socket.gethostname())
addr = (server, port)
Format = 'utf-8'
disconnect_message = "End"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)


def handle_clients(connection,addr):
    connected = True
    while connected:
        msg_len = connection.recv(header).decode(Format)
        if msg_len:
            msg_len = int(msg_len)
            msg = connection.recv(msg_len).decode(Format)
            if msg == disconnect_message:
                connected = False
                connection.send("Goodbye".encode(Format))
            else:
                count = 0
                vowels = "aeiouAEIOU"
                for i in msg:
                    if i in vowels:
                        count += 1

                if count == 0:
                    connection.send("Not enough vowels".encode(Format))
                elif count <= 2:
                    connection.send("Enough vowels I guess".encode(Format))
                else:
                    connection.send("Too many vowels".encode(Format))
    connection.close()


def start():
    server.listen()
    print("Server is Listening and Online.")
    while True:
        connection, addr = server.accept()
        thread = threading.Thread(target=handle_clients, args=(connection, addr))
        thread.start()
        print(f"Total connected clients : {threading.active_count() - 1}")


start()