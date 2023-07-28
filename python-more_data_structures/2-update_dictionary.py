def update_dictionary(a_dictionary:dict, key:str, value):
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary.update({key: value})
