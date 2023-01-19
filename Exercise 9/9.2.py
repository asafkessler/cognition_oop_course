def poem_creator(list_cuts, tuple_cuts):
    s_song = ""
    for curr in tuple_cuts:
        list_cuts.append(curr)

    dict= {}
    for index in range(1, len(list_cuts), 2):
        dict[list_cuts[index]-1] = list_cuts[index-1]

    my_keys = list(dict.keys())
    my_keys.sort()
    sorted_dict = {i: dict[i] for i in my_keys}

    for curr in sorted_dict.values():
        s_song += curr

    return s_song


if __name__ == '__main__':

    T = ('s.', 9, 'ate y', 2, 'I h', 1, 't no', 6)
    L =  ['og', 3, 'es', 8, 'urt, ', 4, 't ch', 7, 'bu', 5]
    print(poem_creator(L, T))