from django.http import HttpResponse
from django.template import loader
import bs4 as bs
from urllib.request import Request, urlopen
from collections import OrderedDict

# rating star global rank country rank

class mi:
    name=""

def index(request):
    a=['hello','motto']

    template=loader.get_template('cf_scrapper/index.html')
    context={
        'a':a
    }
    return HttpResponse(template.render(context,request))

def search(request):

    mi.name=request.GET['q']
    url='https://www.codechef.com/users/'+mi.name


    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = bs.BeautifulSoup(webpage, 'lxml')
    ratings=[]

    r1 = soup.find('div', class_='rating-number')
    ratings.append(r1.text)

    cnt = 0
    r2 = soup.find('div', class_='rating-star')

    for x in r2.find_all('span'):
        cnt += 1

    ratings.append(cnt)
    q=[]
    r3 = soup.find('div', class_='rating-ranks')

    for x in r3.find_all('li'):
        y = x.find('a')
        ratings.append(y.text)

    t = soup.find('section', class_='rating-data-section problems-solved')
    q = []
    clist = []
    dic = {}
    f = 0
    a = t.find_all('article')

    a1 = a[0].find_all('p')

    for x in a1:
        y = x.find('strong')
        nm = y.text
        for z in x.find_all('a'):
            s = z.text
            q.append(s)
        print(q)
        dic[nm] = q
        q = []
    if(len(a)>1):
        a1 = a[1].find_all('p')
        for x in a1:
            y = x.find('strong')
            nm = y.text + '(Partial)'
            for z in x.find_all('a'):
                s = z.text
                q.append(s)
            print(q)
            dic[nm] = q
            q = []


    context = {
        'dic':dic,
        'ratings': ratings,
    }
    template = loader.get_template('cf_scrapper/detail.html')
    return HttpResponse(template.render(context,request))

def ans(request,string):
    s1=string.replace(":", "")
    s=s1.split('-')
    if 'Practice' in s:
        url='https://www.codechef.com/status/'+s[0]+','+mi.name
    else:
        url='https://www.codechef.com/'+s[1]+'/status/'+s[0]+','+mi.name

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    s = bs.BeautifulSoup(webpage, 'lxml')

    f = s.find('div', class_='tablebox-section l-float')
    sd = f.find('tbody')
    fg = sd.find('tr')
    gf = fg.find_all('td')
    df = gf[7]

    af = df.find('a')

    newurl = 'https://www.codechef.com' + af['href']
    abc=newurl
    req = Request(newurl, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = bs.BeautifulSoup(webpage, 'lxml')

    h = []

    table = soup.find("ol")

    for t in table.find_all('li'):
        h.append(t.text)

    context = {
        'h': h,
        'url':url,
    }
    template = loader.get_template('cf_scrapper/ans.html')
    return HttpResponse(template.render(context, request))


