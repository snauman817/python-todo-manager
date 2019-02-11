class Project(object):
    
    def __init__(self, name, is_complete):
        self.items_list = []
        self.name = name

    def add_task(self, task):
        self.items_list.append(task)

    def complete_task(self, task):
        for thing in self.items_list:
            if thing.task == task:
                thing.is_complete = True
        
        if self.project_complete():
            self.is_complete = True
    
    def project_complete(self):
        for thing in self.items_list:
            if thing.is_complete == False:
                return False
        
        return True