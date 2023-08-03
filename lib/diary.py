import math

class Diary():
    def __init__(self):
        self._entries = []

    def add(self, entry):
        self._entries.append(entry)

    def all(self):
        return self._entries

    def count_words(self):
        word_counts = ([entry.count_words() for entry in self._entries])
        return sum(word_counts)

    def reading_time(self, wpm):
        word_count = self.count_words()
        return math.ceil(word_count/wpm)