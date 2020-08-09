# **Multiplayer Tic-Tac-Toe**

This is Online Multiplayer Tic-Tac-Toe Game with [Server File](https://github.com/RajatLeo/Multiplayer-Tic-Tac-Toe/blob/master/Server.py) and [Client File](https://github.com/RajatLeo/Multiplayer-Tic-Tac-Toe/blob/master/Client.py). [Game Class](https://github.com/RajatLeo/Multiplayer-Tic-Tac-Toe/blob/master/GameClass.py) and [Network File](https://github.com/RajatLeo/Multiplayer-Tic-Tac-Toe/blob/master/Network.py) are helper file for [client](https://github.com/RajatLeo/Multiplayer-Tic-Tac-Toe/blob/master/Client.py) to run. [Game Class](https://github.com/RajatLeo/Multiplayer-Tic-Tac-Toe/blob/master/GameClass.py) file is used to setup game and [Network File](https://github.com/RajatLeo/Multiplayer-Tic-Tac-Toe/blob/master/Network.py) is used to establish connection between [Server](https://github.com/RajatLeo/Multiplayer-Tic-Tac-Toe/blob/master/Server.py) and [Client](https://github.com/RajatLeo/Multiplayer-Tic-Tac-Toe/blob/master/Client.py).

**Getting Started:**

**Modules Used:**

- PyGame : Used to create interface of Game.
- Socket : Used to establish connection between [Server](https://github.com/RajatLeo/Multiplayer-Tic-Tac-Toe/blob/master/Server.py) and [Client](https://github.com/RajatLeo/Multiplayer-Tic-Tac-Toe/blob/master/Client.py).
- Thread : Used to run many Game simultaneously i.e. to Create another thread to run in parallel.
- Pickle : Used to transfer Game Object between [Server](https://github.com/RajatLeo/Multiplayer-Tic-Tac-Toe/blob/master/Server.py) and [Client](https://github.com/RajatLeo/Multiplayer-Tic-Tac-Toe/blob/master/Client.py).
- Time : Used to add Running Time on [Client](https://github.com/RajatLeo/Multiplayer-Tic-Tac-Toe/blob/master/Client.py) Interface.
- Sys :  Used to close [Client](https://github.com/RajatLeo/Multiplayer-Tic-Tac-Toe/blob/master/Client.py) window after game ends.
- Mixer(Pygame) : Used to add various Sound effect and Background music in Game.


**Modules Required to be installed:**

     You need to have Pygame Module to run this Project.

     >>To install Pygame Module:
       -Open Command Prompt.

       -Enter following Command:
         >pip install pygame

**How to Run Game:**

-  In [Network.py](https://github.com/RajatLeo/Multiplayer-Tic-Tac-Toe/blob/master/Network.py), at [line 7](https://github.com/RajatLeo/Multiplayer-Tic-Tac-Toe/blob/75bebdfe82970e23c8dc3d9492746318dbf3d684/Network.py#L7) (i.e. self.server = "Enter Your Server Address") you need to enter IP address of server on which [Server.py](https://github.com/RajatLeo/Multiplayer-Tic-Tac-Toe/blob/master/Server.py) is going to run. IP is string Value so don't remove double quote.

- First Run [Server.py](https://github.com/RajatLeo/Multiplayer-Tic-Tac-Toe/blob/master/Server.py) on server and then run [Client.py](https://github.com/RajatLeo/Multiplayer-Tic-Tac-Toe/blob/master/Client.py) so that Client can connect to server.

- Since it is Online Multiplayer Game, and so Internet is required to run this game.


**Author:**

-[Rajat Srivastava/RajatLeo](https://github.com/RajatLeo)

**Attribute:**

-Images used as Window icon are from [FlatIcon](https://flaticon.com).

-Music and Sound are from [Free Sounds](http://www.freesound.org/).
