def solution(A):
    A.sort()
    
    for i in range(len(A)-2):
        if triangle(A, i, i+1, i+2):
            return 1
    
    return 0


def triangle(A, P, Q, R):
    if P >= 0 and P < Q < R and R < len(A):
        if A[P]+A[Q]>A[R] and A[Q]+A[R]>A[P] and A[R]+A[P]>A[Q]:
            return True 
    return False