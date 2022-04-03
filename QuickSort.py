import random


def partition(arr, low, high):
    """
    Implementation of the Hoare partition scheme, in which we partition an array by
    continually swapping elements from the right that are less than the pivot with
    elements from the left that are greater than the pivot until our traversals
    from the left and right meet at the pivot itself.

    :param arr: The array to partition in regards to some pivot, which will be
                pivoted in-place.
    :param low: The lower index of the array range to pivot.
    :param high: The upper index of the array range to pivot.
    :return: The final index of the pointer advancing from the right (i.e. the
             position chosen as pivot).
    """
    pivot = arr[random.randint(low, high)]
    i, j = low - 1, high + 1

    while True:
        # Move i (left index) to right until you find an element greater than or equal to
        # the pivot.
        i += 1
        while arr[i] < pivot:
            i += 1

        # Move j (right index) to left until you find an element less than or equal to
        # the pivot.
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # Once the pointer advancing from the left meets the one advancing from the right,
        # we're done.
        if i >= j:
            return j

        # We know that j is the index of an element less than the pivot with a greater index
        # and i is the index of an element greater than the pivot with a lesser index. Since
        # we want elements greater (lesser) than the pivot to have greater (lesser) indices,
        # we can swap these two elements. By doing this continuously until the pivots meet,
        # it is possible to ensure that all elements to the left of the pivot are less than
        # the pivot and that all elements to the right are greater than it.
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp


def quick_sort(arr, low=0, high=None):
    """
    In-place quicksort of an array using Hoare partitioning.

    :param arr: The array to sort in-place.
    :param low: The lower index of the array that will be sorted.
    :param high: The upper index of the array that will be sorted ("None" for final index).
    """
    # Obviously, we can't assign a default parameter to be the length of the passed array,
    # so we use this simple workaround.
    if high is None:
        high = len(arr) - 1

    if 0 <= low < high and high >= 0:
        # Partition the entire array with some arbitrary pivot.
        p = partition(arr, low, high)
        # Now partition the part of the array to the left of the pivot.
        quick_sort(arr, low, p)
        # As well as the part to the right of the pivot.
        quick_sort(arr, p+1, high)

