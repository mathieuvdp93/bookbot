from stats import get_book_text


def main():
    text = get_book_text("books/frankenstein.txt")
    words = text.split()
    word_count = len(words)
    print(f"Found {word_count} total words")


if __name__ == "__main__":
    main()



