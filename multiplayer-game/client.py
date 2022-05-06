import pygame

from network import Network
from button import Button


pygame.font.init()

window_width, window_height = 650, 600
this_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Client')

client_number = 0


def redraw_window(window, game, player):
    window.fill((128, 128, 128))

    if not game.connected():
        font = pygame.font.SysFont('Bahnschrift', 30)
        text = font.render('Waiting for other player...', 1, (255, 0, 0), True)
        window.blit(
            text,
            (window_width / 2 - text.get_width() / 2, window_height / 2 - text.get_height() / 2)
        )
    else:
        font = pygame.font.SysFont('Bahnschrift', 40)
        text = font.render('Your Move', 1, (0, 255, 255))
        window.blit(text, (80, 100))
        text = font.render('Opponents', 1, (0, 255, 255))
        window.blit(text, (380, 100))

        move_one = game.get_player_moves(0)
        move_two = game.get_player_moves(1)

        if game.both_moved():
            text_one = font.render(move_one, 1, (0, 0, 0))
            text_two = font.render(move_two, 1, (0, 0, 0))
        else:
            if game.player_one_moved and player == 0:
                text_one = font.render(move_one, 1, (0, 0, 0))
            elif game.player_one_moved:
                text_one = font.render('Locked In', 1, (0, 0, 0))
            else:
                text_one = font.render('Waiting...', 1, (0, 0, 0))

            if game.player_two_moved and player == 1:
                text_two = font.render(move_two, 1, (0, 0, 0))
            elif game.player_two_moved:
                text_two = font.render('Locked In', 1, (0, 0, 0))
            else:
                text_two = font.render('Waiting...', 1, (0, 0, 0))

        if player == 1:
            window.blit(text_two, (100, 250))
            window.blit(text_one, (400, 250))
        else:
            window.blit(text_one, (100, 250))
            window.blit(text_two, (400, 250))

        for button in buttons:
            button.draw(window)

    pygame.display.update()


buttons = [
    Button('Rock', 50, 400, (0, 0, 0)),
    Button('Scissors', 250, 400, (255, 0, 0)),
    Button('Paper', 450, 400, (0, 255, 255))
]


def main():
    clock = pygame.time.Clock()
    network = Network()
    player = int(network.get_player())
    print(f'You are player {player}')

    while True:
        clock.tick(10)
        try:
            game = network.send('get')
        except:
            print('Could not get the game...')
            break

        if game.both_moved():
            redraw_window(this_window, game, player)
            pygame.time.delay(500)
            try:
                game = network.send('reset')
            except:
                print('Could not get in the game...')
                break

            font = pygame.font.SysFont('Bahnschrift', 60)
            if game.winner() == player:
                text = font.render('You Won!', 1, (0, 255, 0))
            elif game.winner() == -1:
                text = font.render('Tie Game!', 1, (0, 0, 255))
            else:
                text = font.render('You Lost!', 1, (255, 0, 0))

            this_window.blit(
                text,
                (window_width / 2 - text.get_width() / 2, window_height / 2 - text.get_height() / 2)
            )
            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                for button in buttons:
                    if button.click(position) and game.connected():
                        if player == 0 and not game.player_one_moved:
                            network.send(button.text)
                        elif player == 1 and not game.player_two_moved:
                            network.send(button.text)
        redraw_window(this_window, game, player)


def menu_screen():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        this_window.fill((128, 128, 128))
        font = pygame.font.SysFont('Bahnschrift', 30)
        text = font.render('Click to Play', 1, (0, 0, 255))
        this_window.blit(text, (225, 275))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
    main()


if __name__ == '__main__':
    while True:
        menu_screen()
