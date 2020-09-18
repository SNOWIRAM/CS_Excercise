class Array:
    def __init__(self, size: int):
        self._size = size
        self._array = [None] * size
?
    def __getitem__(self, item):
        if not 0 <= item < self._size:
            raise IndexError
        return self._array[item]
?
    def __setitem__(self, key, value):
        if not 0 <= key < self._size:
            raise IndexError
        self._array[key] = value
?
    def __repr__(self):
        return f"Array{self._array}"
