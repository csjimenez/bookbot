def main():
    book_path = "books/frankenstein.txt"

    print(f"--- Begin report of {book_path} ---")

    text = get_book_text(book_path)

    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    print()

    char_dict = get_chars(text)
    char_count_list = dict_to_list(char_dict)
    char_count_list.sort(reverse=True, key=sort_on)
    
    for dict in char_count_list:
        name = dict["name"]
        num = dict["num"]
        if not name.isalpha():
            continue
        print(f"The '{name}' character was found {num} times")

    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars(string):
    char_dict = {}

    for c in string.lower():
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict.update({c: 1})

    return char_dict

def dict_to_list(dict):
    mylist = []
    for key in dict:
        mylist.append({"name": key, "num": dict[key]})

    return mylist

def sort_on(dict):
    return dict["num"]

main()
