def get_num_words(booktext):
    words = booktext.split()
    num_words = len(words)
    return num_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_num_of_each_char(booktext):
    words = booktext.split()
    num_of_each_char = {}
    for word in words:
        for char in word:
            num_of_each_char[char.lower()] = num_of_each_char.get(char.lower(),0)+1
    return num_of_each_char

def get_list_of_char_count(dict):
    list_of_char = []
    for entry in dict:
        temp_list = {"char":entry, "num" : dict[entry]}
        list_of_char.append(temp_list)
    return list_of_char