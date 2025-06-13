todo_list = []

def add_task(task):
    todo_list.append(task)

def show_tasks():
    for i, task in enumerate(todo_list):
        print(f"{i+1}. {task}")

def delete_task(index):
    if 0 <= index < len(todo_list):
        todo_list.pop(index)
