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
    print("\nMenu Options:")
    print("-------------")
    print("1. Show all todos")
    print("2. Show next todo")
    print("3. Add new todo")
    print("4. Edit todo")
    print("5. Delete todo")
    print("6. Exit")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')