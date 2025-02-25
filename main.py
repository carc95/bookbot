from stats import get_num_words,character_count,convert_list_of_dicts,print_report
import sys

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
    return file_contents

def main():

    if (len(sys.argv) != 2):
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)    
    character_dict = character_count(text)    
    list_of_character_dicts = convert_list_of_dicts(character_dict)
    print_report(sys.argv[1],num_words,list_of_character_dicts)


main()
