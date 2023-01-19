
def f5_11(L):
    lists_ints, lists_float, lists_strs = [], [], []

    if not L:
        return L
    else:
        for curr_value in L:
            if isinstance(curr_value, int):
                lists_ints.append(curr_value)
            elif isinstance(curr_value, float):
                lists_float.append(curr_value)
            elif isinstance(curr_value, str):
                lists_strs.append(curr_value)
            else:
                break

    return lists_ints, lists_float, lists_strs # the way to return a tuple.


if __name__ == "__main__":
    print("Start coding")
    print(f5_11([1, 1.2, 'a', [11]]))

