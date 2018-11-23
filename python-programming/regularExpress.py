import re

phoneNumber = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""
pnbr = re.compile("(\w{3})[-](\w{4})[-](\w{4})")
print(pnbr.sub("\g<1>-\g<2>-####",phoneNumber))

data = """
park@naver.com
kim@daum.net
lee@myhome.co.kr
"""

dat = re.compile(".*[@].*[.](?:com$|net$).*$",re.MULTILINE)
for i in dat.finditer(data):
    print(i.group())


data2 = """
kim,fail,fail
shin,pass,fail
"""

dat2 = re.compile("(\w{3,})[,](\w{4})[,](\w{4})")
print(dat2.sub("\g<1>,\g<2>,pass",data2))

dat2 = re.compile("fail$",re.MULTILINE)
print(dat2.sub('pass',data2))