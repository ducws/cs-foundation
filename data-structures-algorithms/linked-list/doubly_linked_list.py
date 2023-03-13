class Node:
    def __init__(self, value):
        self.previous = None
        self.value = value
        self.next = None


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    # Counting the number of elements in a linked list
    def size(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    # Adding a new node to the end of a linked list
    def append(self, value):
        new_node = Node(value)
        # Just another way of writing: if self.head is None
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            # Loop until current node is the last node of the linked list
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.previous = current_node

    # Add a new node to the beginning of a linked list
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
            self.head.previous = new_node
        self.head = new_node

    # Add a new node to a selected position in a linked list
    def insert(self, value, position):
        if position == 0:
            self.prepend(value)
        else:
            new_node = Node(value)
            current_node = self.head
            for i in range(position - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            new_node.previous = current_node
            if current_node.next:
                current_node.next.previous = new_node
            current_node.next = new_node

    # Remove a node from a linked list by a value
    def remove(self, value):
        if not self.head:
            return
        if self.head.value == value:
            # The old head will be automatically set to None by Python's garbage collector.
            self.head = self.head.next
            if self.head:
                '''Set the previous link of the new head to None. 
                Without this line, the new head previous link still
                points to the old node which has been deleted.'''
                self.head.previous = None
        else:
            current_node = self.head
            # Loop until the value of the node equals to the value we want to delete.
            while current_node.next:
                if current_node.value == value:
                    current_node.previous.next = current_node.next
                    if current_node.next:
                        current_node.next.previous = current_node.previous
                    break
                current_node = current_node.next

    # Remove a node from a linked list by a position
    def remove_at(self, position):
        if not self.head:
            return
        if position == 0:
            self.head = self.head.next
            if self.head:
                self.head.previous = None
        else:
            current_node = self.head
            for i in range(position):
                current_node = current_node.next
                if not current_node:
                    return
            current_node.previous.next = current_node.next
            if current_node.next:
                current_node.next.previous = current_node.previous

    def reverse(self):
        current_node = self.head
        previous_node = None
        while current_node:
            previous_node = current_node.previous
            '''This step reverses the current node's pointers,
            as its 'previous' attribute now points to the next 
            node in the list.'''
            current_node.previous = current_node.next
            '''We move to the next node in the list by assigning 
            'current_node' to its new 'previous' node (which was 
            its original 'next' node).'''
            current_node.next = previous_node
            current_node = current_node.previous
        self.head = previous_node.previous

    # Find the position of a value in a linked list
    def get_position(self, value):
        position = 0
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return position
            position += 1
            current_node = current_node.next
        return -1

    def delete_recursively(self, node):
        if node:
            self.delete_recursively(node.next)
            del node

    def delete_all(self):
        self.delete_recursively(self.head)
        '''Without this line the head of the linked list will still
        point to the first node of the list even though all nodes 
        have been deleted. Therefore, any subsequent operations on the linked list
        will still reference to the first node, which is no longer part of the list,
        leads to unexpected behavior.'''
        self.head = None

    # Print all nodes of a linked list
    def display(self):
        values = []
        current_node = self.head
        while current_node:
            values.append(current_node.value)
            current_node = current_node.next
        print(values)


dll = DoublyLinkedList()
day = 13
month = 3
year = 2023
hour = 0
minute = 19
second = 20

# Test "prepend" operation
dll.prepend(day)

# Test "append" operation
dll.append(month)

# Test "insert" operation
dll.insert(year, 2)

# Check three adding operations
dll.display()

# Test "getting position" operation
print(dll.get_position(2023))

# Test "reverse" operation
dll.reverse()
dll.display()

# Test "size" operation
print(dll.size())

# Test "remove by value" operation
dll.remove(2023)

# Test "remove by position" operation
dll.remove_at(1)

# Check two removing operations
dll.display()

for element in [hour, minute, second]:
    dll.append(element)

# Check "delete all nodes" operation
dll.delete_all()
dll.display()
