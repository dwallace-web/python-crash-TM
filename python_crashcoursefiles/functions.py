# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# create simple function

def sayGoodbye(name):
    print(f'Goodbye, until next time {name} ......' + name)


sayGoodbye('Jonathan Doe')

# return values


def getSum(num1, num2, num3):
    # function scope
    total = num1 + num2 + num3
    return total


print(getSum(1, 1, 2))

num = getSum(2, 2, 2)
print(num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions
# built like a arrow function
# this is a lamda function
# findSum = lambda num4, num5 : num4 + num5


def findSum(num4, num5): return num4 + num5


print(findSum(10, 3))
