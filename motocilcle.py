# Changing an element in a list

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#Appeding or Adding a new item to the end of the list.
motorcycles.append("Kasynsky")
print(motorcycles)

#names Family with append
family = []

family.append('Thalita')
family.append('Angelina')
family.append('Ricardo')
family.append("Nicolas")
family.append("Maria")

print(family)

#Insert an item in a list

family.insert(1, "Antonio")
family.insert(2, "Antonio")

print(family)

#Remove an Item in a List

del family[2]
print(family)