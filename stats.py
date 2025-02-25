def get_num_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1        
    return count

def character_count(text):    
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
    print("=========== BOOKBOT =============")    
    print(f"Analyzing book found at {path_to_book}...")
    print("---------- Word Count -----------")
    print(f"Found {word_count_text} total words") 
    print("-------- Character Count --------")
    for dict in list_of_character_dicts:
        print(f"{dict['character']}: {dict['num']}")        
    print("============ END ================")