def f5_12(S):
    len_s = len(S)
    new_s = ""

    for index in range(0, len(s) ,1):
        new_s += S[index] + str(len_s)
        len_s -= 1

    return S, new_s


if __name__ == "__main__":
    s = "abcde"
    print(f5_12(s))
