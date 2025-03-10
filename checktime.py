from exercise32 import continous_spaces
from exercise33 import walk_matrix
import time

arr = ['010101','101010', '010101']

begin_a = time.time()
print(continous_spaces(arr))
end_a = time.time()

print(f'first aproach time: {begin_a - end_a:.10f} segundos.')


begin_b = time.time()

print(walk_matrix(arr))

end_b = time.time()


print(f'last aproach time: {begin_b - end_b:.10f} segundos')


