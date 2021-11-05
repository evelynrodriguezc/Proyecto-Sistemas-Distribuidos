import threading
import socket
import pickle

PORT = 8001
BUFFER_SIZE = 1024

bd = {'username':[], 'socket':[]}


class Server(threading.Thread):
    def __init__(self, conn, addr):
        threading.Thread.__init__(self, target=Server.run)
        #conn is a new socket object that can be used to send and receive data on the connection,
        self.conn = conn
        #the address is the address bound to the socket at the other end of the connection
        self.addr = addr

    def run(self):
        with self.conn:
            while True:
                #data is a dictionary
                data = self.conn.recv(BUFFER_SIZE)
                print(data.decode())
                msg = f'hola {data.decode()}'
                self.conn.sendall()


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


