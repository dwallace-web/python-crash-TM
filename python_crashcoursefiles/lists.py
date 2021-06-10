# A List is a collection which is ordered and changeable. Allows duplicate members.

# create list
numbers = [2, 4, 6, 7, 8, 42]

# constructors
numberZ = list((1, 2, 3, 4, 5, 6))

print(numbers, numberZ)

# cars
cars = ['mustang', 'tesla', 'prius', 'volt', 'f150', 'revian']
# get the f150
print(cars[4])
# get the length of the list
print(len(cars))

# append to the end
cars.append('Model 3')
print(cars)

# add to the beginning
cars.insert(0, 'Tesla Roadster')
print(cars)

# remove from the list
cars.pop(2)
print(cars)

# insert into the list
cars.insert(3, 'Hummer EV')
print(cars)

# reverse the list
cars.reverse()
print(cars)

# alphabetize the list
cars.sort()
print(cars)

# reverse the list
cars.sort(reverse=True)
print(cars)

# change 4th item in the list into BOLT
cars[3] = 'BOLT'
print(cars)

# alphabetize the list 2 intentional
cars.sort()
print(cars)
