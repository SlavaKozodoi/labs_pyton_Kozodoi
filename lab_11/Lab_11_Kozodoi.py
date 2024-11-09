#1
class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__count = 0

    def get_counter(self):
        return self.__count

    def pop(self):
        val = super().pop()
        self.__count += 1
        return val


stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
########################################
#2
class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.list_queue = []

    def put(self, elem):
        self.list_queue.append(elem)

    def get(self):
        if not self.list_queue:
            raise QueueError
        else:
            return self.list_queue.pop(0)

que = Queue()
que.put(1)
que.put("dog")
que.put(False)

try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")


#####################################
#3

class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.list_queue = []

    def put(self, elem):
        self.list_queue.append(elem)

    def get(self):
        if not self.list_queue:
            raise QueueError
        else:
            return self.list_queue.pop(0)

class SuperQueue(Queue):
    def isempty(self):
        return len(self.list_queue) == 0

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")


