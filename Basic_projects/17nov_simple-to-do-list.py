tasks=[]
completed_tasks=[]

def add_task_func():
    add_task = input("Add some task: ")
    tasks.append(add_task)

def show_task_func():
    for i, item in enumerate(tasks, 1):
        print(i ,":", item)
    for i, item in enumerate(completed_tasks, 1):
        print(i ,":", item)

def complete_task_func():
    show_task_func()
    to_com = int(input("Which one to be marked as completed"))
    completed_tasks.append(tasks[to_com-1])
    tasks.remove(tasks[to_com-1])

while (1):
    print("Choose any one:\n")
    print("1. Add Task")
    print("2. Show Task")
    print("3. Mark Task as complete")
    chosen = int(input("Choose any one number:  "))
    if chosen == 1:
        add_task_func()
    elif chosen == 2:
        show_task_func()
    elif chosen == 3:
        complete_task_func()