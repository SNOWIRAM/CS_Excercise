from _array import Array
?
?
class ArrayList:
    """
    if ... write necessary code.
    if return ... the function must return something
    if there are no return in the function, the function doesn't need to return anything.
    you may make necessary additional function aside from;
        append O(1), pop O(N), remove O(N), insert O(N)
    """
    def __init__(self):
        ...
?
    def __getitem__(self, index):
        # Don't touch
        if not 0 <= index < self._size:
            raise IndexError
        return self._array[index]
?
    def __setitem__(self, index: int, value):
        # Don't touch
        if not 0 <= index < self._size:
            raise IndexError
        self._array[index] = value
?
    def __repr__(self):
        # Don't touch
        return f"ArrayList[{', '.join(str(self._array[i]) for i in range(self._size))}]"
?
    def __len__(self):
        # O(1)
        return ...
?
    def __contains__(self, item: int):
        # al = ArrayList()À ¶§, item in al ±â ±¸Ç
        # O(N)
        ...
        return ...
?
# Aside from arraylist
# 1. Binary Search - social distancing problem
