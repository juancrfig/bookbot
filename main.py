import sys
from stats import count_words, count_chars, sort_dicts


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    
    lst_of_dic = sort_dicts(count_chars(text))
    for dic in lst_of_dic:
        print(f"{dic['char']}: {dic['num']}")

    print("============= END ===============")



main()
