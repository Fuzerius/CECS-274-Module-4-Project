from Interfaces import Graph, List
from ArrayList import ArrayList
from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack
import numpy as np


class AdjacencyMatrix(Graph):

    def __init__(self, n: int, dtype=ArrayList):
        self.n = n
        self.adj = np.zeros((self.n, self.n), dtype=int)
        self.dtype = dtype

    def add_edge(self, i: int, j: int):
        """
        adds a directed edge from node i to node j
        :param i: int type; index of node i
        :param j: int type; index of node j
        :raises: IndexError if i < 0 or j < 0
                 or i >= number of nodes or j >= number of nodes
        """
        # FIXME: REPLACE WITH YOUR IMPLEMENTATION
        if i < 0 or j < 0 or i >= self.n or j >= self.n:
            raise IndexError("Invalid index for node")
        self.adj[i][j] = True

    def remove_edge(self, i: int, j: int) -> bool:
        """
        removes the directed edge from node i to node j,
        if it exists in the graph.  Returns true if
        edge was removed, false otherwise
        :param i: int type; index of node i
        :param j: int type; index of node j
        :raises: IndexError if i < 0 or j < 0
                 or i >= number of nodes or j >= number of nodes
        :returns: bool type; true if the edge (i, j) was removed, false otherwise.
        """
        # FIXME: REPLACE WITH YOUR IMPLEMENTATION
        if i < 0 or j < 0 or i >= self.n or j >= self.n:
            raise IndexError("Invalid index for node")
        if self.adj[i][j]:  # Check if the edge exists
            self.adj[i][j] = 0  # Remove the edge
            return True
        return False  # Edge did not exist

    def has_edge(self, i: int, j: int) -> bool:
        """
        determines if the directed edge from node i to node j
        exists in the graph.  Returns true if edge (i, j) exists,
        false otherwise.
        :param i: int type; index of node i
        :param j: int type; index of node j
        :raises: IndexError if i < 0 or j < 0
                 or i >= number of nodes or j >= number of nodes
        :returns: bool type; true if the edge (i, j) exists, false otherwise.
        """
        # FIXME: REPLACE WITH YOUR IMPLEMENTATION
        if i < 0 or j < 0 or i >= self.n or j >= self.n:
            raise IndexError("Invalid index for node")
        return self.adj[i][j]

    def out_edges(self, i) -> List:
        """
        returns a List of node indices that are targets
        of the node at index i, i.e., a List of all nodes j
        such that (i, j) is an edge in the graph
        :param i: int type; index of source node
        :raises: IndexError if i < 0 or i >= number of nodes
        :returns: List subclass type; either an ArrayList or DLList
                  as specified by the attribute 'dtype'
        """
        # FIXME: REPLACE WITH YOUR IMPLEMENTATION
        if i < 0 or i >= self.n:
            raise IndexError("Invalid index for node")
        l = self.dtype()
        for j in range(self.n):
            if self.adj[i][j]:
                l.append(j)
        return l
        

    def in_edges(self, j) -> List:
        """
        returns a List of node indices that are sources
        of the node at index j, i.e., a List of all nodes i
        such that (i, j) is an edge in the graph
        :param j: int type; index of targe node
        :raises: IndexError if i < 0 or i >= number of nodes
        :returns: List subclass type; either an ArrayList or DLList
                  as specified by the attribute 'dtype'
        """
        # FIXME: REPLACE WITH YOUR IMPLEMENTATION
        if j < 0 or j >= self.n:
            raise IndexError("Invalid index for node")
        l = self.dtype()
        for i in range(self.n):
            if self.adj[i][j]:
                l.append(i)
        return l

    def bfs(self, r: int):
        """
        returns a List of the node indices of the graph as they are
        traversed using Breadth-First Search Traversal beginning at
        the node at index r
        :param r: int type; the index of the source node
        :returns: List subclass type; ArrayList or DLList as specified by
                  the attribute 'dtype'
        """
        # FIXME: REPLACE WITH YOUR IMPLEMENTATION
        traversal = self.dtype()
        seen = [False] * self.n
        q = ArrayQueue()
        q.add(r)
        traversal.append(r)
        seen[r] = True
        while q.size() != 0:
            v = q.remove()
            for i in range(self.n):
                if self.adj[v][i] and not seen[i]:
                    q.add(i)
                    traversal.append(i)
                    seen[i] = True
        return traversal

    def dfs(self, r: int):
        """
        returns a List of the node indices of the graph as they are
        traversed using Depth-First Search Traversal beginning at
        the node at index r
        :param r: int type; the index of the source node
        :returns: List subclass type; ArrayList or DLList as specified by
                  the attribute 'dtype'
        """
        # FIXME: REPLACE WITH YOUR IMPLEMENTATION
        traversal = self.dtype()
        seen = [False] * self.n
        s = ArrayStack()
        s.push(r)
        while s.size() != 0:
            v = s.pop()
            if not seen[v]:
                seen[v] = True
                traversal.append(v)
                for i in range(self.n - 1, -1, -1):  # Reverse order to maintain correct DFS order
                    if self.adj[v][i] and not seen[i]:
                        s.push(i)
        return traversal

    def size(self):
        """
        returns the number of nodes in the graph
        :returns: int type;
        """
        return self.n

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += f"{i}:  {self.adj[i]}\n"
        return s

