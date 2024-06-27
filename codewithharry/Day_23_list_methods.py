from typing import List

l = [11,45,68,1,2,4,6,1,1,4]
print(l)
# l.append(7)
# l.sort(reverse=True)
l.reverse()
print(l.index(45))
print(l.count(1))
# m = l.copy()
# m[0] = 0
l.insert(1,899)
m = [900,1000,1100]

l.extend(m)
print(l)