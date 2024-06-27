# Try Except
# a = input("Enter the Number")
#
# print(f"Multiplication table of {a}")
try:
    num = (int(input('Enter an Integer')))
except ValueError:
    print("Number Entered is not an Integer")
except IndexError:
    print('Index Error')
print("Some line of code")