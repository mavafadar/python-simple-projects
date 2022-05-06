import threading
import socket


def receive(nickname, client):
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print('An error occurred!')
            client.close()
            break


def write(nickname, client):
    while True:
        message = f'{nickname}: {input()}'
        client.send(message.encode('ascii'))


def main():
    nickname = input('Enter your nickname: ')

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 55555))

    receive_thread = threading.Thread(target=receive, args=(nickname, client))
    receive_thread.start()

    write_thread = threading.Thread(target=write, args=(nickname, client))
    write_thread.start()


if __name__ == '__main__':
    main()
