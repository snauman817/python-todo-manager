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


    # def string_to_datetime(self, datetime_string):
    #     date_and_time = datetime_string.split(" ")
    #     date = date_and_time[0]
    #     time = date_and_time[1]

    #     date_list = date.split("-")
    #     time_list = time.split(":")

    #     return datetime.datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]), int(time_list[0]), int(time_list[1]), int(time_list[2]))
