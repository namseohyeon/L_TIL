# 모듈 사용 시 편리함
# from collections import deque
# popleft(),appendleft(), append(), pop() 존재
class Queue():
    def __init__(self):
        self.queue = []
    def isEmpty(self):
        if not self.queue: # not == !
            return True #큐에 요소x
        else:
            return False #큐에 요소o
    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            Q=self.queue[0]
            self.queue = self.queue[1:] #self.queue.pop(0)
            return Q

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.queue[0]

queue1 = Queue()
# print(queue1.isEmpty())
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
# print(queue1.isEmpty())
# print(queue1.dequeue())
# print(queue1.peek())


# while not queue1.isEmpty():
#     print(queue1.dequeue(),end="")

class CircularQueue():
    def __init__(self):
        # self.CQ = []
        self.front = 0
        self.rear = 0
        self.MAX = 10
        self.CQ = [None]*self.MAX
        # self.count = 0

    def IsEmpty(self):
        if(self.front == self.rear):
            return True
        else:
            return False
    def IsFull(self):
        if(self.rear+1)%self.MAX == self.front:
            return True
        else:
            return False
    def enqueue(self,data):
        if self.IsFull():
            print("FULL")
        else:
            self.rear=(self.rear+1)%self.MAX
            self.CQ[self.rear] = data
            #self.count +=1
    def dequeue(self):
        if self.IsEmpty():
            return "EMPTY"
        else:
            self.front = (self.front+1)%self.MAX
            #self.count -=1
            return self.CQ[self.front]
    def peek(self):
        if self.IsEmpty():
            print("Queue is empty")
        else:
            return(self.CQ[(self.front + 1)%self.MAX])
        #self.front = (self.)
    def print_queue(self):
        i = self.front
        if self.IsEmpty():
            print("EMPTY")
            return
        else:
            while not self.IsEmpty():
                print(self.dequeue())


queue2 = CircularQueue()
# print(queue2.IsEmpty())
# print(queue2.IsFull())
queue2.enqueue(1)
queue2.enqueue(2)
queue2.enqueue(3)
queue2.print_queue()
    
