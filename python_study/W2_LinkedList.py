class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def add(data): #테일에 추가
    node = head
    while node.next:
        node = node.next
    node.next = Node(data) 

def delete(data): #데이터를 입력하면 그 데이터 삭제
    global head 
    if head.data == data:
        current = head
        head = head.data
        return
    
    current = head 
    while node.next:
        before=current
        current = current.next
        if(current.data == data):
            before.next = current.next
            return

    


node1 = Node(1)

node2 = Node(2)

node3 = Node(3)

node2.next = node1
node3.next = node2
head = node3

node=head

add(4) #Node뒤에 값을(tail)을 추가하는 함수 node1 다음 노드가 데이터4를 가지고 있다.
delete(2)

while node.next:
    print(node.data)
    node=node.next
print(node.data)
