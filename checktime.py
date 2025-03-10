from exercise32 import continuous_spaces
from exercise33 import walk_matrix
from exercise34 import continuous_0
import time

arr = ['010101','101010', '010101']

begin_a = time.time()
print(continuous_spaces(arr))
end_a = time.time()

print(f'first aproach time: {begin_a - end_a:.10f} segundos.')


begin_b = time.time()

print(walk_matrix(arr))

end_b = time.time()


print(f'second aproach time: {begin_b - end_b:.10f} segundos')


begin_c = time.time()

print(continuous_0(arr))

end_c = time.time()


print(f'last aproach time: {begin_c - end_c:.10f} segundos')


