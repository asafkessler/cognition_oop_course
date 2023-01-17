def f8_1(n1, n2):
    """
    Without list comprehension.
    :param n1:
    :param n2:
    :return:
    """
    list_of_lists = []
    for number in range(n1, n2+1):
        if number % 2 == 1:
            list_of_lists.append([2*number, number**2 - 1, number**3 + 1])
    return list_of_lists

def f8_1_with(n1, n2):
    """
    With list comprehension.
    newlist = [expression for item in iterable if condition == True]
    The condition is like a filter that only accepts the items that valuate to True.
    The iterable can be any iterable object, like a list, tuple, set etc. An object that you can iterate on.
    The expression is the current item in the iteration, but it is also the !outcome!, which you can manipulate before
    it ends up like a list item in the new list.The expression can also contain conditions, not like a filter,
    but as a way to manipulate the outcome.

    :param n1:
    :param n2:
    :return:
    """
    newlist = [number for number in range(n1, n2+1) if number % 2 == 1]
    finallist = [[2*number, number**2 - 1, number**3 + 1] for number in newlist]
    return finallist


if __name__ == '__main__':
    print("Start coding")
    print(f8_1_with(1,2))