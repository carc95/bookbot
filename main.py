def main():
    path_to_book = "books/frankenstein.txt"
    text = get_book(path_to_book)
    word_count_text = word_count(text)
    character_dict = character_count(text)    
    list_of_character_dicts = convert_list_of_dicts(character_dict)
    print_report(path_to_book,word_count_text,list_of_character_dicts)

def get_book(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
    return file_contents

def word_count(file_contents):
    count = 0
    words = file_contents.split()
    for word in words:
        count += 1        
    return count

def character_count(text):
    count = 0
    character_dict = {}
    lowered_text = text.lower()    
    for character in lowered_text:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    
    return character_dict

def sort_on(dict):
   return dict["num"]

def convert_list_of_dicts(dict):
    list_of_dicts = []
    for character in dict:
        dict_indivual_values = {'character':character, 'num':dict[character]}
        if character.isalpha():
            list_of_dicts.append(dict_indivual_values)    
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def print_report(path_to_book,word_count_text,list_of_character_dicts):    
    print(f"--- Begin report of {path_to_book} ---")
    print(f"{word_count_text} words in the document.") 
    print("\n")
    for dict in list_of_character_dicts:
        print(f"The '{dict['character']}' character was found {dict['num']} times.")        
    print("--- End report --- ")
    
main()