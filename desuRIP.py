from urllib.parse import urlparse
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import timeit

def nameEx(url):
    o = urlparse(url).path
    for i in range(1, len(o)):
        if o[-i] == "/":
            return -(i - 1)

threadlink = input("Enter thread link: ")

timeStart = timeit.default_timer()
request = Request(threadlink, headers={'User-Agent': 'Mozilla/5.0'})
desuka = urlopen(request).read()
    
soup = BeautifulSoup(desuka, 'html.parser')

desu = open("{}.csv".format(threadlink[-8:-1]), "w", encoding='utf-8')
desu.write("{},{},{}\n".format("Name","Link","Filename"))
    
for link in soup.find_all('a'):
    temp = str(link.get('href'))
    tamp = str(link.get('title'))
    if temp.find(".webm") != -1:
        if tamp == "None":
            continue
        if tamp.find(",") != -1:
            tamp = tamp.replace(",", "")
        if urlparse(temp).netloc == "files.catbox.moe":
            timp = urlparse(temp).path[1:]
            tamp = timp
        else:
            timp = temp[nameEx(temp):]
        desu.write("{},{},{}\n".format(tamp, temp, timp))

timeStop = timeit.default_timer()
print("Done in {} seconds".format(timeStop - timeStart))
desu.close()
