class Node:
    def __init__(self, Data=None):
        self.Data = Data
        self.NextNode = None

    def __str__(self):
        return f"{self.Data}"


class LinkedList:
    def __init__(self, Items=[]):
        self.Start = Node()
        self._Length = 0

        _Node = self.Start

        for element in Items:
            _Node.Data = element
            _Node.NextNode = Node()
            _Node = _Node.NextNode
            self._Length += 1
        self.End = _Node

    def __iter__(self):
        self._Node = self.Start
        return self

    def __next__(self):
        self._CurrentNode = self._Node
        self._Node = self._Node.NextNode

        if self._Node is None:
            raise StopIteration

        return self._CurrentNode.Data

    def __str__(self):
        return "[" + ", ".join(map(str, self)) + "]"

    def __getitem__(self, Index):
        self._Node = self.Start

        for i in range(Index):
            self._Node = self._Node.NextNode

        return self._Node.Data

    def __setitem__(self, Key, Value):
        self._Node = self.Start

        for i in range(Key):
            self._Node = self._Node.NextNode

        self._Node.Data = Value

    def Add(self, value):
        self.End.Data = value
        self.End.NextNode = Node()
        self.End = self.End.NextNode
        self._Length += 1
