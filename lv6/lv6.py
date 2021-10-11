'''''''''''''''''''''''''''''
> Filename: lv6.py
> Author: Kadrick, BoGwon Kang
> Created at: 2021/10/11 16:07
> Description: zip
'''''''''''''''''''''''''''''
import zipfile
import re

# open zipfile
zfile = zipfile.ZipFile('./channel.zip')

# check list
'''
print(zfile.namelist())
print(zfile.read("readme.txt"))
print(zfile.read("90052.txt"))
'''

# follow nothing & collect the comments
comments = ""

nothing = "90052.txt"
target = r"[0-9]+"

while True:
    answer = zfile.read(nothing).decode('utf-8')
    # collect comment
    comments += zfile.getinfo(nothing).comment.decode('utf-8')
    print(answer)

    findRet = re.findall(target, answer)

    if len(findRet) == 0:
        break
    
    nothing = findRet[0] + ".txt"

print("answer is ...")
print(comments)
