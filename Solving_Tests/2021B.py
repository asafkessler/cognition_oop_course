def even_border_finder(numbers_string):
    d_dict = {}

    helper = []
    beg = 0
    end = 0

    curr_key = ""
    curr_char = 0
    while curr_char <= len(numbers_string):
        helper = curr_char
        while not int(numbers_string[helper]) % 2 == 1 and \
                helper < len(numbers_string) - 1:
            curr_key += numbers_string[helper]
            helper += 1

        if len(curr_key) >= 2:
            d_dict[curr_key] = []
        curr_key = ""
        curr_char = helper


    print(d_dict)

    # we have the idea of the find function

    # for i in range(0, len(numbers_string), 1):
    #     if numbers_string[i] % 2 == 0:
    #         helper.append(i)
    #
    #     if not d_dict[curr_key]:
    #         d_dict[curr_key] = [helper[0],helper[len(helper)-1]]
    #     else:
    return d_dict


if __name__ == "__main__":
    n_string = '243246524680'
    dig = ['0', '2', '4', '6', '8']
    D = {}
    even_border_finder(n_string)
