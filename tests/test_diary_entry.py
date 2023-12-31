from lib.diary_entry import DiaryEntry 

'''When initialising title and contents, it returns title and contents'''
def test_constructs_and_gets_title_and_contents():
    diary_entry = DiaryEntry("My Title", "My Contents")
    assert diary_entry.title == "My Title"
    assert diary_entry.contents == "My Contents"

'''When initialise with 5 word contents, count_words should return 5'''
def test_count_words_returns_word_count_of_contents():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    assert diary_entry.count_words() == 5

'''When initialise with 5 words contents, reading_time with wpm of 2 should return 3'''
def test_reading_time():
    diary_entry = DiaryEntry("My Title", "One Two Three Four Five")
    assert diary_entry.reading_time(2) == 3

'''When initialise with 5 words contents, at first reading_chunk should return first chunk'''
def test_readable_chunk_first_chunk():
    diary_entry = DiaryEntry("My Title", "One Two Three Four Five")
    assert diary_entry.reading_chunk(2, 1) == "One Two"

'''When initialise with 5 words contents, on second call, reading_chunk should return second chunk'''
def test_readable_chunk_second_chunk():
    diary_entry = DiaryEntry("My Title", "One Two Three Four Five")
    assert diary_entry.reading_chunk(2, 1) == "One Two"
    assert diary_entry.reading_chunk(2, 1) == "Three Four"

'''When initialise with 5 words contents, on third call, reading_chunk should return final, partial chunk'''
def test_readable_chunk_third_chunk():
    diary_entry = DiaryEntry("My Title", "One Two Three Four Five")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "Five"

'''When initialise with 5 words contents, on fourth call, reading_chunk should start again from beginning'''
def test_readable_chunk_fourth_chunk():
    diary_entry = DiaryEntry("My Title", "One Two Three Four Five")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "One Two"

'''When initialise with 6 words contents, on fourth call, reading_chunk should start again from beginning'''
def test_readable_chunk_fourth_chunk_with_six_words():
    diary_entry = DiaryEntry("My Title", "One Two Three Four Five Six")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "One Two"

