import string
number = 1
work_list = string.ascii_lowercase[:number]



def center_section():
    center = work_list[0]
    right = '-'.join(list(work_list[1:]))
    left = right[::-1]
    print(f'{left}-{center}-{right}')


def bottom_section():
    for i in range(1,number):
        local_list = work_list[i:]
        center = local_list[0]
        right = '-'.join(list(local_list[1:]))
        left = right[::-1]
        print(f'{left}-{center}-{right}'.center(number * 4 -3, '-'))

def top_section():
    for i in reversed(range(1,number)):
        local_list = work_list[i:]
        center = local_list[0]
        right =  '-'.join(list(local_list[1:]))
        left = right[::-1]
        print(f'{left}-{center}-{right}'.center(number * 4 -3, '-'))

top_section()
center_section()
bottom_section()
