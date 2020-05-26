from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque([])


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0



# Your MyStack object will be instantiated and called as such:
