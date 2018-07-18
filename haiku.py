five1 = ['i like your hat', 'you are beautiful', 'you have a large neck']
seven = ['it is a very cute one', 'you shine like a shooting star', 'it is very big on you']
five2 = ['I wish i had one', 'shine bright today please', 'please make it smaller']
#five1
from random import randint
random1 = randint (0,len(five1))
#seven
from random import randint
random2 = randint(0,len(seven))
#five2
from random import randint
random3 = randint (0,len(five2))

print(five1[random1])
print(seven[random2])
print(five2[random3])
