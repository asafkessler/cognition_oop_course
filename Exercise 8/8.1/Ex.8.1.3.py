numbers_list = ['0', '8.1', '2', '3', '4', '5', '6', '7', '8', '9']


def count_tenz(tenz_string):
    numbers = []
    sub_numbers_list = [int(curr_char) if numbers_list.__contains__(curr_char) else "s" for curr_char in tenz_string]
    tenz_counter = 0

    # for i in range(0, len(sub_numbers_list)):
    size_flag = 0

    while size_flag < len(sub_numbers_list):
        saver = ''
        while sub_numbers_list[size_flag] != 's':
            saver += str(sub_numbers_list[size_flag])
            size_flag += 1
            if size_flag == len(sub_numbers_list):
                break

        if saver != '':
            numbers.append(saver)
            if (int(saver) > 10) & (int(saver) < 100):
                tenz_counter += 1

        size_flag += 1

    result_tuple = (tenz_counter, numbers)
    return result_tuple


if __name__ == '__main__':
    test = '8.1'
    print(count_tenz(test))
