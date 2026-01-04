from stats import get_book_text, get_char_amount, sort_dict, print_report


def main():
    file_location = "books/frankenstein.txt"
    text = get_book_text(file_location)
    words = text.split()
    word_count = len(words)
    char_count = get_char_amount(text)
    sorted_char_count = sort_dict(char_count)
    
    print_report(file_location, word_count, sorted_char_count)
    


if __name__ == "__main__":
    main()



