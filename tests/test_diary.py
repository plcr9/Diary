import pytest
from lib.diary import Diary

'''Initially, there is an empty list of entries'''
def test_initially_has_empty_list_of_entries():
    diary = Diary()
    assert diary.all() == []

'''Initially, word count is zero'''
def test_initially_word_count_is_zero():
    diary = Diary()
    assert diary.count_words() == 0

'''Initially, reading time should raise an error'''
def test_initially_reading_time_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.reading_time(2)
    assert str(err.value) == "No entries added yet"

'''Initially, find_best_entry_for_reading_time should raise an error'''
def test_initially_find_best_entry_for_reading_time_raises_an_error():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.find_best_entry_for_reading_time(2, 2)
    assert str(err.value) == "No entries added yet"