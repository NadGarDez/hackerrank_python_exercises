figure = '.|.'

N = 27

M = 9


def get_max_levels():
    return (M - 1) / 2

def triangle():
    for i in range(1, int(get_max_levels()) + 1):
        word = ''
        if i == 1:
            word = figure
        else: 
            times = (2*i) -1
            word = figure * times

        print(word.center(21, '-'))

def invert_triangle():
    a = int(get_max_levels())
    for i in range(1, a + 1):
        times = (2*a) - (2 * i - 1)
        word = figure * times
        print(word.center(21, '-'))
        



triangle()
print('WELCOME'.center(N, '-'))
invert_triangle()
