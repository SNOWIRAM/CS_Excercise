from _array import Array

ARRAY_DEFAULT_SIZE = 10

class ArrayList:
    """
    if ... write necessary code.
    if return ... the function must return something
    if there are no return in the function, the function doesn't need to return anything.
    you may make necessary additional function aside from;
        append O(1), pop O(N), remove O(N), insert O(N)
    """
    def __init__(self):
        self._size = 0
        self._array = Array(size=ARRAY_DEFAULT_SIZE)

    def __getitem__(self, index):
        if not 0 <= index < self._size:
            raise IndexError
        return self._array[index]

    def __setitem__(self, index: int, value):
        if not 0 <= index < self._size:
            raise IndexError
        self._array[index] = value

    def __repr__(self):
        return f"ArrayList[{', '.join(str(self._array[i]) for i in range(self._size))}]"

    def __len__(self):
        return self._size

    def __contains__(self, item: int):
        bool_contain = False
        for i in self._array:
            if i == item:
                bool_contain = True
                break
        return bool_contain

    def append(self, value):
        if self._size == self._array._size:
            temp_array = Array(size=2*self._array._size)

            for i in range(self._array._size):
                temp_array[i] = self._array[i]
            self._array = temp_array

        self._array[self._size] = value
        self._size += 1

    def pop(self, index: int):
        if not 0 <= index < self._size:
            raise IndexError

        self._size -= 1
        value = self._array[index]

        for i in range(index, self._size):
            self._array[i] = self._array[i+1]
        return value

    def remove(self, index: int):
        if not 0 <= index < self._size:
            raise IndexError

        self._size -= 1 

        for i in range(index, self._size):
            self._array[i] = self._array[i+1]

    def insert(self, index: int, value):
        if not 0 <= index < self._size:
            raise IndexError

        if self._size == self._array._size:
            temp_array = Array(size=2*self._array._size)
            for i in range(self._array._size):
                temp_array[i] = self._array[i]
            self._array = temp_array

        for j in range(self._size, index, -1):
            self._array[j] = self._array[j-1]

        self._array[index] = value
        self._size += 1


if __name__ == "__main__":
    # Test
    al = ArrayList()
    al.append(1)
    print(al)
    print(len(al))
    al.pop(1)
    print(al)
    print(len(al))
    al.insert(4, 2)
    print(al)
    print(len(al))
