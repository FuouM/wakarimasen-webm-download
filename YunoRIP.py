import timeit
import requests
import os
import shutil
import sys
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from tqdm.auto import tqdm





def nameEx(url):
    o = urlparse(url).path
    for i in range(1, len(o)):
        if o[-i] == "/" and o[-1] != 1:
            return -(i - 1)

threadlink = sys.argv[1]
folder = threadlink[-8:-1]
currentDir = ".\\"
path = os.path.join(currentDir, folder)
if os.path.isfile(path) == False:
    os.mkdir(path)

def downloadWEBM(title, url):
    timeStart = timeit.default_timer()
    file_path = os.path.join(path, title)
    with requests.get(url, stream=True) as desu:
        total_length = int(desu.headers.get("Content-Length"))
        with tqdm.wrapattr(desu.raw, "read", total = total_length, desc = title) as raw:
            with open(file_path, "wb") as output:
                shutil.copyfileobj(raw, output)
    timeStop = timeit.default_timer()
    print("{}, {} seconds\n".format(title, timeStop - timeStart))

timeStartAll = timeit.default_timer()
request = Request(threadlink, headers={'User-Agent': 'Mozilla/5.0'})
desuka = urlopen(request).read()
    
soup = BeautifulSoup(desuka, 'html.parser')

desu = open("{}.csv".format(threadlink[-8:-1]), "w", encoding='utf-8')
desu.write("{},{},{}\n".format("Name","Link","Filename"))
    
for link in soup.find_all('a'):
    file_url = str(link.get('href'))
    file_name = str(link.get('title'))
    if file_url.find(".webm") != -1:
        if file_name == "None":
            continue
        if file_name.find(",") != -1:
            file_name = file_name.replace(",", "")
        if urlparse(file_url).netloc == "files.catbox.moe":
            store_name = urlparse(file_url).path[1:]
            file_name = store_name
        else:
            store_name = file_url[nameEx(file_url):]
            
        downloadWEBM(file_name, file_url)
        
        desu.write("{},{},{}\n".format(file_name, file_url, store_name))

timeStopAll = timeit.default_timer()
print("Done in {} seconds".format(timeStopAll - timeStartAll))
desu.close()
