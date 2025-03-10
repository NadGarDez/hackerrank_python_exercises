class UnionFind:
    def __init__(self, elements):
        self.parents = {element: element for element in elements}
        self.ranks = {element: 0 for element in elements }
        

    def find(self, element):
        if element in self.parents.keys():
            if self.parents[element] != element:
                self.parents[element] = self.find(self.parents[element])
            return self.parents[element]

        else:
            raise KeyError

    def union(self, element_a, element_b):
        root_a = self.find(element_a)

        root_b = self.find(element_b)

        if root_a != root_b:
            if self.ranks[root_a] > self.ranks[root_b]:
                self.parents[root_b] = root_a
            elif self.ranks[root_b] > self.ranks[root_a]:
                self.parents[root_a] = root_b
            else:
                self.parents[root_b] = root_a
                self.ranks[root_a] += 1


    def find_roots(self):
        return {self.find(element) for element in self.parents.values()}

    def make_groups(self):
        roots = self.find_roots()
        groups = []
        for root in roots:
            group = [x for x in self.parents.keys() if self.parents[x] == root]
            groups.append(group)
        return groups


def create_relations(position, arr):
    relations = []
    i,j = position
    possibles =  [(i + 1, j),( i - 1, j), (i, j + 1), (i, j - 1)] 
    return [(ni,nj) for ni,nj in possibles if (ni, nj) in arr ]

def continuous_0(arr):
    zeros = [(i,j) for i in range(len(arr)) for j in range(len(arr[0])) if arr[i][j] == '0']
    tool = UnionFind(zeros)
    for position in zeros:
        relations = create_relations(position, zeros)

        for relation in relations:
            tool.union(position,relation)

    return len(tool.find_roots())
    
        
