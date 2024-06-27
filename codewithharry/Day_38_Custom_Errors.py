a = (input("Enter any value between 5 and 9: "))

if a == 'quit':
    pass
elif a < 5 or a > 9:
    raise ValueError('Value Should be between 5 or 9 ')

print(a)


# Defining Custom Exceptions
#
# class