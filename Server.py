import socket
from _thread import *
from GameClass import Game
import pickle
import sys

server = ""
port = 9999


def create_server():
    global server, port
    global soc
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def bind_port():
    global server, port
    try:
        soc.bind((server, port))
        soc.listen(2)
        print("Server Initiated...\nWaiting for Connection...")
    except Exception as e:
        print("Error: " + str(e))


def main():
    create_server()
    bind_port()


def gamefunction(conn, p, gameid):
    global playercount
    conn.send(str.encode(str(p)))
    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode("utf-8")
            if gameid in games:
                game = games[gameid]

                if not data:
                    break

                else:
                    if data == "reset":
                        game.resetgame()

                    elif data != "get":
                        data = data.split(",")
                        game.play(p, (int(data[0]), int(data[1])))
                        game.total_move += 1

                    reply = game
                    conn.send(pickle.dumps(reply))
            else:
                break
        except:
            break
    print("Lost Connection")
    try:
        del games[gameid]
        print("Deleting Game-Id: ", gameid)
    except:
        pass
    playercount -= 1
    conn.close()



games = {}
playercount = 0

main()
while True:
    conn, addr = soc.accept()
    print("Connected to IP:" + str(addr[0]))
    playercount += 1
    gameid = (playercount - 1) // 2

    p = 0
    if playercount % 2 == 1:
        games[gameid] = Game(gameid)
    else:
        games[gameid].ready = True
        p = 1
    start_new_thread(gamefunction, (conn, p, gameid))
