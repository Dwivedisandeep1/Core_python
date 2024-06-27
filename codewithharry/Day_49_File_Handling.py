f = open('myfile.txt','w',encoding='latin1')
print(f)

f.write('Hello World!')
print(f)
f.close()