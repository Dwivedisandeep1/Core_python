# def average(a = 9,b = 5):
#     print(f"The average is {int((a+b)/2)}")
#
# average(b=15)

def average(*numbers):
    sum = 0
    for i in numbers:
         sum = sum + i
    return sum/len(numbers)



c = average(4,5,6,8,9)
print(c)

def name(**name):
   print("Hello", name['fname'],name['mname'],name['lname'])

name(fname='sandeep' , mname='Rajesh',lname='Dwivedi')