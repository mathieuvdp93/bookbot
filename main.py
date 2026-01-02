def get_book_text(fp):
    with open(fp) as f:
        return f.read()


def main():
    text = get_book_text("books/frankenstein.txt")
    words = text.split()
    word_count = len(words)
    print(f"Found {word_count} total words")


if __name__ == "__main__":
    main()



