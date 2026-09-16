class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity 

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.size += 1
        self.arr[self.size - 1] = n

    def popback(self) -> int:
        res = self.arr[self.size - 1]
        self.size -= 1
        return res

    def resize(self) -> None:
        self.capacity *=2
        newArr = [0] * self.capacity
        
        for idx,num in enumerate(self.arr):
            newArr[idx] = num
        self.arr = newArr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity