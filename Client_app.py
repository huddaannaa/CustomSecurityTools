import socket, sys, os

host_ = socket.gethostbyname('localhost')
port_ = 4444

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.connect((host_, port_))
while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            sock.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print client_response
