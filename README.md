# To-Do List (Python CLI)

A simple command-line based To-Do List application built with Python.
This project demonstrates basic programming concepts such as loops, functions, lists, and input handling.

## Features

* View tasks in a numbered list
* Add new tasks
* Remove tasks by selecting their number
* Exit the application when finished

## How It Works

* Tasks are stored in memory (not saved to a file).
* When the program is closed, all tasks are cleared.
* Input validation ensures that invalid selections or empty tasks are handled gracefully.

## Example Usage

```
>> To-Do List <<
1. View tasks
2. Add task
3. Remove task
4. Exit
```

* Choosing **1** displays all current tasks.
* Choosing **2** allows you to add a new task.
* Choosing **3** shows the task list and prompts for a task number to remove.
* Choosing **4** exits the program.

## Requirements

* Python 3.6+

## Installation

Clone the repository:

```bash
git clone https://github.com/kaiintech/to-do-list-python.git
cd to-do-list-python
```

Run the program:

```bash
python main.py
```

## Future Improvements

* Save tasks to a file so they persist between sessions
* Add due dates or priorities for tasks
* Implement task editing functionality
* Build a graphical user interface (GUI) version
* Extend to a web-based version with Flask or Django
