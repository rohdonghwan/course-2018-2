import re

data = """
park@naver.com
kim@daum.net
lee@myhome.co.kr
"""

dat = re.compile(".*[@].*[.](?:com$|net$).*$")

data2 = """
kim,fail,fail
shin,pass,fail
"""

dat2 = re.compile("(\w{3})[,](\w{4})[,](\w{4})")
print(dat2.sub("\g<1>,\g<2>,pass",data2))

dat2 = re.compile("fail$",re.MULTILINE)
print(dat2.sub('pass',data2))