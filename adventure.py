available_exit=["N","S","E","W"]
chosen_exit=""
while chosen_exit not in available_exit:
    chosen_exit=input("Please choose a direction: ").casefold()
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break
    else:
        print("Aren't you glad you got out of there")
