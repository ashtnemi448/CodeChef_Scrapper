import bs4 as bs
from urllib.request import Request, urlopen


    url='https://www.codechef.com/users/'+ajaybgunjal199


    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = bs.BeautifulSoup(webpage, 'lxml')
    ratings=[]

    t = soup.find('section', class_='rating-data-section problems-solved')
    d=[]
    cnt=1
    clist=[]
    for x in t.find_all('p'):
        y = x.find('strong')
        q.append(y.text)
        for z in x.find_all('a'):
            s = z.text
            q.append(s)
            cnt+=1
        clist.append(cnt)


    context = {
        'q':q,
        'ratings': ratings,
        'd':d,
        'clist':clist,
    }
    template = loader.get_template('cf_scrapper/detail.html')
    return HttpResponse(template.render(context,request))
