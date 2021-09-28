'''''''''''''''''''''''''''''
> Filename: lv3.py
> Author: Kadrick, BoGwon Kang
> Created at: 2021/09/28 11:23
> Description: Regular Expression
'''''''''''''''''''''''''''''
import requests
from html.parser import HTMLParser
import re

# get html file
file = requests.get("http://www.pythonchallenge.com/pc/def/equality.html").text

# My Solution

# class for html parsing


class CHtmlParser(HTMLParser):
    def __init__(self, *, convert_charrefs: bool = ...) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self.comment = []

    def handle_comment(self, data):
        self.comment.append(data)

    def getComment(self):
        return self.comment

def mySolution():
    parser = CHtmlParser()
    parser.feed(file)
    
    text = parser.getComment()[0]
    target = r"[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]"

    result = re.findall(target, text)

    for idx in range(0, len(result)):
        print(result[idx][4], end="")

mySolution()