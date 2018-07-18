name = ['annie', 'sophie', 'sarah', 'maxwell', 'jake', 'alex','justin']
last = ['anderson', 'smith', 'rhodes', 'hu']
#last name
from random import randint
random_2 = randint (0,len(last))
#first name
from random import randint
random = randint(0,len(name))

print(name[random]); print(last[random_2])
