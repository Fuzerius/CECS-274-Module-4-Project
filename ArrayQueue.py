import numpy as np
from Interfaces import Queue


class ArrayQueue(Queue):
    def __init__(self):
        self.n = 0
        self.j = 0
        self.a = np.zeros(self.n, dtype=object)

    def resize(self):
        """
        helper method; creates a new array that maintains the
        array size invariant and copies the old values making sure to maintain FIFO order.
        """
        # FIXME: Complete this method
        b = np.zeros(max(1, 2 * self.n), dtype=object)
        for i in range(self.n):
            b[i] = self.a[(self.j + i) % len(self.a)]
        self.a = b
        self.j = 0 


    def add(self, x: object):
        """
        adds the given element to the tail of the FIFO queue
        :param x; object type; the element that will be added to the queue
        :return bool type; returns True if the element was successfully added
        """
        # FIXME: Complete this method
        if self.n == len(self.a):
            self.resize()
        self.a[(self.j + self.n) % len(self.a)] = x
        self.n += 1
        

    def remove(self) -> object:
        """
        removes the element at the head of the FIFO queue
        :return object type; returns the element that was removed
        """
        # FIXME: Complete this method
        if self.n <= 0:
            raise IndexError("Queue is empty")
        x = self.a[self.j]
        self.j = (self.j + 1) % len(self.a)
        self.n -= 1
        if len(self.a) >= 3 * self.n:
            self.resize()
        return x


    def size(self):
        """
        gets the current number of elements in the queue
        :return: int type; the number of elements in the queue
        """
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i < self.n - 1:
                s += ","
        return s + "]"

    def __iter__(self):
        """
        makes this ArrayQueue an iterable object
        """
        self.iterator = 0
        return self

    def __next__(self):
        """
        returns the next item in the sequence when iterating over the
        ArrayQueue
        """
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator += 1
        else:
            raise StopIteration()
        return x
