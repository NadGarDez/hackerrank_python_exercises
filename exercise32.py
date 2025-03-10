from functools import reduce

def analize(current_hole, next_hole):
    ci, cj = current_hole

    ni, nj = next_hole

    return ((ni, nj) == (ci, cj + 1) or (ni, nj) == (ci, cj - 1) or ((ni, nj) == (ci + 1, cj) ) or ((ni, nj)==(ci -1 , cj))) 

def create_relations(holes):
    relations = []
    for i in holes:
        filtered = set(filter(lambda x: analize(i, x), holes))
        filtered.update([i])
        relations.append(filtered)

    return relations


def filter_groups(item, groups):
    filtered_relations = []
    indexes = []
    for i in enumerate(groups):
        index, value = i
        if len(item & value) > 0:
            filtered_relations.append(value)
            indexes.append(index)
    return (filtered_relations, indexes)

def combine_relations(relations):
    base = set()
    return set(reduce(lambda x,y: x | y,relations, base ))


def continous_spaces(str_arr):
    holes = [(i,j) for i in range(len(str_arr)) for j in range(len(str_arr[0])) if str_arr[i][j] == '0']
    relations = create_relations(holes)
    groups = [relations[0]]
    for relation in relations:
        filtered_groups, indexes = filter_groups(relation, groups) 
        
        if len(filtered_groups) > 0:
            new_group = combine_relations([relation]+ filtered_groups[:])
            groups[indexes[0]] = new_group
            del_indexes = indexes[1:].copy()
            for i in del_indexes:
                del groups[i]
        else:
            groups.append(relation)

    return len(groups)
