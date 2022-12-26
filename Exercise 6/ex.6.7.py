
def dict_sum(user_dict):
    helper = dict(user_dict)
    sum = 0
    for value in helper.keys():
        if isinstance(value, int):
            if value % 2 == 0 and \
                    (isinstance(helper.get(value), str) or \
                     isinstance(helper.get(value), set)):
                sum += value

    return sum



if __name__ == '__main__':
    user_dict = {1:2, 'abc':3}
    print(dict_sum(user_dict))