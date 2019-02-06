import datetime

class Item(object):

    def __init__(self, task, datetime_due):
        self.task = task
        self.is_completed = False
        self.datetime_due = self.string_to_datetime(datetime_due)
        self.datetime_created = datetime.datetime.now()

    def string_to_datetime(self, datetime_string):
        date_and_time = datetime_string.split(" ")
        date = date_and_time[0]
        time = date_and_time[1]

        date_list = date.split("-")
        time_list = time.split(":")

        return datetime.datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]), int(time_list[0]), int(time_list[1]), int(time_list[2]))
