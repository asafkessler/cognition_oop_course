
def dict_sum(user_dict):
    helper = dict(user_dict)
    sum = 0
    for value in helper.values():
        if isinstance(value, int) or \
                isinstance(value, float):
            sum += value

    return sum



if __name__ == '__main__':
    user_dict = {"q" : 8, (1, 2) : (3, 4), "list" : [7], 'Hi' : 0.6}
    print(dict_sum(user_dict))