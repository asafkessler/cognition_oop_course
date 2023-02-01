def n_4():
    a = [2, 3, 4]
    b = [2, 8, 2]
    d = [(y - x, y + x) for x, y in reversed(list(zip(a, b))) if abs(x - y) <= 2]
    print(d)


def n_3():
    def a(x):
        return x + 2

    def c(y):
        x = a(y)
        return a(x - y)

    x = a(123123)
    print(x)
    y = c(312321312312)
    print(y)
    print(y + 2)


if __name__ == "__main__":
    s_test = "asafkesslerofficial"
    # print(s_test[1::5])
    # print(s_test[16:19:1])
    # print(len(s_test[4:24:3]))
    # print(len(s_test[90:100:1]))
    # print(len(s_test[90:29:-1]))
    # print(len(s_test[90:0:-1]))
    # print(len(s_test[29:3:-2]))

    # print(s_test[16])
    #
    # s1 = "abcde"
    # print(s1[:4:3])
    # print(s1[1:6:2])
    # print(s1[4:2:-1])
    # print(s1[4:1:-1])
