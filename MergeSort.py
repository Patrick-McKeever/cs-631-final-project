import random

def merge(S1, S2, S):
    """
    Non-stable merge of items from sorted arrays S1 and S2 into new array S.
    :param S1: A pre-sorted array which will be merged.
    :param S2: A pre-sorted array which will be merged.
    :param S: The output array, which will be used to store the merged version of the
              given arrs.
    """
    # i is index of position in S1, j is index of S2.
    i = j = 0

    # I.e. Until we explore all elements of S1 and S2.
    while i + j < len(S):
        # We know that S1[i] < S1[i+1]. So, we can merge the two by maintaining
        # indices of S1 and S2. If the current element of S1 is smaller than the
        # current element of S2, add it to the output array and move forward one
        # position in S1; and vice versa for S2.
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1


def merge_sort(arr):
    """
    Merge sort of an array, using textbook implementation (Code fragment 12.2, p. 544).
    :param arr: The array to sort in-place.
    """
    # BASE CASE: If array contains a single or no elements, then it is already sorted.
    if len(arr) < 2:
        return

    # RECURSIVE CASE: Split the array in 2, sort each half, then merge sorted halves
    # together.
    mid = len(arr) // 2
    s1 = arr[0:mid]
    s2 = arr[mid:len(arr)]
    merge_sort(s1)
    merge_sort(s2)
    merge(s1, s2, arr)

