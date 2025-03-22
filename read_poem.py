
with open('hungrydane.txt',encoding='utf-8') as hungry:
    for line in hungry:
        print(line.rstrip())
        # if 'eyes' in line.casefold(): # finds the line for a object easier
        #     break
