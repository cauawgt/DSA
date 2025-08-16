class StackNode:
    def __init__(self, value:int):
        self.value = value
        self.prev = None

class StackLinked:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        new_node = StackNode(value)
        new_node.prev = self.head
        self.head = new_node
    

    def pop(self):
        if not self.head:
            return None
        
        removed_value = self.head.value
        
        self.head = self.head.prev

        return removed_value