"""
Write a function, def solution(A), that given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.
"""

def solution(A):
    if len(A) == 0:
        return -1 
        
    leader = fast_leader(A.copy())
    
    if leader > 0:
        return A.index(leader)
    else:
        return leader
    
    
def fast_leader(arr):
    leader = -1
    arr.sort()
    candidate = arr[len(arr)//2]
    count = 0
    
    for i in range(len(arr)):
        if (arr[i] == candidate):
            count += 1
    
    if count > len(arr)//2:
        leader = candidate
        
    return leader