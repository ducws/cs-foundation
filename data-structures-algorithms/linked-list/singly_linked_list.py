class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Counting the number of nodes in a linked list
    def size(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    # Adding a new node to the last of the linked list
    def append(self, value):
        new_node = Node(value)
        # Just another way of writing: if self.head is None
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            # loop until current node is the last node of the linked list
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    # Adding a new node to the front of the linked list; at the same time, the new node also becomes the new head of the linked list
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Adding a new node to a selected position in the linked list
    def insert(self, value, position):
        if position == 0:
            self.prepend(value)
        else:
            new_node = Node(value)
            current_node = self.head
            for i in range(position - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node

    # Remove a node by value if it is in the linked list
    def remove(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
        else:
            current_node = self.head
            # Loop until the value of the next node equals to the value wanted to delete
            while current_node.next:
                if current_node.next.value == value:
                    # Python will automatically clear the memory of the current_node.next so that we don't have to do it manually
                    current_node.next = current_node.next.next
                    break
                current_node = current_node.next

    # Remove a node by a selected position in the linked list
    def remove_at(self, position):
        if not self.head:
            return
        if position == 0:
            self.head = self.head.next
        else:
            current_node = self.head
            for i in range(position - 1):
                if not current_node.next:
                    return
                current_node = current_node.next
            if not current_node.next:
                return
            current_node.next = current_node.next.next

    # Delete each node before the head recursively
    def delete_recursive(self, node):
        if node:
            self.delete_recursive(node.next)
            del node

    def delete_all(self):
        self.delete_recursive(self.head)
        '''Without this line the head of the linked list will still
        point to the first node of the list even though all nodes 
        have been deleted. Therefore, any subsequent operations on the linked list
        will still reference to the first node, which is no longer part of the list,
        leads to unexpected behavior'''
        self.head = None

    # Reverse the order of the linked list
    def reverse(self):
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    # Find the position of a value if it is in the linked list
    def get_position(self, value):
        position = 0
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return position
            position += 1
            current_node = current_node.next
        return -1

    # Print all nodes of a linked list
    def display(self):
        values = []
        current_node = self.head
        while current_node:
            values.append(current_node.value)
            current_node = current_node.next
        print(values)


sll = SinglyLinkedList()
day = 13
month = 3
year = 2023
hour = 0
minute = 19
second = 20

# Test "prepend" operation
sll.prepend(day)

# Test "append" operation
sll.append(month)

# Test "insert" operation
sll.insert(year, 2)

# Check three adding operations
sll.display()

# Test "getting position" operation
print(sll.get_position(2023))

# Test "reverse" operation
sll.reverse()
sll.display()

# Test "size" operation
print(sll.size())

# Test "remove by value" operation
sll.remove(2023)

# Test "remove by position" operation
sll.remove_at(1)

# Check two removing operations
sll.display()

for element in [hour, minute, second]:
    sll.append(element)

# Check "delete all nodes" operation
sll.delete_all()
sll.display()
