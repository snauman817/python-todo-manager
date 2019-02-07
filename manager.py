import item

class Manager(object):

    def __init__(self):
        pass
    
    def to_do(self):
        file_obj = open('todos.txt', 'r')
        rows = file_obj.read().split('\n')

        for index in range(1, len(rows)):
            cols = rows[index].split('|')
            if cols[1] == 'False':
                print('-'*10)
                print(f"Task: {cols[0]}\nCompleted: {cols[1]}\nDue: {cols[2]}\nEntered: {cols[3]}")

        file_obj.close()

    def add(self):
        task = input('task: ')
        due = input("due by: ")
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
            task_dict[cols[0]] = item.Item(cols[0], cols[2], cols[1], cols[3])
        
        task_dict[task].is_completed = True

        file_obj.write('task|completed|date due|date entered')
        file_obj.close()

        for entry in task_dict:
            self.write_to_database(entry)


manager = Manager()
manager.complete('shopping')