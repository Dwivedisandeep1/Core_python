with open("myfile.txt",'w') as f:
    # print(type(f))
    #
    # f.seek(10)
    # print(f.tell())
    #
    # data = f.read(5)
    # print(data)

    f.write('Hello World!')
    f.truncate(5)
    print(f)

with open('myfile.txt' , 'r') as f:
    print(f.read())