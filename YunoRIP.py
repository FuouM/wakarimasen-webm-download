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
        if o[-i] == "/" and i != 1:
            return -(i - 1)

threadlink = sys.argv[1]
folder = threadlink[nameEx(threadlink):]
currentDir = ".\\"
if len(sys.argv) > 2:
    currentDir = sys.argv[2] + ".\\"
path = os.path.join(currentDir, folder)
if os.path.isdir(path) == False:
    os.mkdir(path)
print(path)
def downloadWEBM(title, url):
    file_path = os.path.join(path, title)
    if os.path.isfile(file_path) == False:
        timeStart = timeit.default_timer()
        with requests.get(url, stream=True) as desu:
            total_length = int(desu.headers.get("Content-Length"))
            with tqdm.wrapattr(desu.raw, "read", total = total_length, desc = title) as raw:
                with open(file_path, "wb") as output:
                    shutil.copyfileobj(raw, output)
        timeStop = timeit.default_timer()
        print("{}, {} seconds\n".format(title, timeStop - timeStart))
    else:
        print("File already exist\t{}".format(title))

timeStartAll = timeit.default_timer()
request = Request(threadlink, headers={'User-Agent': 'Mozilla/5.0'})
desuka = urlopen(request).read()
    
soup = BeautifulSoup(desuka, 'html.parser')

desu = open("{}.csv".format(threadlink[-8:-1]), "w", encoding='utf-8')
desu.write("{},{},{}\n".format("Name","Link","Filename"))

div = soup.find('div', class_="post_file_controls")
children = div.findChildren("a" , recursive=False)
first_post = str(children[-1]).replace("<a class=\"btnr parent\" download=", "").replace(" href", "").replace("\"", "").replace("><i class", "").split("=")
if first_post[0].find(".webm") != -1:
    downloadWEBM(first_post[0], first_post[1])
    desu.write("{},{},{}\n".format(first_post[0], first_post[1], first_post[1][nameEx(first_post[1]):]))
    
for link in soup.find_all('a'):
    file_url = str(link.get('href'))
    file_name = str(link.get('title'))
    
    if file_url.find(".webm") != -1:
        if file_name == "None":
            continue
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