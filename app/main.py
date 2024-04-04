from views.userinterface import UserInterface


def main():
    ''' Application initializer. '''
    ui: UserInterface = UserInterface()
    ui.render()


if __name__ == '__main__':
    main()