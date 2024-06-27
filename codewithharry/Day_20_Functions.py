# a = 9
# b = 8
#
# gmean = a*b/a+b
# print(gmean)
#
# c = 8
# d = 7
# gmean2 = (c*d)/(c+d)
# print(gmean2)
a = 9
b = 8


def calculategmean(a, b):
    mean = (a * b) / (a + b)

    print(mean)


def greater(a, b):
    if a > b:
        print(f"{a} is greater than {b}")
    elif b > a:
        print(f"{b} is greater than {a}")
    else:
        print(f"{a} and {b} are Equal")

def lesser(a , b):
    pass


calculategmean(a, b)
greater(a, b)
