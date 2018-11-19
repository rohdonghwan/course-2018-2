import os, sys
dirs = os.listdir("C:/Temp/A")
print(dirs)
lists =([])
for i in dirs:
    a = i[-3:]
    
    if a == ".py":
        lists.append(i)        

for i in lists:
    print(i)