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
        option = int(input("-----------------\nQue quieres hacer:\n\n1.Añadir a la cola\n2.Finalziar tarea actual\n3.Salir\n\nElección: "))
        if option == 1:
            clear()
            task = input("Tarea a añadir: ")
            q.enqueue(task)
        elif option == 2:
            clear()
            q.dequeue()
        elif option == 3:
            clear()
            print("--Proceso terminado, cola eliminada--")
            input("")
            end = True


    except:
        clear()
        print("ERROR")
        input("")

