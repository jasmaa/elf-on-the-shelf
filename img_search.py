import json
from urllib import request
from bs4 import BeautifulSoup

import os
import shutil
import time

# clear subdir
def clear(folder):
    # delete subdir contents
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

# retrieve image from wikipedia
def get_img_from_search(search, limit=5):

    # clear images folder
    clear('images')

    resp = request.urlopen("https://en.wikipedia.org/w/api.php?action=query&format=json&list=allimages&aifrom=" + search + "&aiprop=dimensions%7Cmime&ailimit="+str(limit))
    output = json.load(resp)

    img_list = []

    for query in output["query"]["allimages"]:
        title = query["title"]
        url = "https://en.wikipedia.org/wiki/" + process(title)
        resp = request.urlopen(url)

        soup = BeautifulSoup(resp.read(), "html5lib")
        img = soup.find("img")

        data = request.urlopen("https:" + img.get("src")).read()
        with open("images/" + title.replace("File:", ""), "wb") as f:
            f.write(data)
        #with open("images/" + title.replace("File:", ""), "w") as f:
        #    f.write(data)

        img_list.append(title.replace("File:", ""))

    return img_list

# process url
def process(title):
    title = title.replace("'", "%27")
    title = title.replace(" ", "_")

    return title
