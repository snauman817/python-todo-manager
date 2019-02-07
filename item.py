import datetime

class Item(object):

    def __init__(self, task, datetime_due, datetime_created = None, is_completed = None):
        self.task = task
        self.datetime_due = datetime_due
        if datetime_created is None:
            self.datetime_created = datetime.datetime.now()
        else:
            self.datetime_created = datetime_created

        if is_completed is None:
            self.is_completed = False
        else:
            self.is_completed = is_completed
