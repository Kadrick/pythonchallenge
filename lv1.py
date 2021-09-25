'''''''''''''''''''''''''''''
> Filename: lv1.py
> Author: Kadrick, BoGwon Kang
> Created at: -
> Description: String
'''''''''''''''''''''''''''''
def findKey(input):
    for i in range(0, len(input)):
        if input[i] == " ":
            if input[i - 1] == ".":
                print("")
            output = input[i]
        elif ord("a") <= ord(input[i]) <= ord("z"):
            src = ord(input[i]) - ord("a")
            dest = (src + 2) % 26;
            output = chr(dest + ord("a"))
        else:
            output = input[i]
        print(output, end="")

def adjustMethod(input, srcTable, destTable):
    transTable = str.maketrans(srcTable, destTable)
    return input.translate(transTable)
       
statement = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print("by loop")
findKey(statement)
print("")
findKey("map")

src = dest = ""
for i in range(0, 26):
    src += chr(i + ord("a"))
    dest += chr((i + 2)  % 26 + ord("a"))

print("")
print("by string.maketrans()")
print(adjustMethod(statement, src, dest))
print(adjustMethod("map", src, dest))