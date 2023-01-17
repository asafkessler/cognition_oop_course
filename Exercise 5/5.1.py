def f5_9(s):
    strings_result = []
    middle_char_place = int(len(s) / 2)
    middle_char = s[middle_char_place]

    strings_result.append(s)
    # string_blocks = str.split(s, middle_char)
    block1 = s[0:middle_char_place]
    block2 = s[middle_char_place + 1: len(s)]

    string_blocks = []
    string_blocks.append(block1)
    string_blocks.append(middle_char)
    string_blocks.append(block2)

    for value in string_blocks:
        strings_result.append(value)

    return strings_result

