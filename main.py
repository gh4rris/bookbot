def main():
    file_contents = get_text()
    words = word_count(file_contents)
    characters = character_count(file_contents)
    characters_split = dict_split(characters)
    characters_split.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words in the document")
    for character in characters_split:
        print(f"The '{character["name"]}' character was found '{character["value"]}' times")
    print("--- End report ---")

def word_count(text):
    count = 0
    word_list = text.split()
    for word in word_list:
        count += 1
    return count

def character_count(text):
    letter_dict = {}
    lower_text = text.lower()
    for letter in lower_text:
        letter_dict[letter] = 0
    for letter in lower_text:
        letter_dict[letter] += 1
    return letter_dict

def dict_split(characters):
    character_dict_list = []
    for character in characters:
        if character.isalpha():
            character_dict = {}
            character_dict["name"] = character
            character_dict["value"] = characters[character]
            character_dict_list.append(character_dict)
    return character_dict_list

def sort_on(characters_split):
    return characters_split["value"]

def get_text():
    with open("books/frankenstein.txt") as f:
        return f.read()

if __name__ == "__main__":
    main()