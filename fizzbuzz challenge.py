
def fizz_buzz(number: int) -> str:
    """
    Playing the game FizzBuzz
    :param number: The number to check
    :return: Fizz, Buzz og number
    """
    if number % 3==0 and number % 5==0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)

#Calculate answer to fizz_buzz(i)
#print response
#calculate answer for player
#get players answer and compare
#repeat till mistake or till 100
#print "congratulations" og "wrong"
print("Play Fizz Buzz. Press ENTER to start")
print()
next_number = 0
while next_number <99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    #players_answer =input("You go")
    players_answer = correct_answer
    if players_answer != correct_answer:
        print("Wrong, you lost, the correct answer was {}".format(correct_answer))
        break
else:
    print("Well done you reached {}".format(next_number))
