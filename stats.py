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
