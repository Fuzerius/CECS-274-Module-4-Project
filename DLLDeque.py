from Interfaces import Deque
from DLList import DLList
import numpy as np


class DLLDeque(Deque, DLList):
    def __init__(self):
        DLList.__init__(self)

    def add_first(self, x: object):
        """
        adds to the head of the list the element x
        :param x: object type; the new element
        """
        self.add(0, x)

    def add_last(self, x: object):
        """
        adds to the tail of the list the element x
        :param x: object type; the new element
        """
        # FIXME: Implement this method
        self.add(self.size(), x)

    def remove_first(self) -> object:
        """
        removes the head of the list and returns it
        :return: object type; the element that was removed
        """
        return self.remove(0)

    def remove_last(self) -> object:
        """
        removes the tail of the list and returns it.
        :return: object type; the element that was removed
        """
        # FIXME: Implement this method
        return self.remove(self.size()-1)

    def clear(self):
        """
        removes all contents in the deque
        :return: None
        """
        # FIXME: Implement this method
        self.n = 0
        self.dummy = self.Node(None)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def size(self):
        """
        returns the number of elements in the deque
        :return: int type;
        """
        return DLList.size(self)
