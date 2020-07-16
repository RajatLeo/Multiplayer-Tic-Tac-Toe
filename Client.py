import pygame
import socket
from Network import Network
from GameClass import Game
import pickle
import time
import sys
from pygame import mixer

pygame.init()

window_size = (900, 600)
win = pygame.display.set_mode(window_size)
pygame.display.set_caption("Tic-Tac-Toe")
logo = pygame.image.load("tic-tac-toe.png")
pygame.display.set_icon(logo)

backmusic = mixer.music.load("Background.wav")
mixer.music.play(-1)

font = pygame.font.Font('freesansbold.ttf', 32)

# variable to reset game
reset = False


def grid():
    # Vertical Lines
    for i in range(4):
        pygame.draw.line(win, (50, 50, 50), (((window_size[0] - 300) // 3) * i, 0),
                         (((window_size[0] - 300) // 3) * i, (window_size[1])),
                         5)
    # Horizontal Lines
    for i in range(4):
        pygame.draw.line(win, (50, 50, 50), (0, ((window_size[1]) // 3) * i),
                         (window_size[0] - 300, ((window_size[1]) // 3) * i),
                         5)

    pygame.draw.rect(win, (50, 50, 50), (600, 0, 300, 600))


def markgrid(pos, game, player):
    if pos[0] < 600 and pos[1] < 600 and player == 0 and game.p1move == False:
        x = pos[0] // 200
        y = pos[1] // 200
        if game.board[x][y] == 0:
            pygame.draw.circle(win, (0, 0, 150), ((x * 200) + 100, (y * 200) + 100), 90, 10)
            pygame.display.update()
            click = mixer.Sound("click.wav")
            click.play()
            return str(x) + "," + str(y)
    elif pos[0] < 600 and pos[1] < 600 and player == 1 and game.p2move == False:
        x = pos[0] // 200
        y = pos[1] // 200
        if game.board[x][y] == 0:
            pygame.draw.line(win, (0, 150, 0), (x * 200 + 10, y * 200 + 10), ((x + 1) * 200 - 10, (y + 1) * 200 - 10),
                             10)
            pygame.draw.line(win, (0, 150, 0), ((x + 1) * 200 - 10, y * 200 + 10),
                             (x * 200 + 10, (y + 1) * 200 - 10),
                             10)
            pygame.display.update()
            click = mixer.Sound("click.wav")
            click.play()
            return str(x) + "," + str(y)
    else:
        return None


def result_panel(win, game, player):
    if player == 0:
        if game.p1move == False:
            font = pygame.font.SysFont("comicsans", 40)
            txt = font.render("Your Move", True, (255, 255, 255))
            win.blit(txt, (660, 100))
        else:
            font = pygame.font.SysFont("comicsans", 40)
            txt = font.render("Opponent's Move", True, (255, 255, 255))
            win.blit(txt, (630, 100))

    elif player == 1:
        if game.p2move == False:
            font = pygame.font.SysFont("comicsans", 40)
            txt = font.render("Your Move", True, (255, 255, 255))
            win.blit(txt, (660, 100))
        else:
            font = pygame.font.SysFont("comicsans", 40)
            txt = font.render("Opponent's Move", True, (255, 255, 255))
            win.blit(txt, (630, 100))


def winner_check(game, player):
    global reset
    res = game.game_winner()
    if player == 0:
        if res == 0:
            win.fill((200, 200, 200))
            font = pygame.font.SysFont("comicsans", 100)
            txt = font.render("You Won", True, (255, 50, 50))
            win.blit(txt, (250, 250))
            mixer.music.stop()
            won = mixer.Sound("win.wav")
            won.play()
            reset = True
        elif res == 1:
            win.fill((200, 200, 200))
            font = pygame.font.SysFont("comicsans", 100)
            txt = font.render("You Lost", True, (255, 50, 50))
            win.blit(txt, (250, 250))
            mixer.music.stop()
            loss = mixer.Sound("lose.wav")
            loss.play()
            reset = True
        elif res == None:
            win.fill((200, 200, 200))
            font = pygame.font.SysFont("comicsans", 100)
            txt = font.render("Draw", True, (255, 50, 50))
            win.blit(txt, (300, 250))
            mixer.music.stop()
            reset = True
    if player == 1:
        if res == 1:
            win.fill((200, 200, 200))
            font = pygame.font.SysFont("comicsans", 100)
            txt = font.render("You Won", True, (255, 50, 50))
            win.blit(txt, (250, 250))
            mixer.music.stop()
            won = mixer.Sound("win.wav")
            won.play()
            reset = True
        elif res == 0:
            win.fill((200, 200, 200))
            font = pygame.font.SysFont("comicsans", 100)
            txt = font.render("You Lost", True, (255, 50, 50))
            win.blit(txt, (250, 250))
            mixer.music.stop()
            loss = mixer.Sound("lose.wav")
            loss.play()
            reset = True
        elif res == None:
            win.fill((200, 200, 200))
            font = pygame.font.SysFont("comicsans", 100)
            txt = font.render("Draw", True, (255, 50, 50))
            mixer.music.stop()
            win.blit(txt, (300, 250))
            reset = True


def draw_board(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 1:
                pygame.draw.circle(win, (0, 0, 150), ((i * 200) + 100, (j * 200) + 100), 90, 10)
            elif board[i][j] == 2:
                pygame.draw.line(win, (0, 150, 0), (i * 200 + 10, j * 200 + 10),
                                 ((i + 1) * 200 - 10, (j + 1) * 200 - 10),
                                 10)
                pygame.draw.line(win, (0, 150, 0), ((i + 1) * 200 - 10, j * 200 + 10),
                                 (i * 200 + 10, (j + 1) * 200 - 10),
                                 10)


def printtime(start):
    sec = start % 60
    min = sec // 60
    timetxt = str(min) + ":" + str(sec)
    timepl = font.render("Time Played: ", True, (255, 255, 255))
    win.blit(timepl, (650, 440))
    timeImg = font.render(timetxt, True, (255, 255, 255))
    win.blit(timeImg, (720, 500))


def window(win, game, player, board, timestart):
    win.fill((200, 200, 200))
    if game.connected() == False:
        pfont = pygame.font.SysFont("comicsans", 80)
        wait = pfont.render("Waiting For other Player...", True, (255, 50, 50))
        win.blit(wait, (100, 250))
        #wait = mixer.Sound("wait.wav")
        #wait.play()
    else:
        timeplayed = round(time.time() - timestart)
        grid()
        draw_board(board)
        result_panel(win, game, player)
        printtime(timeplayed)
        winner_check(game, player)
    pygame.display.update()


def main():
    global reset
    run = True
    n = Network()
    player = int(n.p_num())
    print("You are Player: ", player)
    timestart = time.time()
    while run:
        if reset:
            pygame.time.delay(2000)
            game = n.send("reset")
            reset = False
            mixer.music.play(-1)
        try:
            game = n.send("get")
        except:
            print("Unable to receive game")
            break
        window(win, game, player, game.board, timestart)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                mark = pygame.mouse.get_pos()
                pos = markgrid(mark, game, player)
                if pos != None:
                    game = n.send(pos)


def firstmenu():
    runmenu = True
    try:
        while runmenu:
            win.fill((200, 200, 200))
            pfont = pygame.font.SysFont("comicsans", 100)
            wait = pfont.render("Click To Play!", True, (255, 50, 50))
            win.blit(wait, (190, 250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runmenu = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    runmenu = False
        main()
    except:
        pygame.quit()
        sys.exit()

while True:
    firstmenu()
