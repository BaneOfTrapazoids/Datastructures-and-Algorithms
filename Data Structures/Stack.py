
class Stack:
    def __init__(self, Items):
        self._Items = list(Items)
        self.Item = self._Items[-1]

    def Get(self):
        return self.Item

    def Set(self, Value):
        self._Items[0] = Value
        self.Item = Value

    def Remove(self):
        self._Items.remove(self.Item)
        self.Item = self._Items[-1]

    def Add(self, Value):
        self._Items.append(Value)
        self.Item = self._Items[-1]

    def __str__(self):
        return "[" + ", ".join(map(str, self._Items)) + "]"

mystack = Stack([1, 2, 3, 4, 5])
print(mystack)
mystack.Remove()
print(mystack)
mystack.Add(50)
print(mystack)