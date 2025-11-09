# 리스트로 큐 구현
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item) # 리스트에 요소 삽입 (큐 enqueue 기능)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0) # 리스트에 가장 먼저 있던 요소 삭제 (큐 dequeue 기능)
        else:
            return "큐 요소가 비어있습니다"

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)

queue = Queue()
queue.enqueue(1)
queue.enqueue(5)
queue.enqueue(2)
print(queue)

queue.dequeue()
print(queue)