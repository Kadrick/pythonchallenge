'''''''''''''''''''''''''''''
> Filename: lv10.py
> Author: Kadrick, BoGwon Kang
> Created at: 2021/10/14 15:52
> Description: Look and say sequence
'''''''''''''''''''''''''''''
def lookSay(input:str) -> str:
    output = ""
    sz = 1
    before = input[0]
    idx = 1

    while idx < len(input):
        if before != input[idx]:
            output += str(sz)
            output += before
            before = input[idx]
            sz = 1
        else:
            sz +=1
        idx += 1;
    
    output += str(sz)
    output += before
    
    return output

arr = "1"
for idx in range(0, 31):
    print(idx, ":", len(arr))
    arr = lookSay(arr)
