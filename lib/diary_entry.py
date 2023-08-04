from math import ceil

class DiaryEntry():
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        return ceil(self.count_words()/wpm)