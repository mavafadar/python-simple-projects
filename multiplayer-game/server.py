import socket
import _thread
import pickle

from game import Game


server = '192.168.0.18'
port = 5555

this_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    this_socket.bind((server, port))
except socket.error as error:
    print(error)

this_socket.listen()
print('Waiting for a connection, server started...')

connected = set()
games = dict()
id_count = 0


def threaded_client(connection, current_player, game_id):
    global id_count
    connection.send(str.encode(str(current_player)))
    while True:
        try:
            data = connection.recv(4096).decode()
            if game_id in games:
                game = games[game_id]
                if not data:
                    break
                else:
                    if data == 'reset':
                        game.reset_move()
                    elif data != 'get':
                        game.play(current_player, data)

                    reply = game
                    connection.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break
    print(f'Lost Connection!\nClosing Game {game_id}...')
    try:
        del games[game_id]
    except:
        pass
    id_count -= 1
    connection.close()


def main():
    global connected, games, id_count
    while True:
        this_connection, address = this_socket.accept()
        print(f'Connected to {address}')

        id_count += 1
        player = 0
        game_id = (id_count - 1) // 2

        if id_count % 2 == 1:
            games[game_id] = Game(game_id)
            print('Creating a new game...')
        else:
            games[game_id].ready = True
            player = 1

        _thread.start_new_thread(threaded_client, (this_connection, player, game_id))


if __name__ == '__main__':
    main()
