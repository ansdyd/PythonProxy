import socket
import sys
from thread import *

try:
	listen_port = int(raw_input("Type and Enter Your Listening Port Number: "))
except KeyboardInterrupt:
	print "Keyboard Interrupt"
	print "Proxy Terminating"
	sys.exit()

max_conn = 5
buffer_size = 8192 # the max of the socket buffer size


def start():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket to be used
		



