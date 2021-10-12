'''''''''''''''''''''''''''''
> Filename: lv7.py
> Author: Kadrick, BoGwon Kang
> Created at: 2021/10/12 16:39
> Description: image
'''''''''''''''''''''''''''''
from PIL import Image

img = Image.open("./oxygen.png")

# img info
print("img Sz: ", img.size, "\nmode: ", img.mode)

# check all pixel
'''
for y in range(0,img.size[1]):
    for x in range(0, img.size[0]):
        print(img.getpixel((x,y)), end="")
    print("")
'''

for y in range(0, img.size[1], 8):
    for x in range(0, img.size[0], 7):
        ret = img.getpixel((x, y))
        if ret[0] == ret[1] == ret[2]:
            # print(ret)
            print(chr(ret[0]), end="")

print("")
answer = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for idx in range(0, len(answer)):
    print(chr(answer[idx]), end="")
