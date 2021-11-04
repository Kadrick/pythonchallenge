'''''''''''''''''''''''''''''
> Filename: lv11.py
> Author: Kadrick, BoGwon Kang
> Created at: 2021/1104 16:36
> Description: image
'''''''''''''''''''''''''''''
from PIL import Image

img = Image.open("./cave.jpg")

# img info
print("img Sz: ", img.size, "\nmode: ", img.mode)

# empty image
empty_im_even = Image.new("RGB", (680 // 2, 480 // 2), "white")
empty_im_odd = Image.new("RGB", (680 // 2, 480 // 2), "white")

count = 0

# check all pixel put even or odd pixel
for y in range(0, img.size[1]):
    for x in range(0, img.size[0]):
        pixel = img.getpixel((x, y))
        if(count % 2):
            empty_im_odd.putpixel((x // 2, y // 2), pixel)
        else:
            empty_im_even.putpixel((x // 2, y // 2), pixel)
        count += 1

empty_im_even.save("./even.jpg")
empty_im_odd.save("./odd.jpg")
