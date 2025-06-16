from stats import get_book_text
from stats import get_num_words
from stats import get_num_of_each_char
from stats import get_list_of_char_count

import sys


def sort_on(dict):
    return dict["num"]

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book_text = get_book_text(sys.argv[1])
    print(f"Analyzing book found at {sys.argv[1]}")
    num_words = get_num_words(book_text)
    print ("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_of_each_char = get_num_of_each_char(book_text)
    list_of_char_count = get_list_of_char_count(num_of_each_char)
    list_of_char_count.sort(reverse=True,key=sort_on)
    for entry in list_of_char_count:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")

main()