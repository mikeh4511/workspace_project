def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    char_count = {}
    for char in file_contents:
        char = char.lower()
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    char_list = [{"char": char, "num": count} for char, count in char_count.items()]
    def sort_on(dict):
        return dict["num"]
    char_list.sort(reverse=True, key=sort_on)
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
main()
