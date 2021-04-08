class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_queue = []
        self.pop_queue = []
        self.top_el = None
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.push_queue.append(x)
        self.top_el = x
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        top = None
        while len(self.push_queue) > 1:
            top = self.push_queue.pop(0)
            self.pop_queue.append(top)
        
        self.top_el = top
        last = self.push_queue.pop(0)
        self.push_queue = self.pop_queue
        self.pop_queue = []

        return last

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.top_el
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return True if len(self.push_queue) == 0 else False


obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.pop())
print(obj.top())
print(obj.empty())
print("-=-=-=-=-=")
print(obj.pop())
print(obj.top())
print(obj.empty())

