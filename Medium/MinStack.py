# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# - MinStack() initializes the stack object.
# - void push(int val) pushes the element val onto the stack.
# - void pop() removes the element on the top of the stack.
# - int top() gets the top element of the stack.
# - int getMin() retrieves the minimum element in the stack.

# You must implement a solution with O(1) time complexity for each function.

class MinStack:
    # When we create a MinStack, we set up two lists, one for the regular stack and one for the special minimum stack.
    def __init__(self):
        self.stack = []  # This is our regular stack where we put our books.
        self.minStack = []  # This is our special stack where we keep track of the smallest books.

    # When we add a new book to our stack, we also check if it's smaller than the smallest book we've seen so far.
    def push(self, val: int) -> None:
        self.stack.append(val)  # We put the new book on top of our regular stack.
        if self.minStack:  # If our special stack already has some books in it,
            val = min(self.minStack[-1], val)  # we check if the new book is smaller than the current smallest book.
        self.minStack.append(val)  # We put the smallest book so far on top of our special stack.

    # When we take a book off the top of our regular stack, we also take the corresponding book off the top of our special stack.
    def pop(self) -> None:
        self.stack.pop()  # We take a book off the top of our regular stack.
        self.minStack.pop()  # We also take the corresponding book off the top of our special stack.

    # If we want to know which book is on top of our regular stack, we just look at the last book we added.
    def top(self) -> int:
        return self.stack[-1]  # We return the last book in our regular stack.

    # If we want to know which book is the smallest in our whole regular stack, we look at the last book in our special stack.
    def getMin(self) -> int:
        return self.minStack[-1]  # We return the last book in our special stack.



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()