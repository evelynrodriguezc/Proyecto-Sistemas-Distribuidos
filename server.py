import threading
import socket
import pickle
import random

PORT = 8001
BUFFER_SIZE = 1024

bd = {'username':[], 'socket':[], 'color':[]}
colors = ['Red', 'Yellow' , 'White', 'Green']


class Server(threading.Thread):
    def __init__(self, conn, addr):
        threading.Thread.__init__(self, target=Server.run)
        #conn is a new socket object that can be used to send and receive data on the connection,
        self.conn = conn
        #the address is the address bound to the socket at the other end of the connection
        self.addr = addr
        #it tells me if the user is logged in
        self.User_logged = False

    def assign_color(self) -> str:
        for el in colors:
            if el not in bd['color']:
                return el
    
    def run(self):
        with self.conn:
            print('conected', self.addr)
            while True:
                #data is a dictionary
                data = pickle.loads(self.conn.recv(BUFFER_SIZE))

                if len(bd['username']) < 4:
                    if not self.User_logged and not data['conected']:
                        #change options
                        self.User_logged = True
                        data['conected'] = True
                        data['color_user'] = self.assign_color()

                        bd['username'].append(data['name_user'])
                        data['bd_users'] = bd['username']
                        bd['socket'].append(self.conn)
                        bd['color'].append(data['color_user'])


                        #send other players
                        for s in bd['socket']:
                            if s != self.conn:
                                s.sendall(pickle.dumps(data))
                        self.conn.sendall(pickle.dumps(data))
                     
                else:
                    self.conn.sendall(pickle.dumps('Server is full'))
                    break


def create_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #bind the socket to an address
        s.bind((socket.gethostname(),PORT))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            Server(conn, addr).start()

if __name__ == '__main__':
    create_server()

