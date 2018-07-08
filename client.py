import socket

def main():
	host = '192.168.0.90'
	port = 1337
	sock = socket.socket()
	sock.connect((host, port))

	msg = raw_input("->")
	while msg != 'q':
		sock.send(msg)
		data = sock.recv(1024)
		print "response: {}".format(data)
		msg = raw_input("->")
	sock.close()

if __name__ == '__main__':
	main()
