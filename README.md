
# QueueTask

An easy-to-use TUI program for managing tasks in a queue. I created this program to
simplify the experience of using other tools like
Notion, Microsoft To Do, and similar applications.


# Installation

> [!WARNING]
> This installation requires sudo to run.

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

> [!TIP]
> To update just uninstall and install again :P (I'm working on this).

> [!IMPORTANT]
> On Windows just clone the repo, `cd` into it, and run `main.py` from the terminal

# Use
```shell
$ quetask
```

# Extra

> To do:
> * Make any task a priority

