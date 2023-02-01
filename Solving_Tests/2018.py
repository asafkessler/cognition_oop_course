if __name__ == "__main__":
    # lista = ["hhhhhhhhhhhhhumus", "pita", "salad", "yogurt"]
    # dict = {}
    #
    # for curr_str in list:
    #     for curr_char in curr_str:
    #         dict[curr_char] = 0
    #
    # for curr_str in list:
    #     for curr_char in curr_str:
    #         dict[curr_char] += 1
    #
    # l = list(dict.keys())
    # print(l)
    # l.append("a")
    # print(l)
    #
    # print(dict)
    dna = "atgagtgaaagttaacgt"
    s_codes = 0
    n_codes = len(dna) / 3
    s_list = []
    dict = {}
    for i in range(0, len(dna), 3):
        if dna[i] == 'a' or dna[i] == 't':
            s_codes += 1
            s_list.append(dna[i:i + 3])
            curr_sp_code = dna[i:i + 3]
            dict[curr_sp_code] = [0, []]

    for i in range(0, len(dna), 3):
        if dna[i] == 'a' or dna[i] == 't':
            curr_sp_code = dna[i:i + 3]
            dict[curr_sp_code][0] += 1
            dict[curr_sp_code][1].append(i)

    print((s_codes * 100) / n_codes)
    print(s_list)
    print(dict)
