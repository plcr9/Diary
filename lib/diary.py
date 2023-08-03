from math import ceil

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
        if self._entries == []:
            raise Exception("No entries added yet")
        word_count = self.count_words()
        return ceil(word_count/wpm)
    
    def find_best_entry_for_reading_time(self, wpm, minutes):
        words_the_user_could_read = wpm * minutes
        readable_entries = []
        for entry in self._entries:
            if entry.count_words() <= words_the_user_could_read:
                readable_entries.append(entry)
        if readable_entries == []:
            return None
        return readable_entries[0]