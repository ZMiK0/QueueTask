#!/usr/bin/env python3

import queue
import os

q = queue.Queue()

end = False

def clear():
    os.system("clear")

while not end:
    clear()
    q.printQueue()
    try:
        option = int(input("-----------------\nWhat would you like to do?:\n\n1.Add Task to Queue\n2.End actual task\n3.Exit\n\nSELECT: "))
        if option == 1:
            clear()
            task = input("Task name: ")
            q.enqueue(task)
        elif option == 2:
            clear()
            q.dequeue()
        elif option == 3:
            clear()
            print("--Program terminated, deleting queue--")
            input("")
            end = True


    except:
        clear()
        print("ERROR")
        input("")

