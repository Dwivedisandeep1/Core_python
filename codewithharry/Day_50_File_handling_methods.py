f = open('myfile.txt','r')
i = 0
while True:
    i = i+1
    line = f.readline()
    if not line:
        print(line, type(line))
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"Marks for student {i} in maths is: {m1}")
    print(f"Marks for student {i} in Science is: {m2}")
    print(f"Marks for student {i} in SST is: {m3}")
