from MobileCritter import MobileCritter
from Insect import Insect


class Spider(Insect, MobileCritter):
    """
    Class: instantiates Spider objects that can move right, left, up, and down
           Inherits from the Insect super class position, so that Ant objects also have position and leaves attributes, as well as methods for collecting and retrieving leaves, and reporting position.
           Implements the MobileCritter interface, i.e., implements the methods move_right, move_left, move_up, move_down
    """
    def __init__(self):
        Insect.__init__(self)  # Calling the Insect constructor to initialize and inherit attributes from Insect

    def move_right(self):
        """moves this spider's position 1 unit right"""
        # todo
        self.position[0] += 1

    def move_left(self):
        """moves this spider's position 2 units left"""
        # todo
        self.position[0] -= 2

    def move_up(self):
        """moves this spider's position 1 unit up"""
        # todo
        self.position[1] += 1

    def move_down(self):
        """moves this spider's position 2 units down"""
        # todo
        self.position[1] -= 2

    def __str__(self):
        return u'\u1F577'
