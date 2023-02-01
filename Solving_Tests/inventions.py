if __name__ == "__main__":
    s_string = "LandenCaldwellAryannaBurchZaydenValenzuelaMarianaPenningtonFernandaPattonWillClayAmericaBondJonah" \
               "ZavalaDeniseHornKathrynMcgeeJaydaRobertsonTrippWilliams"

    s_names = {('L', 'B'), ('K', 'T'), ('Z', 'H'), ('F', 'D'), ('W', 'V')}
    d_dict = {}

    # init
    for index in s_names:
        d_dict[index] = ""

    for curr_key in d_dict.keys():
        for curr_char in range(0, len(s_string), 1):
            name = ""
            builder_index = 0

            if curr_key[0] == s_string[curr_char]:
                name += s_string[curr_char]
                builder_index = curr_char
                builder_index += 1
                while builder_index < len(s_string) and s_string[builder_index].islower():
                    name += s_string[builder_index]
                    builder_index += 1
                d_dict[curr_key] += name

            last_name = ""
            builder_index = 0
            if curr_key[1] == s_string[curr_char]:
                last_name += s_string[curr_char]
                builder_index += 1
                while builder_index < len(s_string) and s_string[builder_index].islower():
                    last_name += s_string[builder_index]
                    builder_index += 1
                d_dict[curr_key] += last_name

    print (d_dict)