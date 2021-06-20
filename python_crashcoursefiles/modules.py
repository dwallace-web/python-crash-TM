# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

from validator import validate_email
import validator
from camelcase import CamelCase
import datetime
from datetime import date
import time

import uuid

today = datetime.date.today()
timestamp = time.time()
print(today)
print(timestamp)

created = uuid.uuid4()
print(created)

# check pip installed in terminal - 'pip3 freeze'
generated = CamelCase()
print(generated.hump('hello is it me you are looking for, i can see it....'))
print(timestamp)


# import custom module
email = 'test@testing.com'
if(validate_email(email)):
    print('email is valid')
else:
    print('not a good email address')

email2 = 'test!testing.com'
if(validate_email(email2)):
    print('email is valid')
else:
    print('not a good email address')
