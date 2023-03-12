class Node: 
    def __init__(self, value): 
        self.value = value 
        self.next = None 
        
class SinglyLinkedList:
    def __init__(self): 
        self.head = None 
    
    # Because Python uses garbage collection so you don't have to free memory manually. 
    # Delete a linked list
    def is_empty(self): 
        return self.head is None 
    
    # Counting the number of elements in a linked list 
    def size(self): 
        count = 0 
        current_node = self.head 
        while current_node: 
            count += 1 
            current_node = current_node.next 
        return count 
    
    # Adding a new element to the last of the linked list
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
            
    # Adding a new element to the front of the linked list; at the same time, the new node also becomes the new head of the linked list
    def prepend(self, value): 
        new_node = Node(value)
        new_node.next = self.head 
        self.head = new_node
        
    # Adding a new element to a selected position in the linked list 
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
    
    # Remove an element by value if it is in the linked list
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
    
    # Remove an element by a selected position in the linked list 
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
    
    # Print all elements of a linked list 
    def display(self): 
        values = []
        current_node = self.head 
        while current_node: 
            values.append(current_node.value)
            current_node = current_node.next 
        print(values)
        

            
            
    
    
                
        