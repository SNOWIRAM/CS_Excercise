class Node:
    def __init__(self, data):
        ...


class LinkedList:
    # Implement the functionality of the Doubly Linked List.

    def __init__(self):
        pass

    def append_head(self, data):
        # Appends the given data at the front of the first node.
        # Should run in O(1) time.
        ...

    def append_tail(self, data):
        # Appends the given data at the back of the last node.
        # Should run in O(1) time.
        ...

    def remove_head(self):
        # Remove and returns the data of the first node.
        # Raises IndexError if linked list is empty.
        # Should run in O(1) time.

        return None

    def remove_tail(self):
        # Remove and returns the data of the last node.
        # Raises IndexError if linked list is empty.
        # Should run in O(1) time.

        return None

    def _get_ith_node(self, index: int):
        # Returns i-th node of this linked list.
        # Raises IndexError for invalid index value.
        # Should run in O(index) time.
        return ...

    def remove_ith(self, index: int):
        # Remove and returns the data of the i-th node.
        # Do not modify the following line;
        _node = self._get_ith_node(index)
        ...
        # The rest of the function should run in O(1) time.
        return ...

    def insert_after_ith(self, index: int, data):
        # Inserts the given data at the back of the i-th node.
        # Do not modify the following line;
        _node = self._get_ith_node(index)
        # Define new node
        ...

    def __contains__(self, data):
        # Should run in O(size) time.
        ...

    def sum(self, initial_value=0):
        # Returns the sum of all data.
        # Should run in O(size) time.
        return ...

    def __repr__(self):
        # Returns a string representation of itself.
        # ex) return "LinkedList[1 -> 2 -> 3 -> 4]"
        # Should run in O(size) time.
        # For simplicity, assume any string addition(concatenation) takes O(1) time.

        # ** Caution **
        #   Do not print the result using print(...).
        #   Constructing the string and returning is enough.
        ...