def greet_pythons(items: list)-> None:
    greeting = 'Hi'
    print(f'The ID of `greeting` in `greet_pythons`is{id(greeting)}')
    print(f'Local namespace in `greet_pythons´(1): {locals()}')

    def make_greeting(item:str)-> str:
        # nonlocal greeting #overwrites 
        print(f'Local namespace in `make_pythons´(1): {locals()}')
        greeting='Hello'
        print(f'The ID of `greeting` in `make_pythons`is{id(greeting)}')
        return f'{greeting} {item}'


    for item in items:
        # greeting='Hey'
        print(make_greeting(item))
    print(f'The Inside `greet_pythons`is {greeting}')
    print(f'The ID of `greeting` in `greet_pythons`is{id(greeting)}')
    print(f'Local namespace in `greet_pythons´(1): {locals()}')

names= ['Olivia', 'Alexander','Lasse', 'Marie', 'Julie']

greet_pythons(names)