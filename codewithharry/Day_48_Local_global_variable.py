x = 4
print(x)

def hello():
    global x
    x = 5
    print(x)
    print("Hello Sandeep")

hello()
print(x)