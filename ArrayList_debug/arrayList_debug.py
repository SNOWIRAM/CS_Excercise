from ArrayList._arraylist import ArrayList

# Bug associated with pop()
# Test code
a = ArrayList()
a.append(1)
print(a)
a.pop(1) # this should return IndexError.

# Bug associated with remove()
# Test code
a = ArrayList()
a.append(1)
a.append(2)
a.append(3)
a.remove(5) # this should return IndexError
print(a)

# also, remove should take value, not index

# Bug associated with insert
a = ArrayList()
a.append(1)
a.append(2)
a.append(3)

a.insert(3,100)
a.insert(4,100)
a.insert(5,100) # WA. None shouldn't be visible.
                # ArrayList[1, 2, 3, 100, 100, None]
print(a)

# Possible Reason
print(a._array) # Array[1, 2, 3, 100, 100, None, 100, None, None, None]
"""
f"ArrayList[{', '.join(str(self._array[i]) for i in range(self._size))}]"

because the code cuts self._array with the self._size, it only shows
[1,2,3,100,100,None]
"""
