def list_to_dict(L1, L2):
    new_dict = {}
    for value in L1:
        if L2.__contains__(value):
            new_dict.update({value: ("L1", "L2")})
        else:
            new_dict.update({value: ("L1")})

    for value in L2:
        if not new_dict.keys().__contains__(value):
            new_dict.update({value: ("L2")})

    return  new_dict

if __name__ == '__main__':
    L1 = [1, 2, 'a', 'b']
    L2 = [2, 3, 'b', 'c', 'd']

    print(list_to_dict(L1, L2))