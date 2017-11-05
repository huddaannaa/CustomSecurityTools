def banner_grab(parsed_args):
    import socket, re
    try:
        sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sk.connect((parsed_args, 80))
    except:
        print 'connection error'

    h_get = b"GET / HTTP/1.1\nHost: "+parsed_args+"\n\n"
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
