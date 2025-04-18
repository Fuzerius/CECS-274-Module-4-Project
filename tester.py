import BookStore
from SLLQueue import SLLQueue
from SLLStack import SLLStack
from DLList import DLList
from DLLDeque import DLLDeque
from MaxQueue import MaxQueue
from BinaryTree import BinaryTree
from BinarySearchTree import BinarySearchTree
import random

def test():
    """write your own tester in this function"""
    print("Running your tester...")
    bookstore = BookStore.BookStore()
    bookstore.load_catalog("books_1.txt", "1")  # Use a small test file
    bookstore.search_by_prefix("a", 1000)

    

