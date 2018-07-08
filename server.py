import socket

def main():
        host = '192.168.0.90'
        port = 1337
        s = socket.socket()
        s.bind((host, port))

        s.listen(1)
        c, addr = s.accept()

        while True:
                data = c.recv(1024)
                if not data:
                        break
                data = str(data).upper()
                c.send(data)
        c.close()

if __name__ == '__main__':
        main()
