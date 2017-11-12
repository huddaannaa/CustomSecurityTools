def banner_grab(host, port = 80):
    #Script by Hud Seidu Daannaa
    #this function takes 2 parameters, the (host IP and the Port)
    #default port is 80
    #_______________________________
    ''' Banner grabbing can be used to find network hosts that are 
        running versions of applications and operating systems with known
        exploits or glean information about a computer system on a network 
        and the services running on its open ports.'''
    import socket, re
    try:
        #establishing connection
        sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sk.connect((host, port))
    except:
        print 'connection error'

    h_get = b"GET / HTTP/1.1\nHost: "+host+"\n\n"
    data = ''
    try:
        sk.sendall(h_get)
        data = sk.recvfrom(1024)
        print data
    except socket.error:
        print ('Socket error', socket.errno)
    finally:
        #whether Try or exp the connection closes
        print ('closing connection')
        sk.close()

        strdata = data[0]
        headers = strdata.splitlines()
        for s in headers:
            if re.search('Server: ', s):
                print(s)
            else:
                pass
