
class Node:
    def __init__(self, Data=None, Branches=[], Parent=None):
        self.Data = Data
        self.Branches = Branches
        self.Parent = Parent

    def __str__(self, Depth=0):
        ReturnStr = f"{self.Data}\n"
        if len(self.Branches) > 0:
            for _Node in self.Branches:
                if Depth >= 1:
                    ReturnStr += "\t" * (Depth) + f"----{_Node.__str__(Depth + 1)}\n"
                else:
                    ReturnStr += "----" * (Depth+1) + f"{_Node.__str__(Depth+1)}\n"
        return ReturnStr[0:-1]

    def Add(self, Branch):
        if isinstance(Branch, Tree):
            self.Branches.append(Tree.Root)
        else:
            self.Branches.append(Node(Data=Branch, Parent=self))

    def Remove(self):
        self.Parent.Branches.remove(self)


class Tree:
    def __init__(self, Root=None):
        self.Root = Node(Data=Root, Parent=self)

    def __str__(self):
        return str(self.Root)

MyTree = Tree(10)