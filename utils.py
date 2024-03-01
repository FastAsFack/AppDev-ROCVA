import os
import time
from tqdm import tqdm
from colorama import Fore, Style


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

    print(Fore.GREEN + """
  _____                         _______        _                              _ _           _   _             
 |  __ \                       |__   __|      | |           /\               | (_)         | | (_)            
 | |__) |___   _____   ____ _     | | ___   __| | ___      /  \   _ __  _ __ | |_  ___ __ _| |_ _  ___  _ __  
 |  _  // _ \ / __\ \ / / _` |    | |/ _ \ / _` |/ _ \    / /\ \ | '_ \| '_ \| | |/ __/ _` | __| |/ _ \| '_ \ 
 | | \ \ (_) | (__ \ V / (_| |    | | (_) | (_| | (_) |  / ____ \| |_) | |_) | | | (_| (_| | |_| | (_) | | | |
 |_|  \_\___/ \___| \_/ \__,_|    |_|\___/ \__,_|\___/  /_/    \_\ .__/| .__/|_|_|\___\__,_|\__|_|\___/|_| |_|
                                                                 | |   | |                                    
                                                                 |_|   |_|                                    
                                                                 """)
    for i in tqdm(range(10), bar_format='{l_bar}{bar}'):
        time.sleep(0.5)
    clear_screen()