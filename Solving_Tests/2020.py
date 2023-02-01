if __name__ == "__main__":
    # L = [11, 3, 17, 54]
    # helper1 = 0
    # helper2 = 0
    #
    # place1 = 0
    # place2 = 0
    # helper1 = L[place1]
    # d_dict = {}
    #
    # for index in range(0, len(L)):
    #     if L[index] < helper1:
    #         helper1 = L[index]
    #         place1 = index
    # del L[place1]
    #
    # for index in range(0, len(L)):
    #     if L[index] > helper1:
    #         helper2 = L[index]
    #         place2 = index
    # del L[place2]
    #
    # d_dict[helper1] = helper2
    # print(d_dict)

    L = [11, 54, (2, 3), 17, 'xx', 'ba', 3, 'milim', (1, 2, 3), 'ddd']

    D = {}

    n_list = []
    str_list = []
    tup_list = []

    for i in L:
        if isinstance(i, int):
            n_list.append(i)
        if isinstance(i, str):
            str_list.append(i)
        if isinstance(i, tuple):
            tup_list.append(i)

    print(str_list)
    D = {}

    for j in n_list:
        for index in range(0, len(n_list)):
            if index < len(n_list)-1 and j < n_list[index]:
                D[j] = n_list[index]
                del n_list[index]

    for j in range(0, len(str_list)):
        for index in range(0, len(str_list)):
            if j <= len(str_list)-1 and \
                    index <= len(str_list)-1 and \
                    str_list[j] < str_list[index]:
                D[str_list[j]] = str_list[index]
                # del str_list[j]
                del str_list[index]

    for value_t in tup_list:
        for index_t in range(0, len(tup_list)):
            if len(value_t) < len(tup_list[index_t]):
                D[value_t] = tup_list[index_t]
                del tup_list[index_t]

    print(D)



