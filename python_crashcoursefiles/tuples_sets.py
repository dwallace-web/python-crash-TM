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
