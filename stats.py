def get_book_text(fp):
    with open(fp) as f:
        return f.read()

def get_char_amount(text):
    result = {}

    text = text.lower()

    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result

def sort_dict(char_amount):
    sorted_char_amount = sorted(char_amount.items(),key = lambda char_amount: char_amount[1], reverse=True)

    return sorted_char_amount

def print_report(file_location, word_count, sorted_char_count):

    print("============ BOOKBOT ============")
    print(f"Analyzing books found at {file_location}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for index in sorted_char_count:
        if index[0].isalpha():
            print(f"{index[0]}: {index[1]}\n")

    print("============= END ===============\n")
