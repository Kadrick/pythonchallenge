'''''''''''''''''''''''''''''
> Filename: lv2.py
> Author: Kadrick, BoGwon Kang
> Created at: 2021/09/27 10:45
> Description: Counting
'''''''''''''''''''''''''''''
from typing import Counter
import requests
from html.parser import HTMLParser

# get html file
file = requests.get("http://www.pythonchallenge.com/pc/def/ocr.html").text

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
    # first, find string in html file
    parser = CHtmlParser()
    parser.feed(file)
    comment = (parser.getComment())[1]

    # second, counting
    count = {}

    for idx in range(0, len(comment)):
        if comment[idx] in count:
            count[comment[idx]] += 1
        else:
            count[comment[idx]] = 1

    print(count)

    # third, show rare char
    result = ""

    for key, val in count.items():
        if val == 1:
            result += key

    print(result)


def solutionByCounter():
    # first, find string in html file
    parser = CHtmlParser()
    parser.feed(file)
    comment = (parser.getComment())[1]

    # second, counting
    count = Counter(comment)
    print(count)

    # third, show rare char
    result = ""

    for key, val in count.items():
        if val == 1:
            result += key

    print(result)


print("My solution")
mySolution()

print("by Counter")
solutionByCounter()
