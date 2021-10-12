
class Stack:
    def __init__(self, max_size):
        self.__stack = []
        self.__max_size = max_size
    def push(self, item):
        if self.isFull():
            raise IndexError("The stack is full of data")
        else:
            self.__stack.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty list")
        else:
            return self.__stack.pop()
    def isEmpty(self):
        return len(self.__stack) == 0
    def isFull(self):
        return len(self.__stack) == self.__max_size
    def peek(self):
        if self.isEmpty():
            pass
        return self.__stack[-1]

if __name__=='__main__':
    stack = Stack(3)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    print(stack)
    print("Top element: ", stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
