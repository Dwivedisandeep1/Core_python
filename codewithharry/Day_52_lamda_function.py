# def double(x):
#     return x * 2

double = lambda x : x*2
cube = lambda x: x**3
print(cube(5))

sum = lambda x,y: x+y

print(sum(3,4))

avg = lambda x , y , z : (x+y+z)/3

print(int(avg(3,5,7)))

def appl(fx , value):
    return 6 + fx(value)


print(appl(cube,2))