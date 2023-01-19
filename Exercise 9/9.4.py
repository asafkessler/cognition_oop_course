def poem_creator(dict_data):

    l_values = list(dict_data.values())
    l_ints = [x for x in l_values if isinstance(x, int)]
    min_value = min(l_ints)

    l_keys = list(dict_data.keys())
    for curr in l_keys:
        if curr > min_value:
            del dict_data[curr]

    return dict_data


if __name__ == '__main__':
    d = {1:4, 6:34, 3:'b', 2:17, 14:'c' }
    print(poem_creator(d))

