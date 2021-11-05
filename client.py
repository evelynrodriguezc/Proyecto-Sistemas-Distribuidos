import threading
import socket
from ui import *
import pickle

PORT = 8001
BUFFER_SIZE = 1024

class User(threading.Thread):
    def __init__(self,my_socket):
        threading.Thread.__init__(self,target=User.run)
        #to send and receive data from the server
        self.my_socket = my_socket
        self.exit = False
        self.want_to_play = False
        self.conected = False
        self.options = {
            'name_user':any,
            'connected_players':0,
            'players_name':[],
            'Your_turn':False,
            'option_user': any,
            'server_message': any
        }

    def run(self):
        while not self.exit:
            name = input('name')
            self.my_socket.sendall(pickle.dumps(self.options))
            data = self.my_socket.recv(1024)
            print(data.decode())

            
if __name__ == '__main__':
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((socket.gethostname(),PORT))

    user = User(my_socket)

    user.start()
