# Used for string formatting

letter  = "Hey my name is {} and I am from {}"
country = "India"
name = "Sandeep"

# print(letter.format(name , country))
print(f'Hey my name is {{name}} and i am from {{country}}')
price = 49.5554
txt = f'for only {price: 0.2f} dollars!'
print(txt)

print(f"{2*30}")