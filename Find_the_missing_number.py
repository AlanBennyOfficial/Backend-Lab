lst = [1,2,4,5]

# n*(n+1)//2        n = length of list + 1 

def missing_no(lst):   
    n = len(lst)+1
    print((n*(n+1)//2)-sum(lst))

missing_no(lst)   
