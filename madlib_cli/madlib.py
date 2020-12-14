# TODO Print a welcome message to the user, explaining the Madlib process and command line interactions
# DONE Create and test a read_template function that takes in a path to text file and returns a stripped string of the file’s contents.
# DONE Create and test a parse function that takes in a template string and returns a string with language parts removed and a separate list of those language parts.
# TODO Create and test a merge function that takes in a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template.

import re 

# -------GLOBAL VARIABLES---------
template_string = ""

language_parts = []
stripped_string = []




# -------WELCOME MESSAGE---------



# -------DEFINE FUNCTIONS---------
def read_template(path): 
    try: 
        with open(path, 'r') as template:
            contents = template.read()
            template_string = str(contents)
            print(contents)
            return contents
    except FileNotFoundError: 
        raise FileNotFoundError ("File not found")


# read_template('assets/madlib_template.txt')
# print("*******************************")
# print(template_string)


def parse_template(string):
    # ---------------collect language parts -> return tuple----------------
    lang_objects = re.findall(r"\{.*?\}", string) 
    for i in lang_objects:
        result = (i[1:-1])
        language_parts.append(str(result))
    language_parts_to_tuple = tuple(language_parts)

    # ---------------remove language parts -> return string-----------------
    removed_result = re.sub(r"\{.*?\}", "{}", string)
    stripped_string.append(removed_result)
    string_return = ""
    for strings in removed_result:
        string_return += strings

    # ---------------return -----------------
    return (string_return, language_parts_to_tuple)



# parse_template("It was a {Adjective} and {Adjective} {Noun}.")

# ---------COLLECT USER INPUT---------
user_input_list = []

def user_inputs(list_of_language_parts): 
    for words in list_of_language_parts: 
        vowel = 'a'
        if words.lower().startswith(vowel):
            user_input_list.append(input("Type in an " + words.lower() + ": "))
        else:
            user_input_list.append(input("Type in a " + words.lower() + ": ")) 
    return user_input_list   


# user_inputs(["Adjective", "noun", "Verb"])


def merge(template, user_list):
    #takes in a bare template & user inputs
    # loop through the result of language_parts_to_tuple temp - for each thing in the list - generate a list of req input messages for user
    # print(user_list)
    switch_from_tuple = list(user_list)
    # print("SWITCH")
    # print(switch_from_tuple)
    complete_string = []
    # template_replace = template
    
    current_index = 0
    # //add to only if replaced

    res = template.split()

# LOOPS THROUGH WORDS
    for i in res:   
        # IF WORD IS [], REPLACE WITH A VALUE FROM USER INPUT, THEN INCREASE YOUR CURRENT INDEX
        if i.startswith('{}'):
            replace_a_bracket = i.replace('{}', switch_from_tuple[current_index], 1)
            # complete_string.append(switch_from_tuple[current_index])
            complete_string.append(replace_a_bracket)
            # print(switch_from_tuple[current_index])
            # print('------')
            # print(current_index)
            current_index += 1
        else:
            complete_string.append(i)
        
        print(complete_string)    

    madlib_string = ""
    for each_word in complete_string:
        madlib_string += (each_word + " ")

    complete_madlib = madlib_string[:-1]
    
    # for i in switch_from_tuple:
    #     print("******")
    #     print(template)
    #     print("******")
    #     print(i)
    #     # complete_string = re.sub(r"\{.*?\}", "i")
    #     replace_a_bracket = template.replace("{}", i, 1)
    #     complete_string.append(replace_a_bracket)
    #     template_replace = template.replace("{}", i, 1)
    #     print("******COMPLETE STRING")
    #     print(complete_string)        
    #     print("******TEMP REPLACE")
    #     print(template_replace)


    # # LOOPS THROUGH LETTERS IN TEMPLATE
    # for i in template:
    


    return complete_madlib 

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
