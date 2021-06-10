# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'David'
age = 1

# simple concat
print(name + ' is only ' + str(age))

age = 10
# arguments by position
print('{name} is only {age}'.format(name=name, age=age))

# f strings in py 3.6+ -similar to a js `template literal - his dog is {age}`
print(f'my name is {name} and I am {age}')

s = 'this is long boring string for testing different methods'
print(s.capitalize())

# list of string methods here -> https://www.w3schools.com/python/python_ref_string.asp
# examples
# turn string into an array
print(s.split())
# is this a character
print(s.isalpha())
# is it alphanumeric
print(s.isalnum())
# is this a number
print(s.isnumeric())

# capitalize string
print(name.capitalize())
# switch the case
print(name.swapcase())
# get the length
print(len(s))
# get the number of 'x' in a string
findme = 'i'
print(s.count(findme))
# replace in a string5
print(s.replace('i', 'I'))

# find position of a character
print(s.find('d'))
