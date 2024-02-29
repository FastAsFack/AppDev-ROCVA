import os

todos = []

def load_todos():
    try:
        with open('todo_log.txt', 'r') as f:
            for line in f:
                date, todo = line.strip().split(': ', 1)
                todos.append(todo)
    except FileNotFoundError:
        pass

def print_menu():
    print("\n1. Show next todo")
    print("2. Edit todo")
    print("3. Delete todo")
    print("4. Add new todo")
    print("5. Show all todos")
    print("6. Exit")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')