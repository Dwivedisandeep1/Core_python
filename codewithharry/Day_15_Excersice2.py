import time
timestamp = int(time.strftime('%H'))
print(timestamp)

if (timestamp > 12 and timestamp < 16):
    print('Good Afternoon')
elif (timestamp > 16 and timestamp < 24):
    print('Good Evening')
elif (timestamp > 0 and timestamp < 6):
    print('Good Night')
else:
    print('Good Morning')