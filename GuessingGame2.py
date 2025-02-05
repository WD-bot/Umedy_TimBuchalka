import random
highest=10
lowest=1
answer=random.randint(lowest,highest)
#print(answer) #TODO: remove after testing
print("please guess number between 1 and 10: ")
guess=int(input())

#if guess == answer:
    #print("You got it the first time")  # kan også gøres sådan her (slette 12-14)
while guess != answer:
    if guess == answer:
        print("You got it the first time")
        break
    if guess < answer:
        print("Please guess higher")
    else: # guess must be greater than answer
        print("Please guess lower")
    guess=int(input())
    if guess == answer:
        print("Well done, you guessed it")
    #else:
        #print("Sorry you didn't guess it")