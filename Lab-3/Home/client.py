import socket

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)
FORMAT = "utf8"
DISCONNECT_MESSAGE = "End"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)

    print(client.recv(2048).decode(FORMAT))


isConnected = True
while isConnected:
    hours = input("Please enter working hours: ")

    if hours == DISCONNECT_MESSAGE:
        send(DISCONNECT_MESSAGE)
        isConnected = False

    else:
        send(hours)