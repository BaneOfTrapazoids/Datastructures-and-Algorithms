from random import randint
import time


class Cell:
    def __init__(self, Key=None, Value=None):
        self.Key = Key
        self.Value = Value
        self.Status = "Empty"


class Dictionary:
    def __init__(self, Keys=[], Values=[]):
        Keys = list(set(Keys))
        self.Size = len(Keys) * 2
        self.Cells = [Cell() for i in range(self.Size)]

        for k, v, in zip(Keys, Values):
            Index = hash(k) % self.Size
            IndexedCell = self.Cells[Index]
            if IndexedCell.Status == "Filled":
                for cell in self.Cells:
                    if cell.Status == "Empty":
                        IndexedCell = cell
                        break
            IndexedCell.Key = k
            IndexedCell.Value = v
            IndexedCell.Status = "Filled"

        self.FilledCells = [element for element in self.Cells if element.Status == "Filled"]

    def __setitem__(self, Key, Value):

        if len(self.FilledCells) / len(self.Cells) >= 0.85:
            print(f"{len(self.FilledCells)} /  {len(self.Cells)} = {len(self.FilledCells) / len(self.Cells)}")
            print("Rehashing...")
            self.Rehash()

        Index = hash(Key) % self.Size
        IndexedCell = self.Cells[Index]
        if IndexedCell.Status == "Filled" and IndexedCell.Key != Key:
            IndexedCell = self.CollisionResolver(Index + 1)
        IndexedCell.Key = Key
        IndexedCell.Value = Value
        IndexedCell.Status = "Filled"
        self.FilledCells = [element for element in self.Cells if element.Status == "Filled"]

    def __getitem__(self, Key):
        Index = hash(Key) % self.Size
        IndexedCell = self.Cells[Index]
        if IndexedCell.Key != Key:
            IndexedCell = self.CollisionResolver(Index + 1)
        return IndexedCell.Value

    def __str__(self):
        ReturnStr = "{ "
        for Cell in self.Cells:
            if Cell.Status == "Filled":
                ReturnStr += f"{Cell.Key} : {Cell.Value}, "
        ReturnStr = ReturnStr[0:-2] + " }"
        return ReturnStr

    def Rehash(self):
        self.Size *= 2
        Cells = [Cell() for i in range(self.Size)]
        for Cell in self.Cells:
            Index = hash(Cell.Key) % self.Size
            IndexedCell = Cells[Index]
            if IndexedCell.Status == "Filled":
                while IndexedCell.Status == "Filled":
                    Index += 1
                    if Index == len(Cells) - 1:
                        Index = 0
                    IndexedCell = Cells[Index]
            IndexedCell.Key = Cell.Key
            IndexedCell.Value = Cell.Value
            IndexedCell.Status = "Filled"
        self.Cells = Cells

    # When a hash collision occurs, this is called to find the proper cell
    def CollisionResolver(self, Start):
        IndexedCell = self.Cells[Start]
        while IndexedCell.Status == "Filled":
            Start += 1
            if Start == len(self.Cells) - 1:
                Start = 0
            IndexedCell = self.Cells[Start]
        return IndexedCell

    def remove(self, Key):
        Index = hash(Key) % self.Size
        IndexedCell = self.Cells[Index]
        if IndexedCell.Key != Key:
            IndexedCell = self.CollisionResolver(Index + 1)
        IndexedCell.Key = None
        IndexedCell.Value = None
        IndexedCell.Status = "Empty"

StartTime = time.perf_counter()
mykeys = [randint(1,100) for i in range(1000000)]
myvalues = [x*2 for x in mykeys]

mydict = Dictionary(mykeys, myvalues)
print(mydict)
EndTime = time.perf_counter()

print(EndTime - StartTime)
