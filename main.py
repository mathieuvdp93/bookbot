from stats import get_book_text, get_char_amount


def main():
    text = get_book_text("books/frankenstein.txt")
    #words = text.split()
    #word_count = len(words)
    #print(f"Found {word_count} total words")
    char_count = get_char_amount(text)
    print(char_count)



if __name__ == "__main__":
    main()



