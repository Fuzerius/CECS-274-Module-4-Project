import random
from Interfaces import List


def linear_search(a: List, x: object):
    """
    uses the linear search algorithm to return the index of the given
    element if it is found in the given list; otherwise returns None.
    :param a: List subclass type; an object from a class that implements the List interface
    :param x: object type; the object to search for
    """
    # FIXME: Implement this method
    for i in range(a.size()):
        if a.get(i) == x:
            return i
    return None


def binary_search(a: List, x : object):
    """
    uses the binary search algorithm to return the index of the given
    element if it is found in the given SORTED list; otherwise returns None.
    :param a: List subclass type; an object from a class that implements the List interface
    :param x: object type; the object to search for
    """
    # FIXME: Implement this method
    l = 0
    r = a.size() - 1
    while l <= r:
        mid = (l + r) // 2
        if a.get(mid) == x:
            return mid
        elif a.get(mid) < x:
            l = mid + 1
        else:
            r = mid - 1
    return None


def _merge(a0: List, a1: List, a: List):
    """
    helper function to merge_sort(); merges list a0 and a1 into
    sorted list a
    """
    # FIXME: Implement this method
    i_zero = 0
    i_one = 0
    for i in range(len(a)):
        if i_zero == len(a0):
            a.set(i, a1.get(i_one))
            i_one += 1
        elif i_one == len(a1):
            a.set(i, a0.get(i_zero))
            i_zero += 1
        elif a0.get(i_zero) < a1.get(i_one):
            a.set(i, a0.get(i_zero))
            i_zero += 1
        else:
            a.set(i, a1.get(i_one))
            i_one += 1


def merge_sort(a: list):
    """
    Sorts the given Python list using the merge sort algorithm.
    :param a: list type; a Python list to be sorted
    """
    if len(a) < 2:
        return a

    mid = len(a) // 2
    a0 = a[:mid]
    a1 = a[mid:]

    merge_sort(a0)
    merge_sort(a1)

    # Merge the sorted sublists back into `a`
    i_zero = i_one = i_main = 0

    while i_zero < len(a0) and i_one < len(a1):
        if a0[i_zero] <= a1[i_one]:
            a[i_main] = a0[i_zero]
            i_zero += 1
        else:
            a[i_main] = a1[i_one]
            i_one += 1
        i_main += 1

    # Copy any remaining elements from a0
    while i_zero < len(a0):
        a[i_main] = a0[i_zero]
        i_zero += 1
        i_main += 1

    # Copy any remaining elements from a1
    while i_one < len(a1):
        a[i_main] = a1[i_one]
        i_one += 1
        i_main += 1

    return a


def _partition_f(a :List, start: int, end: int):
    """
    helper function to _quick_sort_f(); partitions a sublist of the given list
    using the first element of the sublist as pivot. The elements of the sublist 
    are arranged into two groups: the first group consists of elements 
    that are less than or equal to the pivot. The second group is
    a group of elements that are greater than the pivot.  By the end of the 
    partitioning process, the pivot is placed in its correct, sorted order,
    elements in the first group appear to the left of the sorted pivot, and 
    elements in the second group appear to the right of the sorted pivot.
    :param a: List subclass type; an object from a class that implements the List interface
    :param start: int type; the index of the first element in the sublist that will be partitioned
    :param end: int type; the index of the last element in the sublist that will be partitioned
    :return: int type; the final index of the pivot element
    """
    # FIXME: Implement this method
    l = start + 1
    r = end
    pivot = a.get(start)
    crossed = False
    while not crossed:
        while l <= r and a.get(l) <= pivot:
            l += 1
        while r >= l and a.get(r) >= pivot:
            r -= 1
        if l < r:
            # Corrected swap logic
            temp = a.get(l)
            a.set(l, a.get(r))
            a.set(r, temp)
        else:
            crossed = True
    temp = a.get(start)
    a.set(start, a.get(r))
    a.set(r, temp)
    return r


def _partition_r(a : List, start, end):
    """
    helper method to _quick_sort_r(); partitions a sublist of the given list
    using a random element in the sublist as pivot. The elements of the sublist
    are arranged into two groups: the first group consists of elements 
    that are less than or equal to the pivot. The second group is
    a group of elements that are greater than the pivot.  By the end of the 
    partitioning process, the pivot is placed in its correct, sorted order,
    elements in the first group appear to the left of the sorted pivot, and 
    elements in the second group appear to the right of the sorted pivot.
    :param a: List subclass type; an object from a class that implements the List interface
    :param start: int type; the index of the first element in the sublist that will be partitioned
    :param end: int type; the index of the last element in the sublist that will be partitioned
    :return: int type; the final index of the pivot element
    """
    # FIXME: Implement this method
    pivot_index = random.randint(start, end)
    # Corrected swap logic
    temp = a.get(start)
    a.set(start, a.get(pivot_index))
    a.set(pivot_index, temp)

    l = start + 1
    r = end
    pivot = a.get(start)
    crossed = False
    while not crossed:
        while l <= r and a.get(l) <= pivot:
            l += 1
        while l <= r and a.get(r) >= pivot:
            r -= 1
        if l < r:
            temp = a.get(l)
            a.set(l, a.get(r))
            a.set(r, temp)
        else:
            crossed = True
    temp = a.get(start)
    a.set(start, a.get(r))
    a.set(r, temp)
    return r


def _quick_sort_f(a: List, start, end):
    """
    helper method to quick_sort(); uses quick-sort with first-element pivot
    to sort a sublist of the given list. 
    :param a: List subclass type; an object from a class that implements the List interface
    :param start: int type; the index of the first element in the sublist
    :param end: int type; the index of the last element in the sublist
    """
    # FIXME: Implement this method
    if start < end:
        pivot_index = _partition_f(a, start, end)
        _quick_sort_f(a, start, pivot_index - 1)
        _quick_sort_f(a, pivot_index + 1, end)


def _quick_sort_r(a: List, start, end):
    """
    helper method to quick_sort(); uses quick-sort with random-element pivot
    to sort a sublist of the given list. 
    :param a: List subclass type; an object from a class that implements the List interface
    :param start: int type; the index of the first element in the sublist
    :param end: int type; the index of the last element in the sublist
    """
    # FIXME: Implement this method
    if start < end:
        pivot_index = _partition_r(a, start, end)
        _quick_sort_r(a, start, pivot_index - 1)
        _quick_sort_r(a, pivot_index + 1, end)


def quick_sort(a: List, p=True):
    """
    sorts the given List using the quick sort algorithm.
    :param a: List subclass type; an object from a class that 
    implements the List interface
    :param p: boolean type; if True, the quick-sort algorithm uses a
              randomly chosen element from a as pivot. 
              Otherwise, uses the first element as pivot.
    """
    if p:
        _quick_sort_r(a, 0, a.size() - 1)
    else:
        _quick_sort_f(a, 0, a.size() - 1)


