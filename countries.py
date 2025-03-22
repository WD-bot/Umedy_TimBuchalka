
input_filename = 'country_info.txt'

countries={}

with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        while len(data) < 7:
            data.append("") # Fyld eventuelle manglende felter med en tom streng ("")

        country, capital, code, code3, dialing, timezone, currency=data
        # print(country, capital, code, code3, dialing, timezone, currency, sep ='\n\t')

        country_dict = {
            'name':country,
            'capital':capital if capital else "No registered capital",
            'country_code':code,
            'cc3':code3,
            'dialing_code':dialing if dialing else "No dialing code",
            'timezone':timezone if timezone else "No timezone data",
            'currency':currency if currency else "No registered currency"
        }
        #print(country_dict)
        # Gem både landets navn og landekode som nøgle (case-insensitive)
        countries[country.casefold()]=country_dict
        # code_lookup[code.casefold()]=country
        countries[code.casefold()]=country_dict

while True:
    chosen_country= input("Please enter the name of a country: ")
    country_key=chosen_country.casefold()
    if country_key == 'quit':
        break
    elif country_key in countries:
        country_data=countries[country_key]
        capital = country_data['capital']
        print(f"The Capital of {chosen_country} is {capital}")
    else:
        print(f"Sorry, '{chosen_country}' was not found in the database.")