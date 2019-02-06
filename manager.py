import item

class Manager(object):

    def __init__(self):
        self.list = []
    
    def to_do(self):
        file_obj = open('todos.txt', 'r')
        rows = file_obj.read().split('\n')

        for index in range(1, len(rows)):
            cols = rows[index].split('|')

            print('-'*10)
            print(f"Task: {cols[0]}\nCompleted: {cols[1]}\nDue: {cols[2]}\nEntered: {cols[3]}")

        file_obj.close()

    def add(self):
        file_obj = open('todos.txt', 'a')

        task = input('task: ')
        due = input("due by: ")

        new_task = item.Item(task, due)

        file_obj.write(f"\n{new_task.task}|{new_task.is_completed}|{new_task.datetime_due}|{new_task.datetime_created}")

        file_obj.close()

manager = Manager()
manager.to_do()