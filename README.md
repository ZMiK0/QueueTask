
# QueueTask

An easy-to-use TUI program for managing tasks in a queue. I created this program to
simplify the experience of using other tools like
Notion, Microsoft To Do, and similar applications.


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

# Extra

> To do:
> * Add windows support
> * Make any task a priority

