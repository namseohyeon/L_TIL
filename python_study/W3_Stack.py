class Stack():
    def __init__(self):
        self.stack = []
    def push(self, data): #원소 추가
        self.stack.append(data)
    def pop(self): #원소 삭제
        # n=len(self.stack)
        # return self.stack.pop(n-1)
        return self.stack.pop()
        # print(self.stack.pop()) #pop함수의 반환값 but 객체에서 pop을 쓸 때는 반환값이 전달이 안되는 듯,,?
    def IsEmpty(self): # 스택 확인
        if not self.stack: # not == !
            return True #스택에 요소x
        else:
            return False #스택에 요소o
    def top(self):
        if self.IsEmpty():
            print("stack에 원소가 없습니다")
        else:
            print(self.stack[-1])
            print("stack에 원소가 있습니다")

stack = Stack()
# print(stack.IsEmpty()) #False
# stack.top() #원소 없
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.pop()
# print(stack.IsEmpty()) #True
# stack.top() #pop값 반환

while not stack.IsEmpty(): #비어있지 않을 동안, stack.IsEmpty()가 거짓이면 계속!
    print(stack.pop(), end=' ')
    
