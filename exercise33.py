def analize(current_hole, next_hole):
    ci, cj = current_hole

    ni, nj = next_hole

    return ((ni, nj) == (ci, cj + 1) or (ni, nj) == (ci, cj - 1) or ((ni, nj) == (ci + 1, cj) ) or ((ni, nj)==(ci -1 , cj))) 

def find_group(item, groups):
    for index, group in enumerate(groups):
        #print('item-> ',item, ' group-> ', groups)
        if item in group:
            return index

    else:
        return -1


def is_position_valid(position, string_arr):
    row, column = position
    if row < 0 or column < 0:
        return False
    try:
        if string_arr[row][column] == '0':
            return True
        else:
            return False
    except:
        return False

def recursive_visit(item, prev,string_arr, groups):
    position = item
    if is_position_valid(position, string_arr) == True and find_group(position, groups)==-1:
        if len(groups) == 0:
             groups.append([position])
        else:
            working_index = find_group(prev, groups)
            if working_index > -1:
                groups[working_index].append(position)
            else:
                groups.append([position])

        recursive_visit((position[0] + 1, position[1]), item, string_arr, groups)
        recursive_visit((position[0] - 1, position[1]), item, string_arr, groups)
        recursive_visit((position[0] , position[1] + 1), item, string_arr, groups)
        recursive_visit((position[0] , position[1] - 1), item, string_arr, groups)

def walk_matrix(string_arr):
    groups = []
    for row in range(len(string_arr)):
        for column in range(len(string_arr[0])):
            recursive_visit((row, column),(-1,-1), string_arr, groups)

    return len(groups)



