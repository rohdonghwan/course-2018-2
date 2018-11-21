string = str(input("문자열을 입력 해 주세요"))
strAry = ([])
curChar = ""
count = 0
for i in string:
    strAry.append(i)
print(len(strAry))
for i in strAry:
    if curChar == i:
        count = count + 1
    else:  
        if count != 0:
            print(curChar,count)
            count = 1
    curChar = i
print(curChar, count)