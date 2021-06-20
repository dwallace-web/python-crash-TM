# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')
myFile.write('I love to learn')
myFile.close()

# Get some info
print('Name: ', myFile.name)
print('Is Closed : ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)

# Write to file - But this will 'w' (overwrite), not append 'a'
myFile = open('myfile.txt', 'w')
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)
