s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}

print(s1.union(s2))
print(s1.symmetric_difference(s2))

cities = {"Tokyo", 'Delhi', "Berlin", 'Madrid'}

cities2 = {'Tokyo', 'Seoul', 'Kabul', "Madrid"}
print(cities.isdisjoint(cities2))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities3 = {"Tokyo", "Berlin","Madrid"}
print(cities.issuperset(cities3))
print(cities.pop())