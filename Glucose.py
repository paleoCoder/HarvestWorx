# basic class to hold glucose readings
class Glucose:
    def __init__(self, date, mgdl):
        self.date = date
        self.mgdl = mgdl

    def __str__(self):
        return '{0} - {1}'.format(self.date, self.mgdl)
