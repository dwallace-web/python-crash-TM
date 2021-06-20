# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# class
class User:
    # constructor - function that runs to instantiate the object from a class
    def __init__(self, name, email, userid, age):
        self.name = name
        self.email = email
        self.userid = userid
        self.age = age

    def salutation(self):
        return f'My name is {self.name} and my email is {self.email}. See ya later!'

    def has_bday(self):
        self.age += 1


# init the object
Michael = User('Michael Scott', 'michael@dundermiflin.com', 4, 45)
print(Michael.email)
print(Michael.userid)
print(Michael.age)
Michael.has_bday()
print(Michael.age)
print(Michael.salutation())


# extend class -> similar to es6 in js, but this is passed as a parameter
class Boss(User):
    # constructor
    def __init__(self, name, email, userid, age):
        self.name = name
        self.email = email
        self.userid = userid
        self.age = age

    def set_balance(self, balance):
        self.balance = balance

    def salutation(self):
        return f'My name is {self.name} and my email is {self.email}. My balance is {self.balance}. See ya later!'


# init boss
stanley = Boss('Stanley', 'stanley@dundermiflin.com', 3, 35)
stanley.set_balance(500000)
print(stanley.salutation())
