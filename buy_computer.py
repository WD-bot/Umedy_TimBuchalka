current_choice="_"
computer_parts= [] #makes an empty list
total_cost=0

availiable_parts=["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "webcam",
                  "hdmi cable",
                  "dvd drive",
                  "disk"]
price_part=[200,100,25,15,25,5,30,30] #price of parts

# Generate valid choices dynamically
valid_choices = [str(i) for i in range(1, len(availiable_parts)+1)]

#valid_choices = []
for i in range(1, len(availiable_parts) + 1):
    valid_choices.append(str(i)) # makes the output a string
availiable_parts.sort()
while current_choice !='0':
    if current_choice in valid_choices:
        index=int(current_choice)-1
        chosen_parts = availiable_parts[index]
        chosen_price = price_part[index] #adds in the price

        if chosen_parts in computer_parts:
            #its already in, so remove it
            print("Removing {} for ${}".format(current_choice,chosen_price))
            computer_parts.remove(chosen_parts)
            total_cost -= chosen_price  # Subtract the price from total cost
        else:
            print("Adding {} for ${}".format(current_choice,chosen_price))
            computer_parts.append(chosen_parts)
            total_cost += chosen_price  # Add the price to total cost
        print("Your lists now contains {0}".format(computer_parts))
        print("Total cost so far: ${}".format(total_cost))
    else:
        print("Please add options from the lists below")
        for number, (part,price) in enumerate(zip(availiable_parts, price_part), start=1):
            print("{0}: {1}, ${2}".format(number +1 ,part, price))
        print("Print 0 to finish")
    current_choice= input()


print("Your final selection contains:")

for part in computer_parts:
    index = availiable_parts.index(part)
    price = price_part[index]
    print("{0}: ${1}".format(part,price))

print("Total cost: ${0}".format(total_cost))


# Samlet pris opdatering:
    # Når en del tilføjes (computer_parts.append(chosen_part)), lægges dens pris (total_cost += chosen_price) til.
    # Når en del fjernes (computer_parts.remove(chosen_part)), trækkes dens pris fra (total_cost -= chosen_price).
# Visning af samlet pris:
    # Den samlede pris (total_cost) vises hver gang brugeren tilføjer eller fjerner en del.
# Afsluttende opsummering:
    # Når brugeren afslutter med valg, udskrives den samlede pris sammen med listen over valgte dele.