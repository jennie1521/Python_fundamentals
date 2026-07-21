#Queue
class Queue:
    def __init__(self):
        self.values=[]
    def enqueue(self,x):
        self.values.append(x)
    def dequeue(self):
        front=self.values[0]
        self.values=self.values[1:]
        return front

q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.values)
print(q.dequeue())
print(q.values)

#stack
class Stack:
    def __init__(self):
        self.values=[]
    def push(self,x):
        self.values=[x]+self.values
    def pop(self):
        return self.values.pop(0)
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(50)
print(s.values)
s.pop()
print(s.values)
