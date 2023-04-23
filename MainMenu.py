from menuoption.MenuOption import MenuOption
import menuoption.ConvertYtToMp3 as ConvertYt

class MainMenu:
    def __init__(self):
        self.menu_options = {}

    def add_menu_option(self, key, menuOption):
        self.menu_options[key] = menuOption

    def add_option(self, key, name, function):
        self.menu_options[key] = MenuOption(name, function)

    def display(self):
        print("\nMain Menu:")
        for key, option in self.menu_options.items():
            print(f"{key}. {option.name}")

    def process_input(self, choice):
        if choice in self.menu_options:
            self.menu_options[choice].execute()
            return True
        else:
            print("Invalid option, please try again")
            return False

    def run(self):
        while True:
            self.display()
            choice = input("Please choose an option: ")

            if choice == 'q':
                print("Exiting...")
                break

            self.process_input(choice)


def function_1():
    print("Function 1 called")


def function_2():
    print("Function 2 called")


def function_3():
    print("Function 3 called")


def main():
    main_menu = MainMenu()
    main_menu.add_menu_option('0', ConvertYt.getMenuOption())
    main_menu.add_option('1', 'Call Function 1', function_1)
    main_menu.add_option('2', 'Call Function 2', function_2)
    main_menu.add_option('3', 'Call Function 3', function_3)
    main_menu.add_option('q', 'Quit', None)

    main_menu.run()


if __name__ == '__main__':
    main()
