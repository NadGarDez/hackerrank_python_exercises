'''

The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.
For example:
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i
This prints:
('python', ['awesome', 'language'])
('something-else', ['not relevant'])
In this challenge, you will be given  integers,  and . There are  words, which might repeat, in word group . There are  words belonging to word group . For each  words, check whether the word has appeared in group  or not. Print the indices of each occurrence of  in group . If it does not appear, print .
Example
Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'
For the first word in group B, 'a', it appears at positions  and  in group A. The second word, 'c', does not appear in group A, so print .
Expected output:
1 3
-1
Input Format
The first line contains integers,  and  separated by a space.
The next  lines contains the words belonging to group .
The next  lines contains the words belonging to group .
Constraints



Output Format
Output  lines.
The  line should contain the -indexed positions of the occurrences of the  word separated by spaces.
Sample Input
STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b
Sample Output
1 2 4
3 5
Explanation
'a' appeared  times in positions ,  and .
'b' appeared  times in positions  and .
In the sample problem, if 'c' also appeared in word group , you would print .


'''



# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

d = defaultdict(list)

n, m = input().split()

A = []

B = []

for _ in range(int(n)):
    n_value = input()
    A.append(n_value)

for _ in range(int(m)):
    m_value = input()
    B.append(m_value)


for search in B:
    for index, value in enumerate(A):
        if value == search:
            d[search].append(str(index +1 ))
    if len(d[search]) > 0:
        print(' '.join(d[search]))
    else:
        print('-1')


    # ocurrence_list = [str(index + 1) for index, value in enumerate(A) if value == search]
    # if len(ocurrence_list) > 0:
    #     print(' '.join(ocurrence_list))
    # else:
    #     print('-1'):
