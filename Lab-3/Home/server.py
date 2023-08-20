import socket

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "End"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()
print("Server is listening!")

conn, addr = server.accept()
isConnected = True

while isConnected:
    msg_length = conn.recv(HEADER).decode(FORMAT)

    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)

        if msg == DISCONNECT_MESSAGE:
            isConnected = False
            conn.send("Goodbye".encode(FORMAT))

        else:
            hours = int(msg)
            salary = 0

            if hours > 40:
                salary = 8000 + ((hours - 40) * 300)

            elif hours <= 40:
                salary = hours * 200

            conn.send(str(salary).encode(FORMAT))

conn.close()