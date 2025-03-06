arr = ['01010','00000','11111', '00000']

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


def relation_search(relations, groups):
    index = None
    for relation in relations:
        index = find_group(relation, groups)
        if index != -1:
            return index
    return index

def continous_spaces(str_arr):
    matrix = [list(x) for x in str_arr]
    holes = [(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == '0']
    groups = []
    for indexHole, hole  in enumerate(holes):
        relations = []
        rest = [value for index, value in enumerate(holes) if index != indexHole]
        for i in rest:
            if analize(hole, i) == True:
                relations.append(i) 
        working_index = relation_search(relations,groups) 
        print(groups)
        if working_index == -1:
            groups.append([hole])
        else:
            groups[working_index].append(hole)

    
    print(len(groups))
continous_spaces(arr)
