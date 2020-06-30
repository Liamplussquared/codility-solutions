def solution(A):
    A.sort()
    
    if(len(A) < 3):
        return 0
        
    return max(A[-1]*A[-2]*A[-3], A[0]*A[1]*A[-1])