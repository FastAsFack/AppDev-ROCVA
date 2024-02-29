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
        new_todo = input('Enter the new todo: ')
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
    todos.append(new_todo)
    with open('todo_log.txt', 'a') as f:
        f.write(f'{datetime.datetime.now()}: {new_todo}\n')

def show_all_todos():
    if todos:
        for i, todo in enumerate(todos, start=1):
            print(f'{i}. {todo}')
    else:
        print('No todos left!')