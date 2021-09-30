'''''''''''''''''''''''''''''
> Filename: lv4.py
> Author: Kadrick, BoGwon Kang
> Created at: 2021/09/30 13:57
> Description: request
'''''''''''''''''''''''''''''
import requests
import re

target = r"[0-9]+"
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
waypoint = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=16044"

while True:
    # get page src
    text = requests.get(url).text

    print("url: ", url)
    print("text: ", text)

    # parse rc
    ret = re.findall(target, text)

    if ret:
        replaceNum = re.findall(target, url)
        # wrong path
        if ret[0] == "82682":
            ret[0] = "63579"
        url = url.replace(replaceNum[0], ret[0])
    else:
        # nothing/2 path
        if url == waypoint:
            url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022"
            continue
        break
