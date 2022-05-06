import threading
import socket


def broadcast(message, clients):
    for client in clients:
        client.send(message)


def handle(client, clients, nicknames):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, clients)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            broadcast(f'{nicknames.pop(index)} left the chat.'.encode('ascii'), clients)
            break


def receive(server, clients, nicknames):
    while True:
        client, address = server.accept()
        print(f'Connected with {address}.')

        client.send('NICKNAME'.encode('ascii'))
        nickname = client.recv(1024).decode()
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}.')
        broadcast(f'{nickname} joined the chat!'.encode('ascii'), clients)
        client.send('Connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client, clients, nicknames))
        thread.start()


def main():
    host = '127.0.0.1'
    port = 55555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    clients = list()
    nicknames = list()

    print('Server is listening...')
    receive(server, clients, nicknames)


if __name__ == '__main__':
    main()
