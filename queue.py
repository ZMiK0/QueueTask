from operator import indexOf, index


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
        print("COLA DE TAREAS")
        print("-----------------")
        for i in range(len(self.items)):
            if i == len(self.items)-1:
                print(f"{len(self.items) - i}: {self.items[i]}  <--- TAREA ACTUAL")
            else:
                print(f"{len(self.items)-i}: {self.items[i]}")
