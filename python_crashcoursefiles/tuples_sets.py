# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# make a tuple
cars = ('Rav-4', 'CRV', 'Hummer', 'Mazda big', 'subaru big')
carz = ('Rav-4')
carz1 = ('Rav-4',)
print(cars, type(cars))
print(carz, type(carz))
print(carz1, type(carz1))

# delete a tuple
del carz1
# print(carz1) -- would return not defined


# A Set is a collection which is unordered and unindexed. No duplicate members.
cars_set = {'Rav-4', 'CRV', 'Hummer', 'Mazda big', 'subaru big'}

# confirm if in a set
print('CRV' in cars_set)

# add to the set
cars_set.add('BMW 5')
print(cars_set)

# FORCING A DUPLICATE - won't add it twice
cars_set.add('BMW 5')
print(cars_set)

# remove from set
cars_set.remove('CRV')
print(cars_set)

# clear the entire set
cars_set.clear()
print(cars_set)

del cars_set
