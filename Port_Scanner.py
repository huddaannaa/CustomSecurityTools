def port_scanner(ip_add, port):
    import socket 
    #print 'connecting ...'
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(5)
    except:
        print 'connection error'
    if (sock.connect_ex((ip_add, port)) == 0):
        return 'Port', port, ' of', ip_add, ' is open'
    else:
        return 'Port', port, ' of', ip_add, ' is filtered'
    sock.close()
