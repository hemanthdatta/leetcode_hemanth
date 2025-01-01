class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MinStack:
    def __init__(self):
        self.head = None
        self.min_stack = []  # Stack to keep track of minimum values

    def push(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        
        # Update the min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> int:
        if self.head is None:
            return -1
        popped_value = self.head.value
        self.head = self.head.next
        
        # Update the min_stack
        if popped_value == self.min_stack[-1]:
            self.min_stack.pop()
        
        return popped_value

    def top(self) -> int:
        if self.head is None:
            return -1
        return self.head.value

    def getMin(self) -> int:
        if not self.min_stack:
            return -1
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()