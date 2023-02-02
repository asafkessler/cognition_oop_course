def func_test(L):
    D = {}
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    value = ""

    # run on each string in the list
    for curr_s in L:

        # string is bigger the two chars
        if len(curr_s) > 2:
            first_c = curr_s[0]
            second_c = curr_s[1]
            bef_last_c = curr_s[-2]
            last_c = curr_s[-1]

            # here I had a bug in the use case of the non-numeric char, changed the usage of isinstance
            if first_c in numbers and second_c in numbers:
                next_c = curr_s[2]
                # here I had a bug when I tried to cast a str to an int & not just searching in the numbers list
                if not next_c in numbers:
                    key = int(first_c + second_c)
                    for i in range(2, len(curr_s)):
                        value += curr_s[i]
                    if not key in D.keys():
                        D[key] = value

                    # here I had a bug of not cleaning the value strings
                    value = ""
            # here I had a bug in the use case of the non-numeric char, changed the usage of isinstance
            elif bef_last_c in numbers and last_c in numbers:
                next_c = curr_s[-3]
                # here I had a bug when I tried to cast a str to an int
                if not next_c in numbers:
                    key = int(bef_last_c + last_c)
                    for i in range(0, len(curr_s) - 2):
                        value += curr_s[i]
                    if not key in D.keys():
                        D[key] = value
                    # here I had a bug of not cleaning value strings
                    value = ""
            else:
                continue

        # string is exactly two chars
        elif len(curr_s) == 2:
            first_c = curr_s[0]
            second_c = curr_s[1]
            if isinstance(int(first_c), int) and isinstance(int(second_c), int):
                key = int(first_c + second_c)
                if not key in D.keys():
                    D[key] = ""
        else:
            continue

    return D


if __name__ == "__main__":
    L = ["12asaf", "kessler12", "1234", "443Shachar", "Gilli13", "Guy35", "88", "a", "Noam", ""]

    # test of hypothesis - using in instead of .__contains__() -> WORKS
    D = {}
    D["a"] = "1"
    D["b"] = "2"

    if "a" in D.keys():
        print("yes")
    if not "c" in D.keys():
        print("No")

    print(func_test(L))
