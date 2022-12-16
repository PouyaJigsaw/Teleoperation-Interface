import socket
from event import *

c = socket.socket()
cmd = 0
c.connect(('192.168.2.252',9999))

cmd = c.recv(1024).decode()
post_event("receive_command", cmd)
msg = 'done!'
c.send(bytes())
    