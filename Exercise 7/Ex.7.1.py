def set_dictionary(user_dict, user_set):
    '''

    :param user_dict:
    :param user_group:
    :return:
    '''
    new_dict = {}

    keys = dict(user_dict).keys()

    for key in keys:
        curr_value = dict(user_dict).get(key)
        if set(user_set).__contains__(key) & \
                set(user_set).__contains__(curr_value):
            new_dict.update({key : curr_value})
            set(user_set).remove(key)
            set(user_set).remove(curr_value)
        else:
            mid_key = 0
            mid_value = 0
            less_value = 0
            less_key = 0

            if isinstance(key, int):
                if (key % 2 == 0) & \
                        (len(curr_value) % 2 == 0):
                    mid_key = int(key / 2)
                    mid_value = str(curr_value)[int(len(curr_value)/2):len(curr_value)]
                else:
                    less_key = key - 1
                    less_value = str(curr_value)[0:len(curr_value)-1]
            elif isinstance(curr_value, int):
                if (curr_value % 2 == 0) & \
                        (len(key) % 2 == 0):
                    mid_value = int(curr_value / 2)
                    mid_key = str(key)[int(len(key) / 2) : len(key)]
                else:
                    less_value = curr_value - 1
                    less_key = str(key)[0:len(key)-1]

            if (mid_value != 0) & (mid_key != 0):
                new_dict.update({mid_key: mid_value})
            if (less_key != 0) & (less_value != 0):
                new_dict.update({less_key: less_value})


    return new_dict



if __name__ == '__main__':
    user_dict = {3: 'table', 'chairs': 6, 'road': 5, 6: "sun", "python": 3, 8: "Mali", 4: 'Iosi'}
    user_set =  {'Iosi', 7, 5, 'road', 'day', 12, 4}

    print(set_dictionary(user_dict, user_set))