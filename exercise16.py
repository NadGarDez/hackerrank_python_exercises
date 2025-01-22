tickness = 9
letter = 'H'

import math



def triangle(tickness_number, letter_for_work):
    last_number = 1
    for i in range(tickness_number):
        if i == 0:

            word = letter_for_work
        else :
            repeat_number = last_number + 2
            word = letter_for_work * repeat_number
            last_number = repeat_number
        print(word.center((tickness_number * 2) -1, ' '))


def inver_triangle(tickness_number, letter_for_work):
    last_number = (tickness_number * 2) -1

    for i in range(tickness_number):
        if i == 0:
            word = letter_for_work * last_number
           
        else :
            repeat_number = last_number - 2
            word = letter_for_work * repeat_number
            last_number = repeat_number

        invert = word.center((tickness_number * 2) -1, ' ')
        print(invert.rjust((tickness_number * 6) -1, ' '))



def rectangle_one(tickness_number, letter_for_work):
    for i in range(tickness_number + 1):
        text = letter_for_work * tickness
        column = text.center((tickness_number * 2) -1, ' ')
        print(column +' ' * ((tickness_number * 2) + 1) +column)


def rectangle_two(tickness_number, letter_for_work):
    times = math.ceil(tickness_number / 2)

    for i in range(times):
        word = letter_for_work * (tickness * 5)
        print(word.center((tickness_number * 6) -1, ' '))



triangle(tickness, letter)
rectangle_one(tickness, letter)
rectangle_two(tickness, letter)
rectangle_one(tickness, letter)
inver_triangle(tickness, letter)




