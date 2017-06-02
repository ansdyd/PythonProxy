import socket
import sys
from thread import *

# simple proxy based on the tutorial by Sergeant Sploit

try:
	listen_port = int(raw_input("Type and Enter Your Listening Port Number: "))
except KeyboardInterrupt:
	print "Keyboard Interrupt"
	print "Proxy Terminating"
	sys.exit()

max_conn = 5
buffer_size = 8192 # the max of the socket buffer size

def proxy_server(webserver, port, conn, data, address):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((webserver, port))
		s.send(data)

		while True:
			reply = s.recv(buffer_size)

			if (len(reply) > 0):
				conn.send(reply)
			else:
				break

		s.close()
		conn.close()
	except socket.error, (value, message):
		s.close()
		conn.close()
		sys.exit(1)

def conn_string(conn, data, address):
	try:
		first_line = data.split('\n')[0]
		url = first_line.split(' ')[1]

		pos_http = url.find('://')
		
		if (pos_http == -1):
			temp - url
		else:
			temp = url[(http_pos + 3):]

		pos_port = temp.find(':')
		pos_webserver = temp.find("/")
		
		if (pos_webserver == -1):
			pos_webserver = len(temp)
		webserver = ""
		port = -1
		
		if (pos_port == -1 or pos_webserver < pos_port):
			port = 80
			webserver = temp[:pos_webserver]
		else:
			port = int((temp[(port_pose + 1):])[:pos_webserver - pos_port - 1])
			webserver = temp[:pos_port]

		proxy_server(webserver, port, conn, address, data)
	except Exception e:
		pass



def start():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket to be used
		s.bind('', listen_port)
		s.listen(max_conn) # connections limited by the maximum number of connections supported
		print('Listening Successfully at %d' % (listen_port))
	except Exception e:
		print 'Failed to Initialize Socket'
		sys.exit()


	# the main loop of the proxy
	while True:
		try:
			conn, address = s.accept()
			data = conn.recv(buffer_size)
			start_new_thread(conn_string, (conn, data, address))
		except KeyboardInterrupt:
			s.close()
			print 'User Keyboard Interrupt'
			sys.exit(1)

	s.close()

if __name__ == '__main__':
	start()

