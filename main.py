import os, pickle
from pyfiglet import Figlet

filename = 'C:\\python_projects\\area\\ToDoApp\\tasks'
banners = ['What next?', 'Taskmaster', '']


class System:
    def __init__(self, tasklist):
        self.taskList = tasklist
        self.f = Figlet(font='slant')
        self.menu()

    def banner(self, type):
        if type == 1:
            print(self.f.renderText('Taskmaster'))
        elif type == 2:
            print(self.f.renderText('What next?'))
        elif type == 3:
            print(self.f.renderText('Let\'s see...'))
        elif type == 4:
            print(self.f.renderText('Another down!'))

    def save(self):
        with open(filename, 'wb') as f:
            pickle.dump(self.taskList, f)

    def clearScreen(self):
        os.system('cls')

    def confirm(self):
        input('\nPress enter to continue...')

    def menu(self):
        self.clearScreen()
        self.banner(1)
        print('Press enter to view tasks')
        print('Enter space to add a task')
        self.checkMenu(input('\n: '))

    def checkMenu(self, choice):
        if choice == ' ':
            print('Adding task...')
            self.addTask()
        else:
            print('\nViewing tasks...')
            self.viewTasks()

    def addTask(self):
        self.clearScreen()
        self.banner(2)
        name = str(input('\nDescription (0 to cancel) : '))
        if name == '0':
            self.menu()
        else:
            self.taskList.append(Task(name))
            self.save()
            self.confirm()
            self.menu()

    def viewTasks(self):
        self.clearScreen()
        self.banner(3)
        if len(self.taskList) == 0:
            print('\nNo tasks')
            self.confirm()
            self.menu()
        else:
            print('')
            for task in self.taskList:
                print('')
                print(f'- {task.getDescription()}')
            self.confirm()
            print('\nEnter space to delete a task')
            print('Press enter to return to menu')
            choice = input('\n: ')
            if choice == ' ':
                self.deleteTask()
            else:
                self.menu()

    def deleteTask(self):
        self.clearScreen()
        self.banner(4)
        counter = 0
        for task in self.taskList:
            counter += 1
            print('')
            print(f'{counter} - {task.getDescription()}')
        print('')
        try:
            reqDel = int(input('Enter number of task you would like to delete (0 to cancel) : '))
            if reqDel == 0:
                self.menu()
            self.taskList.remove(self.taskList[reqDel - 1])
        except (IndexError, ValueError) as e:
            print('\nError - The number inputted isn\'t a valid task number')
            print(f'Details - {e}')
            self.confirm()
            self.clearScreen()
            self.deleteTask()
        self.save()
        self.confirm()
        self.menu()


class Task:
    def __init__(self, name):
        self.name = name

    def getDescription(self):
        return self.name


if __name__ == '__main__':
    if os.path.getsize(filename) == 0:
        data = []
    else:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
    sys = System(data)
