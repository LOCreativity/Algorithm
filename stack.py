# 리스트로 스택 구현
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item) # 리스트 끝에 요소 삽입 (스택 push 기능)

    def pop(self):
        if not self.is_empty():
            return self.items.pop() # 리스트 끝에 있는 요소 삭제 (스택 pop 기능)
        else:
            return "스택이 비어있습니다"

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)

stack = Stack()
stack.push(1)
stack.push(5)
print(stack)

stack.pop()
print(stack)