# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

workers = ['michael', 'pam', 'dwight', 'david', 'stanley']
for labor in workers:
    print(f'this is the cast member: {labor}')


# stop loop with break
for labor in workers:
    if labor == 'dwight':
        break
    print(f'current cast member: {labor}')

# skip with continue
for labor in workers:
    if labor == 'dwight':
        continue
    print(f'current cast member should be: {labor}')

# print with the length of the list except the last two
for i in range(len(workers) - 2):
    print(workers[i])

# while loop - count while it's less than or equal to 3
count = 0
while count <= 3:
    print(f'count {count} + 1')
    count += 1
