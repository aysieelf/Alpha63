def formatted_print(variable):
    width = len(bin(variable)[2:])

    for i in range(1, variable+1):
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexa = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)

        print(f'{decimal} {octal} {hexa} {binary}')

n = int(input())

formatted_print(n)
