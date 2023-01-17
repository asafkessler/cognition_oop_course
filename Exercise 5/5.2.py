def f5_10(s):
    blocks_list = []
    index = 0
    length_str = len(s)
    blocks_list.append(s[index])
    index+=1

    while index < length_str:
            curr_block = blocks_list[index-1]+s[index]
            blocks_list.append(curr_block)
            index+=1

    return blocks_list