"""
Write a function:
def solution(A)
that, given an array A consisting of N integers, returns the maximum sum of any slice of A.
"""


def solution(A):
    return get_max_slice(A)

def get_max_slice(A):
    max_ending, max_slice = -10000000000, -10000000000
    for a in A:
        max_ending = max(a, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice