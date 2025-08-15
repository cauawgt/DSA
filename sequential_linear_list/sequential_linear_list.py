class SeqLinearNode:
    def __init__(self, key:int):
        self.key = key

class SeqLinearList:
    def __init__(self, max:int, last:int, data:list[SeqLinearNode]):
        self.max = max
        self.last = last
        self.data = data
    
# Functions
def search(x:int, list:SeqLinearList):
    index = __search_index(x, list)
    if index != -1:
        return list.data[index]
    else:
        return None
 
def __search_index(x:int, list:SeqLinearList) -> int:
    index = -1
    n = list.last
    i = 0
    while i <= n:
        if list.data[i].key == x:
            index = i
            i = n + 1
        else:
            i += 1
    
    return index

def insert(X:SeqLinearNode, list:SeqLinearList):
    n = list.last
    if n < list.max:
        if __search_index(X.key, list) == -1:
            n += 1
            list.data[n] = X
            list.last = n
        else:
            print(f"Node {X.key} have already exists in list.")
    else:
        print("Full list")

def remove(x:int, list:SeqLinearList):
    removed = None
    n = list.last
    index = __search_index(x, list)
    d = list.data
    if index != -1:
        removed = d[index]
        for i in range(index, n):
            d[i] = d[i+1]
        list.last = n-1
    
    return removed

# examples
if __name__ == "__main__":
    # Create a sequential linear list
    max_size = 5
    data = [SeqLinearNode(-1) for i in range(max_size)]
    seq_list = SeqLinearList(max=max_size, last=0, data=data)

    # Search for a node
    result = search(3, seq_list)
    print(f"Search result: {result.key if result else 'Not found'}")

    # Insert a new node
    new_node = SeqLinearNode(5)
    insert(new_node, seq_list)

    # Remove a node
    removed_node = remove(2, seq_list)
    print(f"Removed node: {removed_node.key if removed_node else 'Not found'}")