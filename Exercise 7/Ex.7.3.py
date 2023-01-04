if __name__ == '__main__':
    # Test
    '''
    res = 1

    print(res , " \n")

    for i in range(-5, 5):
        print("i:  " , i)
        print("res:  " , res)
        res += i

    print(pow(res, 2))
    '''

    # Test
    '''
    a = set([(1, 2, 3), (4, 5, 6), (1, 2, 3)])

    b = set([(1, 2, 3), ('a', 'b', 'c'), 4, 5, 6])

    print(a | b)
    '''

    # Test
    print((range(17,-2,-3)))

    L1 = [1, 2];
    L2 = ["a", 2]

    L3 = []

    for n in L1:

        for p in L2:

            if n != p:
                L3.append((n, p))

    print(L3)