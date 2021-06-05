# A variable is a container for a value, which can be of various types
'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes

VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one,
  - no semi colon needed
'''
x = 10  # int
y = 2.5  # floating number
z = 'Dave'  # string
is_active = True  # boolean - T or F must be capitalized or it will be a variable instead of  boolean value
print(x, y, z, is_active)

# assign multiple values
x, y, z, is_active = (20, 2.1, 'Ron', False)
print(x, y, z, is_active)

# simple matth
a = x + y
print(a)
# type of test
print(type(x))
# casting - turn value into a string
x = (str(x))
print
# type of test
print(type(x))
