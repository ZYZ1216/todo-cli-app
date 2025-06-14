import todo

def test_add_and_show():
    todo.todo_list.clear()
    todo.add_task("Buy milk")
    todo.add_task("Do homework")
    assert todo.todo_list == ["Buy milk", "Do homework"]

def test_delete_task():
    todo.todo_list.clear()
    todo.add_task("Task A")
    todo.add_task("Task B")
    todo.delete_task(0)
    assert todo.todo_list == ["Task B"]
