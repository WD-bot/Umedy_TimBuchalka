answer=5
print("please guess number between 1 and 10: ")
guess=int(input())

#if guess < answer:
    #print("Please guess higher")
    ##if guess == answer:
        #print("well done, you guessed it")
    #else:
     #   print("sorry still not right...")
#elif guess > answer:
    #print("Please guess lower")
    #guess=int(input())
    #if guess == answer:
     #   print("well done, you guessed it")
    #else:
     #   print("sorry still not right...")
#else:
   # print("You got it first time")

#if guess != answer:
    #if guess < answer:
       # print("Please guess higher")
   # else: # guess must be greater than answer
       # print("Please guess lower")
   # guess=int(input())
   # if guess == answer:
     #   print("Well done, you guessed it")
   # else:
     #   print("Sorry you didn't guess it")
#else:
    #print("You got it the first time")


if guess == answer:
    print("You got it the first time")
else:
    if guess < answer:
        print("Please guess higher")
    else: # guess must be greater than answer
        print("Please guess lower")
    guess=int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry you didn't guess it")
