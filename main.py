def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def func1(n):
    if n > 0:
        if (n <= 99) & (n >= 10):
            if (n % 5 == 0) & (n % 7 == 0):
                return "OK"
            else:
                return "wrong input"
        else:
            return "wrong input"
    else:
        return "wrong input"


def func2(n):
    if (n > 0 & (((n <= 99) & (n >= 10)) & ((n % 5 == 0) & (n % 7 == 0)))):
        return "OK"
    else:
        return "wrong input"


def func3(n):
    if (n <= 999) & (n >= 100):

        middleNumber = (n / 10) % 10
        return middleNumber
    else:
        return "Bad input"


def f3(n):
    twoD = n % 100
    first = int(twoD / 10)
    second = int(twoD % 10)
    sum = first + second
    if sum % 2 == 0:
        return True
    else:
        return False


'''
    working with string slicing 
    8.1) I basically need to remember the function split 
    2) I need to remember the relations of [first:until:jumps]
    3) I can change a global variable using the global function
    4) isinstance returns True / False relative to the type
    5) remove removes an element from a list not by place
    6) del is more efficient then remove, remove runs on the list, del deletes the value in a given place
'''


def f5_1(s):
    index_of_middle = int(len(s) / 2)
    strings_list = []
    strings_list.append(s)
    helper_list = []
    helper_list[:0] = s
    # helper_list.remove(helper_list[index_of_middle])
    del helper_list[index_of_middle]
    new_string = ''.join(helper_list)
    strings_list.append(new_string)
    return strings_list


def f5_3(s1, s2):
    strings_tuple = []
    length_s1 = len(s1)
    length_s2 = len(s2)
    string_saver = []
    if length_s1 > length_s2:
        if length_s1 % 2 == 0:
            strings_tuple.append(s1)
        else:
            strings_tuple.append(s2)
        if not length_s1 % 2 == 0:
            string_saver = s1[abs(len(s1) - len(s2)) + 1:]
        else:
            string_saver = s1[abs(len(s1) - len(s2)):]
    else:
        if length_s2 % 2 == 0:
            strings_tuple.append(s2)
        else:
            strings_tuple.append(s1)
        if not length_s2 % 2 == 0:
            string_saver = s2[abs(len(s1) - len(s2)) + 1:]
        else:
            string_saver = s2[abs(len(s1) - len(s2)):]

    strings_tuple.append(string_saver)
    return tuple(strings_tuple)


def f5_9(user_string):
    strings_result = []
    middle_char_place = int(len(user_string) / 2)
    middle_char = user_string[middle_char_place]

    strings_result.append(user_string)
    # string_blocks = str.split(user_string, middle_char)
    block1 = user_string[0:middle_char_place]
    block2 = user_string[middle_char_place + 1: len(user_string)]

    string_blocks = []
    string_blocks.append(block1)
    string_blocks.append(middle_char)
    string_blocks.append(block2)

    for value in string_blocks:
        strings_result.append(value)

    return strings_result


def f5_10(user_string):
    blocks_list = []
    index = 0
    length_str = len(user_string)
    blocks_list.append(user_string[index])
    while index < length_str:
        curr_block = blocks_list[index - 1] + user_string[index]
        blocks_list.append(curr_block)
        index += 1

    return blocks_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # test_string = "abcde"
    # print(f5_10(test_string))ww

    s = "www.google.com"
    print(len(s))
    print(s[4:10])
    print(s[-10:-4])

    x = [0,1,2,3,4]
    print(x[4:-1])
