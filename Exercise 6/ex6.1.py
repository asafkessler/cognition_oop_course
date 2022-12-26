vowels = ['a', 'e', 'i', 'u', 'o']


def pairs_creator(s_string, c_vowel):
    pairs_set = {''}
    pair = ''
    # There is here code reppetion need to be changed
    if len(s_string) > 1:
        for index in range(len(s_string)):
            current_char = s_string[index]
            if current_char == c_vowel:
                if index == 0 and \
                        not vowels.__contains__(s_string[index + 1]):
                    pair = s_string[index] + s_string[index + 1]
                    pairs_set.add(pair)

                elif not index + 1 == len(s_string):

                    if not vowels.__contains__(s_string[index - 1]):
                        pair1 = s_string[index - 1] + s_string[index]
                        pairs_set.add(pair1)
                    if not vowels.__contains__(s_string[index + 1]):
                        pair2 = s_string[index] + s_string[index + 1]
                        pairs_set.add(pair2)
                else:
                    if not vowels.__contains__(s_string[index - 1]):
                        pair = s_string[index - 1] + s_string[index]
                        pairs_set.add(pair)

    return pairs_set


def lett_sets(user_string_list):
    vowels_set = {''}
    bTm_set = {''}
    nTz_set = {''}
    pairs_set = {''}

    # running on the current string in the list of stings
    for curr_string in user_string_list:
        # running on each char in the current string
        for index_char in range(len(curr_string)):

            current_char = curr_string[index_char]
            if vowels.__contains__(current_char):
                vowels_set.add(current_char)
                pairs_set.update(pairs_creator(curr_string, current_char))
            elif current_char <= 'm':
                bTm_set.add(current_char)
            else:
                nTz_set.add(current_char)

    vowels_set.remove('')
    bTm_set.remove('')
    nTz_set.remove('')
    pairs_set.remove('')

    lengths = []
    lengths.append(len(vowels_set))
    lengths.append(len(bTm_set))
    lengths.append(len(nTz_set))
    lengths.append(len(pairs_set))

    return tuple(lengths)


if __name__ == '__main__':
    user_list = ["applesarenotblue", "thisbushadsaltywheels", "besttreesdonotwrite"]
    print(lett_sets(user_list))
