from utils import load_todos, print_menu, clear_screen
from actions import show_next_todo, edit_todo, delete_todo, add_todo, show_all_todos

def main():
    load_todos()
    while True:
        clear_screen()
        print_menu()
        choice = input('Choose an option: ')
        if choice == '1':
            show_all_todos()
        elif choice == '2':
            show_next_todo()
        elif choice == '3':
            add_todo()
        elif choice == '4':
            edit_todo()
        elif choice == '5':
            delete_todo()
        elif choice == '6':
            break
        else:
            print('Invalid choice')
        input('Press enter to continue...')

if __name__ == '__main__':
    main()