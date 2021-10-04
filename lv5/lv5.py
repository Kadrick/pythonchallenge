'''''''''''''''''''''''''''''
> Filename: lv5.py
> Author: Kadrick, BoGwon Kang
> Created at: 2021/10/05 01:54
> Description: pickle
'''''''''''''''''''''''''''''
import urllib.request
import pickle

textfile = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()

ret = pickle.loads(textfile)

for line in ret:
    target = ""
    for dump in range(len(line)):
        add = line[dump][0]
        for cnt in range(line[dump][1]):
            target += add
    print(target)
