#guess the number.
import random
number=random.randint(1,10) #generate random num
guess=int(input('please guess the number'))
while number != guess:  #! means not equal to.
    guess=int(input("Uffs!!! try again: guess again:"))
else:
    print('Congratulations!!! you are right')
