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
        
findKey("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
print("")
findKey("map")