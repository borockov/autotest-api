import socket
import threading

messages = []
def handle_client(client_socket, client_address):
    print(f"Пользователь с адресом: {client_address} подключился к серверу")

    try:
        data = client_socket.recv(1024).decode()
        if data:
            print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")
            messages.append(data)

            # Отправляем клиенту всю историю сообщений
            full_history = '\n'.join(messages)
            client_socket.send(full_history.encode())
    finally:
        client_socket.close()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(10)

    print("Сервер запущен и ждет подключений...")

    while True:
        client_socket, client_address = server_socket.accept()
        # Запускаем отдельный поток для каждого клиента
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == '__main__':
    server()
