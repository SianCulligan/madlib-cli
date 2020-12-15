import re 

# -------GLOBAL VARIABLES---------
template_string = ""
language_parts = []
stripped_string = []
user_input_list = []



# -------DEFINE FUNCTIONS---------
def read_template(path): 
    try: 
        with open(path, 'r') as template:
            contents = template.read()
            template_string = str(contents)
            # print(contents)
            # contents_of_file.append(contents)
            return contents
    except FileNotFoundError: 
        raise FileNotFoundError ("File not found")


def parse_template(incoming_message):
    string = str(incoming_message)
    # collect language parts -> return tuple
    lang_objects = re.findall(r"\{.*?\}", string) 
    for i in lang_objects:
        result = (i[1:-1])
        language_parts.append(str(result))
    language_parts_to_tuple = tuple(language_parts)

    # remove language parts -> return string
    removed_result = re.sub(r"\{.*?\}", "{}", string)
    stripped_string.append(removed_result)
    string_return = ""
    for strings in removed_result:
        string_return += strings

    # ---------------return -----------------
    return (string_return, language_parts_to_tuple)




# ---------COLLECT USER INPUT---------


def user_inputs(list_of_language_parts): 
    for words in list_of_language_parts: 
        vowel = 'a'
        if words.lower().startswith(vowel):
            user_input_list.append(input("Type in an " + words.lower() + ": "))
        else:
            user_input_list.append(input("Type in a " + words.lower() + ": ")) 
    return user_input_list   





def merge(template, user_list):
    if isinstance(template, str) != True:
        unnest_once = ""
        unnest_again = ""

        for element in template:  
            unnest_once += element
        for element in unnest_once: 
            unnest_again +=element
        results = unnest_again.split()
    else: 
        results = template.split()
    # this is not pretty, I am very aware. But it works ¯\_(ツ)_/¯ 

    switch_from_tuple = list(user_list)
    complete_string = []
    current_index = 0
    

    # LOOPS THROUGH WORDS
    for i in results:   
        # IF WORD IS {}, REPLACE WITH A VALUE FROM USER INPUT, THEN INCREASE YOUR CURRENT INDEX
        if i.startswith('{}'):
            replace_a_bracket = i.replace('{}', switch_from_tuple[current_index], 1)
            complete_string.append(replace_a_bracket)
            current_index += 1
        elif i.startswith('{ }'):
            replace_a_bracket = i.replace('{ }', switch_from_tuple[current_index], 1)
            complete_string.append(replace_a_bracket)
            current_index += 1
        else:
            complete_string.append(i)
        
        # print(complete_string)    

    madlib_string = ""
    for each_word in complete_string:
        madlib_string += (each_word + " ")

    complete_madlib = madlib_string[:-1]
    print(complete_madlib)
    return complete_madlib 








# -------WELCOME MESSAGE---------

if __name__ == "__main__":
#   Code to run in the condition REMINDER - goes in at the bottom
    user_name = input(
    """Oh hello there! 

    Welcome to MadLibs

    What\'s your name? > """)

    print('Nice to meet you, ' + user_name + " (That's such a 102 thing to do. Annnnyways....)")

    welcome = input(
    """ Let's play! 

    It's not too hard - first you'll tell me which file you'd like to find, then I'll ask you to enter a series of words &, finally, I'll return your story.

    So which file do you want to access? If you don't know the path, just hit enter and I'll pick one for you. > """) or "assets/madlib_template.txt"


    contents_of_file = read_template(welcome)
    parse_template(contents_of_file)
    user_inputs(language_parts)
    merge(stripped_string, user_input_list)
