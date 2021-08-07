
class Queue:
    def __init__(self, Items):
        self._Items = list(Items)
        self.Item = self._Items[0]

    def Get(self):
        return self.Item

    def Set(self, Value):
        self._Items[0] = Value
        self.Item = Value

    def Remove(self):
        self._Items.remove(self.Item)
        self.Item = self._Items[0]

    def Add(self, Value):
        self._Items.append(Value)

    def __str__(self):
        return "[" + ", ".join(map(str, self._Items)) + "]"
