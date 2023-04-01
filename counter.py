import time


class Counter:

    def __init__(self, window=5):
        self.window = window
        self.records = []

    def record(self, time):
        if len(self.records) > self.window:
            del self.records[0]
        self.records.append(time)

    def average(self):
        return str(sum(self.records)/len(self.records))
