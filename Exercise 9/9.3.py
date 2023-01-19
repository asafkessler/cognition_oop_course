def poem_creator(dict_data):
    dict= {}
    s_song = ""

    for curr_key in dict_data:
        if isinstance(curr_key, int):
            dict[curr_key] = dict_data[curr_key]
        else:
            dict[dict_data[curr_key]] = curr_key

    my_keys = list(dict.keys())
    my_keys.sort()
    sorted_dict = {i: dict[i] for i in my_keys}

    for curr in sorted_dict.values():
        s_song += curr

    return s_song

if __name__ == '__main__':
    d = {'ppl':4, 2:'y e','es':5,3:'ats a','El':1}
    print(poem_creator(d))

