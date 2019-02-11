import datetime

class Item(object):

    def __init__(self, task, datetime_due, datetime_created = None, is_completed = None):
        self.task = task
        self.datetime_due = datetime_due
        # self.datetime_created = datetime.datetime.now()
        self.datetime_created = datetime_created
        if is_completed == 'False':
            self.is_completed = False
        elif is_completed == 'True':
            self.is_completed = True
        else:
            self.is_completed = is_completed

    def get_class_name(self):
        return 'Item'
