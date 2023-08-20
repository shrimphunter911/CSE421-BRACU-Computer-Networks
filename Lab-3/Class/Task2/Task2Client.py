import socket
header = 16
port = 10232
server = socket.gethostbyname(socket.gethostname())
addr = (server, port)
Format = 'utf-8'
disconnect_message = "End"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)
def send(msg):
    message = msg.encode(Format)
    msg_len = len(message)
    send_len = str(msg_len).encode(Format)
    send_len = send_len + b' ' * (header - len(send_len))
    client.send(send_len)
    client.send(message)
    print(client.recv(2048).decode(Format))
connected = True
while connected:
    input_message = input("Enter your message: ")
    if input_message == "end":
        connected = False
        send(disconnect_message)
    else:
        send(input_message)