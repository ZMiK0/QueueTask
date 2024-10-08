
Programa sencillo de seguimiento de tareas para la gente que no quiere comerse la cabeza con programas ultra complejos como Notion

To do:
-
* Darle prioridad urgente a una tarea cualquiera
* Compatibildad con windows

# Installation

```shell
git clone https://github.com/ZMiK0/QueueTask.git
cd QueueTask
mv main.py main
chmod a+x main
cd ..
sudo cp -r QueueTask /usr/local/bin/
sudo ln -s /usr/local/bin/QueueTask/main /usr/local/bin/quetask
rm -r QueueTask
```

## Uninstall
```shell
sudo rm /usr/local/bin/quetask
sudo rm -r /usr/local/bin/QueueTask
```

# Use
```shell
$ quetask
```

