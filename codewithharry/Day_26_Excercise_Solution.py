import time
hour = int(time.strftime('%H'))
print(hour)

if (0 <= hour < 12):
    print('Good Morning Sir!')
elif(12 <= hour < 17):
    print('Good Afternoon Sir!')
elif 17 <= hour < 0:
    print('Good Night Sir!')