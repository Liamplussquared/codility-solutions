def solution(X, A):
    positions = set()
    
    for i in range(len(A)):
        leaf = A[i]
        positions.add(leaf)
        
        if len(positions)==X:
            return i
            
    return -1