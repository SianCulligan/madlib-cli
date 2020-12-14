# TODO Print a welcome message to the user, explaining the Madlib process and command line interactions
# DONE Create and test a read_template function that takes in a path to text file and returns a stripped string of the file’s contents.
# DONE Create and test a parse function that takes in a template string and returns a string with language parts removed and a separate list of those language parts.
# TODO Create and test a merge function that takes in a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template.

import re 

# -------GLOBAL VARIABLES---------
template_string = ""
contents_of_file = []
language_parts = []
stripped_string = []
user_input_list = []


# -------WELCOME MESSAGE---------

user_name = input(
"""Oh hello there! 

Welcome to MadLibs

What\'s your name? > """)

print('Nice to meet you, ' + user_name + " (That's such a 102 thing to do. Annnnyways....)")

welcome = input(
""" Let's play! 

It's not too hard - first you'll tell me which file you'd like to find, then I'll ask you to enter a series of words &, finally, I'll return your story.

So which file do you want to access? If you don't know the path, just hit enter and I'll pick one for you. > """) or "assets/madlib_template.txt"




# -------DEFINE FUNCTIONS---------
def read_template(path): 
    try: 
        with open(path, 'r') as template:
            contents = template.read()
            template_string = str(contents)
            # print(contents)
            contents_of_file.append(contents)
            return contents
    except FileNotFoundError: 
        raise FileNotFoundError ("File not found")


read_template(welcome)



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

parse_template(contents_of_file)


# ---------COLLECT USER INPUT---------


def user_inputs(list_of_language_parts): 
    for words in list_of_language_parts: 
        vowel = 'a'
        if words.lower().startswith(vowel):
            user_input_list.append(input("Type in an " + words.lower() + ": "))
        else:
            user_input_list.append(input("Type in a " + words.lower() + ": ")) 
    return user_input_list   

user_inputs(language_parts)
# user_inputs(["Adjective", "noun", "Verb"])


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
        else:
            complete_string.append(i)
        
        print(complete_string)    

    madlib_string = ""
    for each_word in complete_string:
        madlib_string += (each_word + " ")

    complete_madlib = madlib_string[:-1]
    print(complete_madlib)
    return complete_madlib 


merge(stripped_string, user_input_list)




























# merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
# Stretch Goals
# TODO Figure out / research a way to verify terminal input/output.
# TODO Test that completed madlib is properly written to disk with correct content.

    # print(stripped_string.join(removed_result))
    # listToStr = stripped_string.join([str(elem) for elem in removed_result])
    
    # regex = re.compile(r'\{.*?\}')
    # result = re.findall(regex, string)
    # new_list = []
    # for i in result:
    #     new_list.append(i)
    #     print(new_list)
    # mystring = "This is a sentence. (once a day) [twice a day] {three times}"

    # regex = re.compile(".*?\((.*?)\)")
    # result = re.findall(regex, mystring)
    # split = string.split()
    # print('**************************************')
    # print(split)
    # language_parts =[]
    # remainder = []
    # for i in split:
    #     if i.startswith('{') == True:
    #         language_parts.append(i)
    #     elif i.endswith('}') == True:  
    #         language_parts.append(i)
    #     else:
    #         remainder.append(i)
    # res = re.findall(r'\(.*?\)', string)
    # res = [str(idx) for idx in eval(string) if isinstance(idx, tuple)] 
    # print('**************************************')
    # print(remainder)
    # print('**************************************')
    # print(language_parts)
    # print('**************************************')
    # print("RES")
    # print(language_parts)
    # print('**************************************')
    # print("ORIG " + string)
    # test_str = "geeks{For}geeks is {best}"
    # test_str = "geeks{For}geeks is {best}"
    # printing original string 
    
    # Extract substrings between brackets 
    # Using regex 
    # printing result  
    # for words in split:
    #     print(words)
    # loop through the string
    # split the string
    # check the index
    # if it's in the 'language'list, append to new_list
    # if it's not in the lang list, .pop it off the list
    # return 
