import datetime


class MyDate:

    def __init__(self, raw_date):
        self.ref = raw_date.split("/")

    def is_valid(self):
        if len(self.ref) == 3:
            return True
        return False

    def get_date(self):
        return datetime.date(int(self.ref[2]), int(self.ref[1]), int(self.ref[0]))


class MyTime:

    def __init__(self, raw_time):
        self.val = raw_time.split(":")

    def is_valid(self):
        if len(self.val) == 2:
            return True
        return False

    def get_val(self):
        dt =datetime.date.today()
        
        return datetime.datetime(datetime.date.year, datetime.date.month, datetime.date.day, int(self.val[0]), int(self.val[1]), 0)
