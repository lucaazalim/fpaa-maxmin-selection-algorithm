from typing import List, Tuple

def max_min_select(array: List[int]) -> Tuple[int, int]:
    """
    Finds the maximum and minimum values in an array using the Max-Min Selection algorithm.

    This function serves as the entry point for the Max-Min Selection algorithm, which
    uses a divide-and-conquer approach to efficiently find the maximum and minimum values
    in the given array.

    :param array: A list of integers to find the maximum and minimum values from.
    :return: A tuple containing the maximum and minimum values in the array (max, min).
    :raises ValueError: If the array is empty.
    """
    return _max_min_helper(array, 0, len(array) - 1)

def _max_min_helper(array: List[int], left: int, right: int) -> Tuple[int, int]:
    """
    Helper function for the Max-Min Selection algorithm.

    This function recursively splits the array into halves, finds the maximum and minimum
    values in each half, and then combines the results to find the overall maximum and
    minimum values.

    :param array: A list of integers to find the maximum and minimum values from.
    :param left: The starting index of the current subarray.
    :param right: The ending index of the current subarray.
    :return: A tuple containing the maximum and minimum values in the current subarray (max, min).
    :raises ValueError: If the array is empty.
    """

    if len(array) == 0:
        raise ValueError("Array is empty")

    # Base case: If the subarray has only one element, return it as both max and min.
    if left == right:
        return array[left], array[right]

    # Base case: If the subarray has two elements, return the larger as max and the smaller as min.
    if left == right - 1:
        if array[left] > array[right]:
            return array[left], array[right]
        return array[right], array[left]

    # Recursively split the array into halves and find the max and min in each half.
    mid: int = (left + right) // 2
    max_left, min_left = _max_min_helper(array, left, mid)
    max_right, min_right = _max_min_helper(array, mid + 1, right)

    # Combine the results to find the overall max and min.
    return max(max_left, max_right), min(min_left, min_right)