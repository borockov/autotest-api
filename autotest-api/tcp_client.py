import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

message = input('Введите сообщение:')
client_socket.send(message.encode())

response = client_socket.recv(4096).decode()
print(response)

client_socket.close()
