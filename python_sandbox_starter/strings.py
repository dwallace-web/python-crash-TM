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
print(s.split())
print(s.isalpha())
