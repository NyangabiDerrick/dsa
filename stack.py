# By Rose Mateta
# Stack - LIFO (Last In, First Out) data structure
# O(1) time complexity for push, pop, and peek operations

class Stack:
    """Stack implementation using Python list"""
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add item to top of stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return item from top of stack"""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack empty!")

    def peek(self):
        """Return top item without removing it"""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack empty!")

    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0

# Example usage
if __name__ == "__main__":
    s = Stack()
    s.push("Book 1")
    s.push("Book 2")
    s.push("Book 3")
    print("Popped:", s.pop())     # Book 3 (last in, first out)
    print("Top is now:", s.peek())    # Book 2
    print("Stack empty?", s.is_empty())
