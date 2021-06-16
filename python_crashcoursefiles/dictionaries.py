# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# similar to object literal in JS

# creating a a simple dictionary
person = {
    'first_name': 'Dave',
    'last_name': 'Wallace',
    'company': 'Dunder-Miflin',
    'userID': 30
}

# user constructor
person2 = dict(first_name='Robert', last_name='Williams',
               company='Warner Brothers')

print(person, type(person))
print(person2, type(person2))

# get value
print(person['company'])
print(person2.get('last_name'))

# add a KVP
person['phone'] = '555-666-7777'

# get keys only
print(person.keys())

# get items /values only
print(person.items())

# copy the dictionary - similar to spread object in JS
person3 = person.copy()
person3['city'] = 'Boston'
print(person3)

# remove item from dict
del(person['company'])
person.pop('first_name')

print(person)

# clear - remove everything
person.clear()

print(person)

# get the length - total number of KVPs
print(len(person2))

# list of dictionaries
the_people = [
    {
        'name': 'Miranda', 'age': 40,
    },
    {
        'name': 'Kevin', 'age': 27
    },
    {
        'name': 'Jack', 'age': 50
    }
]
print(the_people)
print(the_people[1]['name'])
print(the_people[2]['age'])
