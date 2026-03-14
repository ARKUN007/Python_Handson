class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.peek()
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
mystack = Stack()

mystack.push("A")
mystack.push("E")
mystack.push("C")
mystack.push("B")
mystack.push("D")

print("Stack: ", mystack.stack)

print("Pop: ",mystack.pop())

print("Stack after pop: ", mystack.stack)

print("isEmpty :", mystack.isEmpty())

print("Size :", mystack.size())

print("Peek :", mystack.peek())