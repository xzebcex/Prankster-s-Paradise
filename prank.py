# Prankster's Paradise

while True:  # Main loop.
    response = input(
        'Do you want to know.\nHow to keep a gullible person busy for hours? Y/N: ')

    if response.lower() == 'no' or response.lower() == 'n':
        break  # If no break out of this loop.

    if response.lower() == 'yes' or response.lower() == 'y':
        continue  # If yes continue to the start of this loop.

    print('"{}" is not a valid yes/no reponse.'.format(response))

print('Have a nice day!')
