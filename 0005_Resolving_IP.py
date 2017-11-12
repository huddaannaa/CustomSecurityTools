def resolving_IP(link): 
    import socket
    if 'com' in link or 'www' in link or 'http' or '/' in link:
        try:
            return socket.gethostbyname(link)
        except:
            print 'connection error'
    else:
        try:
            return socket.gethostbyaddr(link)
        except:
            print 'connection error'
