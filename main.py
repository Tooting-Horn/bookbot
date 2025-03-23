import sys
from stats import get_num_words, get_num_chars, sort_num_chars

def get_book_text(book_filepath):
    with open(book_filepath) as book:
        book_contents = book.read()
    return book_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_location = sys.argv[1]
        book_text = get_book_text(book_location)

        # print header text
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_location}...")

        # print number of words
        num_words = get_num_words(book_text)
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")

        # print number of characters
        char_dict = get_num_chars(book_text)
        sorted_char_list = sort_num_chars(char_dict)
        print("--------- Character Count -------")
        for dict in sorted_char_list:
            if dict["char"].isalpha():
                print(f"{dict["char"]}: {dict["num"]}")

        # print footer text
        print("============= END ===============")

main()
