from stats import get_book_text, get_char_amount, sort_dict, print_report, check_correct_input
import sys


def main():
    if not check_correct_input(sys.argv):
        sys.exit(1) 
    file_location = sys.argv[1]
    text = get_book_text(file_location)
    words = text.split()
    word_count = len(words)
    char_count = get_char_amount(text)
    sorted_char_count = sort_dict(char_count)
    
    print_report(file_location, word_count, sorted_char_count)
    


if __name__ == "__main__":
    main()



