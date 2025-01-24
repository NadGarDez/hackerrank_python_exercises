def print_line(number, padding):
    dec_number = str(number)
    bin_number = str(bin(number))[2:]
    hex_number = str(hex(number))[2:].upper()
    octal_number = str(oct(number))[2:]
    line = f'{dec_number.rjust(padding, " ")} {octal_number.rjust(padding, " ")} {hex_number.rjust(padding, " ")} {bin_number.rjust(padding, " ")}'
    print(line)

def print_formatted(number):
    padding = len(str(bin(number)[2:]))
    for i in range(1, number + 1):
        print_line(i, padding)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)