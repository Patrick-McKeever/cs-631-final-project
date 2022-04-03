from MergeSort import merge
import random


def chunks(lst, n):
    """
    Generator to split a list into non-overlapping sublists of size n.
    :param lst: The list to split.
    :param n: The size of desired sublists.
    :return: Continually generate sublists of size n from the original list.
    """
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def newsort2(arr):
    """
    Sort an array consisting of pre-sorted blocks by identifying those blocks
    and merging adjacent blocks until no more remain.

    :param arr: The array to sort.
    :return: The sorted array.
    """
    blocks = []
    # Find all pre-sorted blocks in the original array, add to "blocks".
    for i in range(len(arr)):
        if i > 0 and arr[i] >= arr[i-1]:
            blocks[-1].append(arr[i])
        else:
            blocks.append([arr[i]])

    while len(blocks) > 1:
        new_blocks = []
        for block_pair in chunks(blocks, 2):
            # For lists with odd number of elements, there will be a single element left over at the end,
            # resulting in a 1-element block_pair.
            if len(block_pair) == 1:
                break

            # Merge 2 adjacent blocks into a new "back_block".
            block1, block2 = block_pair
            back_block = [0] * (len(block1) + len(block2))
            merge(block1, block2, back_block)
            # Append this new block to the array.
            new_blocks.append(back_block)

        # Now that we're done iterating through it, we can reassign blocks to a version in which
        # all adjacent arrays have been merged.
        blocks = new_blocks

    return blocks[0]

