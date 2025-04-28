import numpy as np
import math
from Interfaces import Queue
from Interfaces import Tree
#import SLLQueue


def left(i: int) -> int:
    """
    helper method; returns the index of the left child of the element at index i
    """
    # FIXME: Replace with your implementation
    return 2 * i + 1


def right(i: int) -> int:
    """
    helper method; returns the index of the right child of the element at index i
    """
    # FIXME: Replace with your implementation
    return 2* (i + 1)

    # Or this one
    # return 2 * i + 2


def parent(i: int) -> int:
    """
    helper method; returns the index of the parent of the element at index i
    """
    # FIXME: Replace with your implementation
    return (i-1) // 2


def _new_array(n: int) -> np.array:
    """
    helper method; creates a new numpy array of 0's of size n
    """
    return np.zeros(n, object)


class BinaryHeap(Queue, Tree):
    def __init__(self):
        self.a = _new_array(1)
        self.n = 0

    def add(self, x: object):
        """
        adds a new element to the binary heap, ensuring that the
        heap invariant parent <= children is maintained
        :param x: object type; the new element
        :returns: boolean type; True if the element was successfully added
        """
        # FIXME: Replace with your implementation
        if self.n == len(self.a):
            self._resize()
        self.a[self.n] = x
        self.n += 1
        self._bubble_up_last()
        return True

    def remove(self):
        """
        removes the smallest element from the heap and returns it
        :returns: object type;
        """
        # FIXME: Replace with your implementation
        if self.n == 0:
            raise IndexError("Heap is empty")
        x = self.a[0]
        self.a[0] = self.a[self.n - 1]
        self.n = self.n - 1
        self._trickle_down_root()
        if self.n * 3 <= len(self.a):
            self._resize()
        return x

    def depth(self, u) -> int:
        """
        returns the depth of element u in the binary heap
        :returns: int type; the number of edges from the root to element u
        """
        # FIXME: Replace with your implementation
        try:
            # Find the index of the element u in the array
            index = self.a.tolist().index(u)
        except ValueError:
            return -1  # Return -1 if the element is not found

        # Calculate the depth based on the index
        return int(math.log2(index + 1))

    def height(self) -> int:
        """
        returns the height of the tree
        :returns: int type
        """
        if self.n == 0:
            return -1  # Return -1 for an empty heap
        return math.floor(math.log2(self.n))

    def bf_order(self) -> list:
        """
        returns a list of the elements in the binary heap as they are traversed
        using Breadth-First order
        :returns: list type;
        """
        # FIXME: Replace with your implementation
        return [self.a[i] for i in range(self.n)]


    def in_order(self) -> list:
        """
        returns a list of the elements in the binary heap as they are traversed
        using in-order traversal
        :returns: list type;
        """
        indices = self._in_order(0)
        return [self.a[idx] for idx in indices]

    def post_order(self) -> list:
        """
        returns a list of the elements in the binary heap as they are traversed
        using post-order traversal
        :returns: list type;
        """
        indices = self._post_order(0)
        return [self.a[idx] for idx in indices]

    def pre_order(self) -> list:
        """
        returns a list of the elements in the binary heap as they are traversed
        using pre-order traversal
        :returns: list type;
        """
        indices = self._pre_order(0)
        return [self.a[idx] for idx in indices]

    def size(self) -> int:
        """
        returns the number of elements in the binary heap
        :returns: int type;
        """
        return self.n

    def get_min(self):
        """
        gets the smallest element in the binary heap without removing it
        :returns: object type;
        """
        # FIXME: Replace with your implementation
        if self.n == 0:
            raise IndexError("Heap is empty")
        return self.a[0]

    def _resize(self):
        """
        helper method; resizes the backing array to twice the
        number of elements, n, or 1 if n = 0.
        """
        a = _new_array(max(1, 2 * self.n))
        for i in range(self.n):
            a[i] = self.a[i]
        self.a = a

    def _bubble_up_last(self):
        """
        helper method to add(x); moves the latest added element
        of the heap to its correct position so that the invariant
        parent <= children is maintained.
        """
        # FIXME: Replace with your implementation
        i = self.n - 1
        p_idx = parent(i)
        while i > 0 and self.a[i] < self.a[p_idx]:
            self.a[i], self.a[p_idx] = self.a[p_idx], self.a[i]
            i = p_idx
            p_idx = parent(i)

    def _trickle_down_root(self):
        """
        helper method to remove(); moves the root of the heap to its correct
        position so that the invariant parent <= children is maintained.
        """
        i = 0
        l_idx = left(i)
        r_idx = right(i)
        while l_idx < self.n:  # Ensure left child exists
            # Determine the index of the smallest element among a[i], a[l_idx], and a[r_idx]
            min_idx = i
            if self.a[l_idx] < self.a[min_idx]:
                min_idx = l_idx
            if r_idx < self.n and self.a[r_idx] < self.a[min_idx]:  # Check if right child exists
                min_idx = r_idx

            if min_idx == i:  # If the current element is already in the correct position
                break

            # Swap the current element with the smallest child
            self.a[i], self.a[min_idx] = self.a[min_idx], self.a[i]

            # Update i to the index of the smallest child
            i = min_idx
            l_idx = left(i)
            r_idx = right(i)

    def _in_order(self, i):
        """
        helper method to in_order(); returns a list of the indices of 
        the elements in the subtree rooted at the element at index i as they are
        traversed using in-order traversal
        :param i: int type; the index of the root of the subtree
        :returns: list type;
        """
        indices = []
        l_idx = left(i)
        r_idx = right(i)
        if 0 <= l_idx < self.n:
            indices.extend(self._in_order(l_idx)) # FIXME: Replace with your implementation
        if 0 <= i < self.n:
            indices.append(i)
        if 0 <= r_idx < self.n:
            indices.extend(self._in_order(r_idx)) # FIXME: Replace with your implementation
        return indices
    
    def _post_order(self, i):
        """
        helper method to post_order(); returns a list of the indices of 
        the elements in the subtree rooted at the element at index i as they are
        traversed using post-order traversal
        :param i: int type; the index of the root of the subtree
        :returns: list type;
        """
        indices = []
        l_idx = left(i)
        r_idx = right(i)
        if 0 <= l_idx < self.n:
            indices.extend(self._post_order(l_idx)) # FIXME: Replace with your implementation
        if 0 <= r_idx < self.n:
            indices.extend(self._post_order(r_idx)) # FIXME: Replace with your implementation
        if 0 <= i < self.n:
            indices.append(i)
        return indices
    
    def _pre_order(self, i):
        """
        helper method to pre_order(); returns a list of the indices of 
        the elements in the subtree rooted at the element at index i as they are
        traversed using pre-order traversal
        :param i: int type; the index of the root of the subtree
        :returns: list type;
        """
        indices = []
        l_idx = left(i)
        r_idx = right(i)
        if 0 <= i < self.n:
            indices.append(i)
        if 0 <= l_idx < self.n:
            indices.extend(self._pre_order(l_idx)) # FIXME: Replace with your implementation
        if 0 <= r_idx < self.n:
            indices.extend(self._pre_order(r_idx)) # FIXME: Replace with your implementation
    
        return indices
    
    def __str__(self):
        """
        returns the string representation of the binary heap array
        :returns: str type;
        """
        return str(self.a[0:self.n])


