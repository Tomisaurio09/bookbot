from stats import count_words, count_characters, sort_dictionary
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    get_string = get_book_text(path)
    num_words = count_words(get_string)
    num_characters = count_characters(get_string)
    sorted_dictionary = sort_dictionary(num_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_dictionary:
        if dict["characther"].isalpha():
            print(f"{dict["characther"]}: {dict["count"]}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()