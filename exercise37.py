numbers = [3, 3, 3, 3, 3, 5,1]

def rank_calculation(nums,item):
    rank = 1
    for i in nums:
        if item < i:
           rank += 1
    return rank 

def create_ranks(arr):

    ranks = []

    diff_values = set(arr)

    for index, value in enumerate(arr):
        ranks.append(rank_calculation(diff_values,value))
    
    return ranks


print(create_ranks(numbers)) # [2, 2, 2, 2, 2, 1, 3]
