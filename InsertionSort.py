def insertion_sort(arr):
    """
    Insertion sort implementation using an array. This is the implementation suggested
    on page 214 of textbook. Other implementations (including one with a priority queue)
    are described elsewhere in the textbook, but this one has the benefits of being
    in-place and not requiring the implementation of a priority queue class.

    :param arr: An array that will be sorted in-place.
    """

    # For each element in the list, move it backwards until it is less than all
    # subsequent elements. This is O(N^2), since we perform the O(N) inner while
    # loop for every element of the list save the first.
    for ind in range(1, len(arr)):
        el = arr[ind]
        j = ind - 1

        # Shift all elements one to the right until you find the correct position
        # off el. This is O(N), since we must iterate through all array positions
        # in the worst case.
        while j >= 0 and arr[j] > el:
            arr[j+1] = arr[j]
            j -= 1

        # Then place el in its correct position.
        arr[j+1] = el

