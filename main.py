def main():
    name = set_book_name()
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)   
    text = file_contents

    num_words = get_count_words(text)
    num_chars = get_count_letters(text)
    char_sorted_list = sorted_list(num_chars)

    print(f"-----BOOK REPORT for {name}----")
    print(f"{num_words} words in book")
    print()

    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("----END REPORT----")

    


#takes text from book as string and returns
# number of words in the string
def get_count_words(text):
    words = text.split()
    return len(words)

#takes text from book as a string and returns
# number of times each character appears in the string
def get_count_letters(text):
    chars = {}
    for c in text:
        lowercase = c.lower()
        if lowercase in chars:
            chars[lowercase] += 1
        else:
            chars[lowercase] = 1
    return chars

#returns key "num" of passed in dictionary
def sort_on(dict):
    return dict["num"]

# returns a sorted list of dictionaries with char and num keys
def sorted_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "num": chars_dict[char]})
        #reverse=true: sorts list in descending order
        #key=sort_on: specifies the sort_on function used to extract a comparison key
        # from each list element
        # not to get confued by sorted() method which explicitily returns a new sorted list instance
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

#sets name of book for report
def set_book_name():
    name  = input("Enter name of book\n")
    return name


main()
