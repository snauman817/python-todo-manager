import item

class Manager(object):

    def __init__(self):
        pass
    
    def to_do(self, uncompleted_only = 0):
        file_obj = open('todos.txt', 'r')
        rows = file_obj.read().split('\n')

        for index in range(1, len(rows)):
            cols = rows[index].split('|')
            if uncompleted_only == 2:
                if cols[1] == 'True':
                    print('-'*10)
                    print(f"Task: {cols[0]}\nCompleted: {cols[1]}\nDue: {cols[2]}\nEntered: {cols[3]}")
            elif cols[1] == 'False' or uncompleted_only == 1:
                print('-'*10)
                print(f"Task: {cols[0]}\nCompleted: {cols[1]}\nDue: {cols[2]}\nEntered: {cols[3]}")


        file_obj.close()

    def add(self, task, due):
        self.write_to_database(item.Item(task, due))
    
    def write_to_database(self, new_task):
        file_obj = open('todos.txt', 'a')
        file_obj.write(f"\n{new_task.task}|{new_task.is_completed}|{new_task.datetime_due}|{new_task.datetime_created}")
        file_obj.close()

    def complete(self, task):
        task_dict = {}

        file_obj = open('todos.txt', 'r+')
        rows = file_obj.read().split('\n')
        
        for index in range(1, len(rows)):
            cols = rows[index].split('|')
            task_dict[cols[0]] = item.Item(cols[0], cols[2], cols[3], cols[1])
        
        task_dict[task].is_completed = True

        file_obj.truncate(0)

        file_obj.write('task|completed|date due|date entered')
        file_obj.close()

        for entry in task_dict:
            self.write_to_database(task_dict[entry])

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
        elif 'add' in command:
            task = input('task: ')
            due = input("due by: ")
            self.add(task, due)
        elif 'complete' or 'finish' in command:
            task = input("Which task would you like to finish? : ")
            self.complete(task)
        else:
            print("I did not understand that.")