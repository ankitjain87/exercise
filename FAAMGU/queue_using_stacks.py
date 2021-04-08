class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = []
        self.pop_stack = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.push_stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.pop_stack) > 0:
            return self.pop_stack.pop()

        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())

        return self.pop_stack.pop()

        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.push_stack and not self.pop_stack:
            return None

        if self.pop_stack:
            return self.pop_stack[-1]

        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())
        
        return self.pop_stack[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.push_stack and not self.pop_stack:
            return True

        return False

obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.pop())
print(obj.peek())
print(obj.empty())
print("-=-=-=-=-=-=-=")        
print(obj.pop())
print(obj.peek())
print(obj.empty())
