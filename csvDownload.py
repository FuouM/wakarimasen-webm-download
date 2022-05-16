import requests
import csv
import os
import timeit
import shutil
from tqdm.auto import tqdm


thread = input("Path to csv: ")
timeStartAll = timeit.default_timer()
with open("{}".format(thread), "r", encoding='utf-8') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    folder = thread[:-4]
    currentDir = ".\\"
    path = os.path.join(currentDir, folder)
    if os.path.isfile(path) == True:
        os.mkdir(path)
        
    next(csvReader, None)
    for row in csvReader:
        timeStart = timeit.default_timer()
        file_path = os.path.join(path, row[0])
        with requests.get(row[1], stream=True) as desu:
            total_length = int(desu.headers.get("Content-Length"))
            with tqdm.wrapattr(desu.raw, "read", total = total_length, desc = row[0]) as raw:
                with open(file_path, "wb") as output:
                    shutil.copyfileobj(raw, output)
        timeStop = timeit.default_timer()
        print("{}, {} seconds\n".format(row[0], timeStop - timeStart))

timeStopAll = timeit.default_timer()
print("Done in {} seconds".format(timeStopAll - timeStartAll))
