import threading
import socket
import os
import pickle

from ui import menu_to_enter, menu_player

PORT = 8001
BUFFER_SIZE = 1024

class User(threading.Thread):
    def __init__(self,my_socket):
        threading.Thread.__init__(self,target=User.run)
        #to send and receive data from the server
        self.my_socket = my_socket
        self.exit = False
        self.want_to_play = False #N
        self.conected = False
        self.your_turn = False  #N
        self.colo_user = any
        self.data = None
        self.name_user = any
        self.options = {
            'name_user':any,
            'conected':False,
            'option_menu':0,
            'color_user':any,
            'want_to_play': False,
            'your_turn': False,

            'bd_users': any
        }


    def play(self):

        while not self.exit and self.conected:
            if not self.your_turn:
                self.data['your_turn'] = self.your_turn
                menu_player(self.data, self.name_user, self.conected, self.colo_user)
                self.data = pickle.loads( self.my_socket.recv(BUFFER_SIZE))

    def run(self):
        while not self.conected:
            os.system('clear')
            menu_to_enter()
            option = int(input('Select:'))
            if option == 1:
                self.options['option_menu'] = 1
                name_user = input('Enter your User name:')
                self.options['name_user'] = name_user
                self.my_socket.sendall(pickle.dumps(self.options))
                
                self.data = pickle.loads(self.my_socket.recv(BUFFER_SIZE))


                if type(self.data) == dict and self.data['conected']:
                    self.conected = True
                    self.name_user = self.data['name_user']
                    self.colo_user = self.data['color_user']
                    self.play()
                else:
                    print(self.data)
                    break

            elif option == 2:
                break
        self.my_socket.close()
            
if __name__ == '__main__':
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((socket.gethostname(),PORT))

    user = User(my_socket)

    user.start()
