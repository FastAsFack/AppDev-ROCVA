import os
import time

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
    print("6. Help")
    print("7. Exit")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def help_todo():
    print("Help")
    print("----")
    print("This is a simple todo application.")
    print("You can add, edit, and delete todos.")
    print("You can also show all todos or just the next one.")

def startup_page():
#     print("""
# ██████╗  ██████╗  ██████╗██╗   ██╗ █████╗     ████████╗ ██████╗ ██████╗  ██████╗      █████╗ ██████╗ ██████╗ ██╗     ██╗ ██████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
# ██╔══██╗██╔═══██╗██╔════╝██║   ██║██╔══██╗    ╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗    ██╔══██╗██╔══██╗██╔══██╗██║     ██║██╔════╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
# ██████╔╝██║   ██║██║     ██║   ██║███████║       ██║   ██║   ██║██║  ██║██║   ██║    ███████║██████╔╝██████╔╝██║     ██║██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║
# ██╔══██╗██║   ██║██║     ╚██╗ ██╔╝██╔══██║       ██║   ██║   ██║██║  ██║██║   ██║    ██╔══██║██╔═══╝ ██╔═══╝ ██║     ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
# ██║  ██║╚██████╔╝╚██████╗ ╚████╔╝ ██║  ██║       ██║   ╚██████╔╝██████╔╝╚██████╔╝    ██║  ██║██║     ██║     ███████╗██║╚██████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
# ╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚═══╝  ╚═╝  ╚═╝       ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝     ╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
#     """)
    print("Welcome to the Todo App!")
    for i in range(3):
        print(".", end='', flush=True)
        time.sleep(1)  # Simulate a delay for the loading process
    clear_screen()