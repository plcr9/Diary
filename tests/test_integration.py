from lib.diary import Diary 
from lib.diary_entry import DiaryEntry

'''Given two diary entries, they are returned in a list'''
def test_adds_and_lists_diary_entries():
    diary_entry = DiaryEntry("My Title", "My Contents")
    assert diary_entry.title == "My Title"
    assert diary_entry.contents == "My Contents"

'''If two diary entries added, if count_words called, it returns the sum of all words in the contents of the diary entries'''
def test_count_words_returns_count_of_all_words_in_all_entry_contents():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "One Two")
    entry_2 = DiaryEntry("My Title 2", "Three Four Five")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 5