def main():
    s = Stack()
    s.push(10)
    s.push(20)
    print(s.pop())
    print(s.isEmpty())
    print(s.pop())
    print(s.isEmpty())

class Stack:

    def __init__(self):
        self.arr = []

    def push(self,value):
        self.arr.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.arr.pop()
    
    def peek(self):
        if not self.isEmpty():
            return self.arr[-1]
    
    def isEmpty(self):
        return len(self.arr) == 0
    

# Run main function only if this python file is directly run
if __name__ == '__main__':
    main()
