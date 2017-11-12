
          
            
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
