def get_num_words(input_string):
    words_list = input_string.split()
    return len(words_list)

def get_num_chars(input_string):
    char_dict = {}
    for char in input_string.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_num_chars(char_dict):
    # create list of dictionaries
    char_list = []
    for char, num in char_dict.items():
        char_list.append({"char": char, "num": num})
    
    # sort list of dictionaries
    char_list.sort(reverse = True, key = sort_on)

    return char_list

    

