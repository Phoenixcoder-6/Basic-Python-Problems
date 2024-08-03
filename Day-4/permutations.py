from itertools import permutations
def find_permutation(string):
    per= permutations(string)
    return per

string=input()
res= permutations(string)
per_list=list(res)
print(per_list)
count=len(per_list)
print(count)