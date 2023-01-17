def str_cmp(s1, s2):
    if len(s1) == len(s2):
        s1_n = ''
        s2_n = ''
        for curr1 in s1:
            if not curr1.isnumeric():
                s1_n += curr1.lower()
            else:
                s1_n += curr1

        for curr2 in s2:
            if not curr2.isnumeric():
                s2_n += curr2.lower()
            else:
                s2_n += curr2

        if s1_n == s2_n:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    # Test
    if str_cmp('123ab', '123aB'):
        print("y")
    else:
        print("n")
