# 1. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty 
# tuples

# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
t = [(2, 3), (1, 5), (4, 4), (3, 2), (2, 1)]
l = len(t) 
for i in range(0, l):     
    for j in range(0, l-i-1): 
        if (t[j][-1] > t[j + 1][-1]): 
            c = t[j] 
            t[j]= t[j + 1] 
            t[j + 1]= c
print(t)