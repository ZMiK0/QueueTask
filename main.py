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
        option = int(input("-----------------\nQue quieres hacer:\n\n1.Añadir a la cola\n2.Eliminar de la cola\n3.Salir\n\nElección: "))
        if option == 1:
            clear()
            task = input("Tarea a añadir: ")
            q.enqueue(task)

    except:
        clear()
        print("ERROR")
        input("")

