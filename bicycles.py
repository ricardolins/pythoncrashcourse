
#Working with lists

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# pull Out the first bicycle in the list

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])


# Add string methods to print a list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

#print 2 items
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1].title())
print(bicycles[3].title())

#Returning the last element in a list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

#put a member od a list in a string and print a string
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."

print(message)

