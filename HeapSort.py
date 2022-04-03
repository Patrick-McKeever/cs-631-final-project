import copy
import heapq


def heap_sort(arr):
    """
    Implementation of heapsort using python heapq library. Does not alter original array,
    returns sorted array instead.
    :param arr: The array to sort, not altered by function.
    :return: A sorted version of the array.
    """
    # Create heap containing elements of array - O(n).
    h = copy.deepcopy(arr)
    heapq.heapify(h)
    # Continually pop from heap and insert into new list, thereby sorting the original.
    return [heapq.heappop(h) for _ in range(len(arr))]

