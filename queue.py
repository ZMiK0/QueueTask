from operator import indexOf, index
blanco = "\033[0m"
verde ="\033[32m"
cyan ="\033[36m"


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printQueue(self):
        print("-----------------")
        print("TASK QUEUE")
        print("-----------------" + blanco)
        for i in range(len(self.items)):
            if i == len(self.items)-1:
                print(f"{len(self.items) - i}: {self.items[i]}  {cyan}<--- {verde}NOW{blanco}")
            else:
                print(f"{len(self.items)-i}: {self.items[i]}")
