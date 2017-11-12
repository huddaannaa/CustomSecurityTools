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
        print ('closing connection')
        sk.close()

        strdata = data[0]
        headers = strdata.splitlines()
        for s in headers:
            if re.search('Server: ', s):
                print(s)
            else:
                pass
          
            
def headers(link):
    import requests
    r = requests.get(link,timeout = 5)
    stat = r.status_code
    res  = [(header,value) for header, value in r.headers.items()]
    req  = [(header1,value1) for header1, value1 in r.request.headers.items()]
    return stat, res, req


def Extract_Urls_4rm_syte(url):
    from bs4 import BeautifulSoup
    import requests
    soup = BeautifulSoup(requests.get('http://' + url).text, 'lxml')
    return [link.get('href') for link in soup.find_all('a')]


def email_extractor(string):
    import re
    sp = re.split(r'\s|,', string)
    return [re.match(r'\w*@\w*.\w*.\w*', sp[n]).group() for n in range(len(sp))]


def img_pdf_scraper(url):
    from lxml import html
    import requests
    try:
        body = html.fromstring(requests.get('http://' + url).content) 
        images = body.xpath('//img/@src')
        pdfs   = body.xpath('//a[@href[contains(., ".pdf")]] /@href')
    except Exception, e:
        print e
        print 'connection error'
        return images, pdfs
