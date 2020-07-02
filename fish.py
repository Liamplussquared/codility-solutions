def solution(A, B):
    stack = []
    count = 0
    for i in range(len(A)):
        if B[i] == 0:
            while len(stack) > 0:
                count += 1
                if stack[-1] > A[i]:
                    break
                else:
                    stack.pop()
        else:
            stack.append(A[i])
  
    return (len(A) - count)