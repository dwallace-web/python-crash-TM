# If/ Else conditions are used to decide to do something based on something being true or false

x = 48
y = 10

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

if x > y:
    if x <= 100:
        print(f'{x} is less than 100')
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')


# Logical operators (and, or, not) - Used to combine conditional statements

if x > 2 and x <= 50:
    print(f'{x} is greater than 2 and less than 50')

if not (x == y):
    print(f'{x} is not equal to {y}')


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1, 2, 5, 3, 40, 41, 47, 3,  10]
# not in - returns true
if x not in numbers:
    # return true or false
    print(x not in numbers)

# in -  returns true
if y in numbers:
    # return true or false
    print(y in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
