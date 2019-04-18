import socket

BUFSIZE = 4096

sock = socket.create_connection(('localhost', 12345))
directions = sock.recv(BUFSIZE)

while True:
    prob = sock.recv(BUFSIZE)
    if not any(x in '+-/*' for x in prob.decode()):
        print(prob)
        break
    sock.send(f"{round(eval(prob.decode().strip()), 2)}\n".encode())

sock.close()

