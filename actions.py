import datetime
from utils import todos

def show_next_todo():
    if todos:
        print(f'Next todo: {todos[0]}')
    else:
        print('No todos left!')

def edit_todo():
    for i, todo in enumerate(todos, start=1):
        print(f'{i}. {todo}')
    todo_number = int(input('Which todo do you want to edit? '))
    if 0 < todo_number <= len(todos):
        new_task = input('Enter the new task: ')
        new_due_date = input('Enter the new due date (YYYY-MM-DD): ')
        new_priority = input('Enter the new priority level (1-5): ')
        new_todo = f'{new_task}, Due Date: {new_due_date}, Priority: {new_priority}'
        todos[todo_number - 1] = new_todo
    else:
        print('Invalid todo number')

def delete_todo():
    for i, todo in enumerate(todos, start=1):
        print(f'{i}. {todo}')
    todo_number = int(input('Which todo do you want to delete: '))
    if 0 < todo_number <= len(todos):
        deleted_todo = todos.pop(todo_number - 1)
        print(f'Deleted todo: {deleted_todo}')
        with open('todo_log.txt', 'w') as f:
            for todo in todos:
                f.write(f'{datetime.datetime.now()}: {todo}\n')
    else:
        print('Invalid todo number')

def add_todo():
    new_todo = input('Enter a new todo: ')
    due_date = input('Enter the due date (YYYY-MM-DD): ')
    priority = input('Enter the priority level (1-5): ')
    todo_entry = f'{new_todo}, Due Date: {due_date}, Priority: {priority}'
    todos.append(todo_entry)
    with open('todo_log.txt', 'a') as f:
        f.write(f'{datetime.datetime.now()}: {todo_entry}\n')

def show_all_todos():
    if todos:
        for i, todo in enumerate(todos, start=1):
            print(f'{i}. {todo}')
    else:
        print('No todos left!')