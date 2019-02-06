import item

class Manager(object):

    def __init__(self):
        self.list = []
    
    def to_do(self):
        self.list = []

        file_obj = open('todos.txt', 'r')
        rows = file_obj.read().split('\n')

        for index in range(1, len(rows)):
            cols = rows[index].split('|')
            obj = item.Item(cols[0], cols[2], cols[3], cols[1])
            self.list.append(obj)
        
        for entry in self.list:
            print("-"* 10)
            print(f"Task: {entry.task}\nCompleted: {entry.is_completed}\nDue: {entry.datetime_due}\nEntered: {entry.datetime_created}")

        file_obj.close()

    def add(self):
        file_obj = open('todos.txt', 'a')

        task = input('task: ')
        due = input("due by (format YYYY-MM-DD HH:MM:SS): ")

        new_task = item.Item(task, due)

        file_obj.write(f"\n{new_task.task}|{new_task.is_completed}|{new_task.datetime_due}|{new_task.datetime_created}")

        file_obj.close()

manager = Manager()
manager.to_do()