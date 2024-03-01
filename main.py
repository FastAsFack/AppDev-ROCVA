from utils import *
from actions import *

def main():
    startup_page()
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
            help_todo()
        elif choice == '7':
            clear_screen()
            break
        else:
            print('Invalid choice')
        input('Press enter to continue...')

if __name__ == '__main__':
    main()