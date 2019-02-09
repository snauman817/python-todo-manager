import item
import datetime

class Manager(object):

    def __init__(self):
        file_obj = open('todos.txt', 'r')
        self.item_list = []
        for line in file_obj.readlines():
            cols = line.split('|')
            self.item_list.append(item.Item(cols[0], cols[2], cols[3].split('\n')[0], cols[1]))

        file_obj.close()
    
    def to_do(self, uncompleted_only = 0):
        for thing in self.item_list:
            if uncompleted_only == 2:
                if thing.is_completed == True:
                    print('-'*10)
                    print(f"Task: {thing.task}\nCompleted: {thing.is_completed}\nDue: {thing.datetime_due}\nEntered: {thing.datetime_created}")
            elif thing.is_completed == False or uncompleted_only == 1:
                print('-'*10)
                print(f"Task: {thing.task}\nCompleted: {thing.is_completed}\nDue: {thing.datetime_due}\nEntered: {thing.datetime_created}")


    def add(self, task, due):
        self.item_list.append(item.Item(task, due, datetime.datetime.now(), False))
    
    def save(self):
        file_obj = open('todos.txt', 'w')
        for thing in self.item_list:
            file_obj.write(f"{thing.task}|{thing.is_completed}|{thing.datetime_due}|{thing.datetime_created}\n")
        
        file_obj.close()

    def complete(self, task):
        for thing in self.item_list:
            if thing.task == task:
                thing.is_completed = True
                break
    
    def clear(self):
        self.item_list = []

        file_obj = open('todos.txt', 'w')
        file_obj.write('')
        file_obj.close()

    def interact(self, command):
        if 'help' in command:
            print("---------COMMANDS---------")
            print("list: display the to-do list")
            print("optional parameters:")
            print("\tall: displays finished tasks as well as completed tasks")
            print("\tdone: displays only finished tasks")
            print(" ")
            print("add: brings up a prompt which asks you for the task and the due time/date")
            print(" ")
            print("complete: brings up a prompt which asks you for the task you would like to be completed")
            print(" ")
            print("quit: quits out of the program")
            print("--------------------------")
        elif 'list' in command:
            if 'all' in command:
                self.to_do(1)
            elif 'done' in command:
                self.to_do(2)
            else:
                self.to_do()
        elif 'clear' in command:
            self.clear()
        elif 'add' in command:
            task = input('task: ')
            due = input("due by: ")
            self.add(task, due)
        elif 'complete' or 'finish' in command:
            task = input("Which task would you like to finish? : ")
            self.complete(task)
        else:
            print("I did not understand that.")