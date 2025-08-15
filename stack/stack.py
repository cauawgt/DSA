class StackNode:
    def __init__(self, key:int):
        self.key = key

class StackListSeq:
    def __init__(self, max:int, top: int, data:list[StackNode]):
        self.max = max
        self.top = top
        self.data = data

# Functions
def push(X:StackNode, list:StackListSeq):
    n = list.top
    if n < list.max-1:
        n += 1
        list.data[n] = X
        list.top = n
    else:
        print('OVERFLOW!')

def pop(list:StackListSeq):
    removed = None
    n = list.top
    if n >= 0:
        removed = list.data[n]
        list.top = n - 1
    else:
        print("UNDERFLOW!")
    
    return removed

max_size = 5
data = [StackNode(-1) for i in range(max_size)]
stack_list = StackListSeq(max_size, -1, data)

# Insert nodes
Node1 = StackNode(1)
push(Node1, stack_list)

Node2 = StackNode(2)
push(Node2, stack_list)

Node3 = StackNode(3)
push(Node3, stack_list)

print(pop(stack_list).key)  # Output: 3