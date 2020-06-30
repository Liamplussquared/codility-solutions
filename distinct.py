def solution(A):
    exclusive = set()
    for a in A:
        exclusive.add(a)
    return len(exclusive)
