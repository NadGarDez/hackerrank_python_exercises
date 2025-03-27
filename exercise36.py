vector  = [-22,1,2,4,3,6]

def find_min_and_max(arr):
    max_number = arr[0]
    min_number = arr[0]
    length = len(arr)
    index = length % 2
        
    while index < length -1:
        if arr[index] > arr[index + 1]:
            local_max = arr[index]
            local_min = arr[index+1]

        else:
            local_max = arr[index + 1]
            local_min = arr[index]

        if local_max  > max_number:
            max_number = local_max
        if local_min< min_number:
            min_number = local_min
        index += 2
        
    return (max_number, min_number)

print(find_min_and_max(vector))
