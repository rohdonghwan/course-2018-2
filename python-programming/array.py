import numpy as np

print("<배열에서의 불 표현>")
dirty = np.array([9,4,1,-0.01,-0.02,-0.001])
whos_dirty = dirty<0
print(whos_dirty)
dirty[whos_dirty] = 0
print(dirty)
print(" ")

print("<논리 연산자로 불 표현 결합>")
linear = np.arange(-1, 1.1, 0.2)
print((linear <= 0.5)&(linear >= -0.5))
print(linear)
print(" ")

print("<배열에서의 벡터 연산>")
a = np.arange(4)
b = np.arange(1,5)
print(a)
print(b)
print(a+b)
print(a*b)
print(" ")

