LOW = 1
HIGH = 56473

# print("Please think of a number between 1 and 1000")
# input("Press ENTER to start")


def guess_binary(answer, low, high):
    guesses = 1
    while True:
        # print("\tGuessing in the range {} to {}".format(low, high))
        guess = low + (high - low) // 2
        # high_low = input("My guess is {}. Should I guess higher or lower? Enter h or l, or c if my guess was correct."
        #                  .format(guess)).casefold()

        # if high_low == "h":
        if guess < answer:
            # I have to guess higher.  The low end of the range becomes 1 greater than the guess.
            low = guess + 1
        # elif high_low == "l":
        elif guess > answer:
            # I have to guess lower.  The high end of the range becomes 1 less than the guess.
            high = guess -1
        # elif high_low == "c":
        elif guess == answer:
            # print("I got it in {} guesses!".format(guesses))
            # break
            return guesses
        # else:
        #     print("Please enter h, l or c")

        guesses += 1
# one=0
# two=0
# three=0
# four=0
# five=0
# six=0
# seven=0
# ate=0
# nine=0
# ten=0
# eleven=0

correct_count=0
max_guesses=0
for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print("{} guessed in {}".format(number, number_of_guesses))
    # if number_of_guesses ==1:
    #     one+=1
    # if number_of_guesses ==2:
    #     two+=1
    # if number_of_guesses ==3:
    #     three+=1
    # if number_of_guesses ==4:
    #     four+=1
    # if number_of_guesses ==5:
    #     five+=1
    # if number_of_guesses ==6:
    #     six+=1
    # if number_of_guesses ==7:
    #     seven+=1
    # if number_of_guesses ==8:
    #     ate+=1
    # if number_of_guesses ==9:
    #     nine+=1
    # if number_of_guesses ==10:
    #     ten+=1
    # if number_of_guesses ==11:
    #     eleven+=1
    if number_of_guesses > max_guesses:
        max_guesses,correct_count=number_of_guesses,1
    elif number_of_guesses==max_guesses:
        correct_count+=1
print("I guessed without being told {} times. Max {} guesses."
      .format(correct_count,max_guesses))


# print("1:", one)
# print("2:", two)
# print("3:", three)
# print("4:", four)
# print("5:", five)
# print("6:", six)
# print("7:", seven)
# print("8:", ate)
# print("9:", nine)
# print("10:", ten)
# print("11:", eleven)


def sum_numbers(n1+n2):
    """
    """

