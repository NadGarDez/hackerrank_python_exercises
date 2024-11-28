z = 2
x = 1
y = 1
n = 3

z_possible_numbers = range(0,z+1) 
x_possible_numbers =  range(0, x + 1)
y_possible_numbers = range(0, y + 1)

items = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != 3]


print(items)
