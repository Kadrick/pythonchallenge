'''''''''''''''''''''''''''''
> Filename: lv8.py
> Author: Kadrick, BoGwon Kang
> Created at: 2021/10/13 21:03
> Description: bzip
'''''''''''''''''''''''''''''
import bz2

userName = b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
password = b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"

uN = bz2.decompress(userName).decode('utf-8')
pw = bz2.decompress(password).decode('utf-8')

print(uN)
print(pw)