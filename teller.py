choise = 'j'
while choise.lower() == 'j':
    try:
        teller = 5
        noemer = int(input('Geef noemer: '))
        resultaat = teller / noemer
    except ZeroDivisionError as e:
            print('Fout 1: ', e)
    except ValueError as e:
            print('Fout 2 :', e)
    else:
            print(teller, '/', noemer, '=', resultaat)

    choise = input('\nGeef nog andere invoeren (j/n)?: ')
#
print('\nDaag!')