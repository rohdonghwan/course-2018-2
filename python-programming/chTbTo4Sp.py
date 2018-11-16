import sys

srcFileName = sys.argv[1]
objFileName = sys.argv[2]


with open(srcFileName,'r') as f:
    
    replaced = f.read()
    print(replaced)
    a = replaced.replace("\t","_"*4)
    print (a)
with open(objFileName,'w') as f:
    print(a)
    f.write(a)

