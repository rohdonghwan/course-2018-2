string = str(input("문자열을 입력 해 주세요"))
strAry = ([])
curChar = ""
count = 0
first = 1
for i in string:
    strAry.append(i)
for i in strAry:
    if curChar == i:
        if count == 0:
            count = count + 2
        else:
            count = count + 1
    else:  
        if count != 0:
            print(curChar,count)
            count = 1
    curChar = i
print(curChar, count)