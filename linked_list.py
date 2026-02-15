# By Tinaelis Mumbi
# Linked List - Singly linked list with dynamic size
# O(n) for append/access/search, O(1) for insert/delete with node reference

class Node:
    """Node with data and pointer to next node"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Singly linked list implementation"""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add node at the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        # Traverse to the end
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        """Print all nodes in the list"""
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.print_list()
