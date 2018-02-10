import cv2



#
# Tello Python3 Control Demo
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import threading
import socket
import sys
import time


host = ''
port = 9000
locaddr = (host,port)


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    cv2.namedWindow('Control')
    sock.send("command")
    while True:

        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break



#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

while True:

    try:
        msg = input("");

        if not msg:
            break

        if 'end' in msg:
            print ('...')
            sock.close()
            break

        k = cv2.waitKey(1)
        if k & 0xFF == ord('a'):
            sock.sendto("left 20".encode(encoding="utf-8"), tello_address)
        if k & 0xFF == ord('s'):
            sock.sendto("back 20".encode(encoding="utf-8"), tello_address)
        if k & 0xFF == ord('w'):
            sock.sendto("forward 20".encode(encoding="utf-8"), tello_address)
        if k & 0xFF == ord('d'):
            sock.sendto("right 20".encode(encoding="utf-8"), tello_address)
        # Send data
        msg = msg.encode(encoding="utf-8")
        sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()
        break