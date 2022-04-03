import random
import time
from collections import defaultdict
from functools import reduce

from HeapSort import heap_sort
from InsertionSort import insertion_sort
from MergeSort import merge_sort
from NewSort import newsort2
from QuickSort import quick_sort


def createRandomArray(n, lower_bound=0, upper_bound=1000):
    """
    Create an array populated by n random elements.
    :param n: The length of the array.
    :param lower_bound: The min value for an element.
    :param upper_bound: The max value for an element.
    :return: The array itself.
    """
    return [random.randint(lower_bound, upper_bound) for _ in range(n)]


def createRandomBlockArray(k, size=5000, lower_bound=0, upper_bound=1000):
    """
    Create an array populated by n random elements.
    :param k: The length of presorted blocks in the array.
    :param size: The length of the array.
    :param lower_bound: The min value for an element.
    :param upper_bound: The max value for an element.
    :return: The array itself.
    """

    # If the largest size of any given block is 1, then that means no element is
    # less than the next; this means the list must be in reverse-sorted order.
    if k == 1:
        return list(reversed(sorted([random.randint(lower_bound, upper_bound)
                                     for _ in range(lower_bound, upper_bound)])))

    arr = []
    previous_upper = upper_bound
    while len(arr) < size:
        # We need to ensure that at least one value in the array is less than the upper bound
        # of the previous block, so we select one element from [lower, max(previous_block)]
        # before selecting the remaining k-1 elements. This element may not even be the min-
        # imimum of the new block, but we need to ensure that there's no possibility that
        # this block's first element is greater than or equal to the last element of the
        # previous range.
        arr += sorted([random.randint(lower_bound, previous_upper)] +
                      [random.randint(lower_bound, upper_bound) for _ in range(k-1)])

        previous_upper = arr[-1]

    return arr


def is_sorted(l):
    """
    Is a list sorted or not?
    :param l: The list to test.
    :return: Whether or not its elements are ordered from least to greatest.
    """
    return all(l[i] <= l[i+1] for i in range(len(l) - 1))


def test_funcs(block_generator, block_gen_params):
    """
    Test the various sorting functions on arrays generated from the given generator.
    :param block_generator: A function which, when passed params from block_gen_params,
                            produces arrays to be sorted.
    :param block_gen_params: A list of parameters to be passed to block_generator; may
                             be either a list of elements (in the case where only one
                             parameter should be passed) or a list of lists of parameters
                             (in the case where multiple parameters must be passed.
    :return: A dictionary mapping function names to the average time (in seconds) they
             took to execute.
    """
    funcs = {
        'heap_sort': heap_sort,
        'insertion_sort': insertion_sort,
        'merge_sort': merge_sort,
        'new_sort': newsort2,
        'quick_sort': quick_sort
    }
    times = defaultdict(lambda: defaultdict(list))
    iterations = 20

    for i in range(iterations):
        print('Iteration %d of %d:' % (i, iterations))
        for param_set in block_gen_params:
            # Allow either 1d or 2d params list.
            first_param = param_set[0] if type(param_set) is list else param_set

            print('\tTesting length/k = %d.' % first_param)
            for name, func in funcs.items():
                # Generate array to be sorted.
                arr = block_generator(param_set if type(param_set) is list else first_param)

                # If sorting func is not in-place, reassign arr to the output of func.
                if name in ['heap_sort', 'new_sort']:
                    start = time.time()
                    arr = func(arr)
                    end = time.time()
                else:
                    start = time.time()
                    func(arr)
                    end = time.time()

                if not is_sorted(arr):
                    print("[ERROR] %s failed to sort properly. Exiting now." % name)
                    exit(1)

                times[name][first_param].append(end - start)

    # Get average time for each function.
    avg_times = {}
    for func_name, len_times in times.items():
        print(func_name)
        for length, ex_times in len_times.items():
            avg_time = reduce(lambda a, b: a + b, ex_times) / len(ex_times)
            avg_times[func_name] = avg_time
            print('\t%d\t\t: %s seconds' % (length, avg_time))

    return avg_times


if __name__ == "__main__":
    avg_times_rand_arr = test_funcs(createRandomArray, [10, 100, 1000, 10000, 100000, 1000000])
    avg_times_block_arr = test_funcs(createRandomBlockArray, [1, 20, 100, 500, 1000, 5000])

