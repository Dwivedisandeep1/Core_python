import os

print("Hello World")
os.system('python --version')

# Match Case System
x = 4
match x:
    # if x is 0
    case 0:
        print('x is Zero')
    case 4:
        print('Case is 4')
    case _ if x!=90:
        print(x)
    case _ if x!=80:
        print(x)