string = "Twinkle, twinkle, little star, |How I wonder what you are! |Up above the world so high, |Like a diamond in the sky. |Twinkle, twinkle, little star, |How I wonder what you are"

list = string.split('|')

for i, n in enumerate(list):
    if n[0] == 'H':
        list[i] = f'\n\t{n}'
    elif n[0] == 'U' or n[0] == 'L':
        list[i] = f'\n\t\t{n}'
    elif i == 4:
        list[i] = f'\n{n}'

print(''.join([str(n) for n in list]))
