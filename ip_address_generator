def private_ip_gen(local = False, a_ = [10, 172, 192], end_ = 5):
    ip_list = []
    if local == True:
        local   = '127.0.0.1'
        #ip_list.join(local)
        return ''.join(local)
    else:
        for a in a_:
            if a == 10:
                for s in range(1,end_):
                    for d in range(1,end_):
                        for f in range(1,end_):
                            ip = str(a) + '.' + str(s) + '.' + str(d) + '.' + str(f)
                            #print ip
                            ip_list.append(ip)       
            if a == 172:
                s = 16
                for d in range(1,end_):
                    for f in range(1,end_):
                        ip = str(a) + '.' + str(s) + '.' + str(d) + '.' + str(f)
                        #print ip
                        ip_list.append(ip)
            if a == 172:
                s = 31
                for d in range(1,end_):
                    for f in range(1,end_):
                        ip = str(a) + '.' + str(s) + '.' + str(d) + '.' + str(f)
                        #print ip
                        ip_list.append(ip)
            if a == 192:
                s = 168
                for d in range(1,end_):
                    for f in range(1,end_):
                        ip = str(a) + '.' + str(s) + '.' + str(d) + '.' + str(f)
                        #print ip
                        ip_list.append(ip)
    return ip_list
