def f8_2(L1, L2, L3):

    # with list comprehension
    get_a_trio = [[x, y, z] for x in L1 for y in L2 if x > y for z in L3 if (x > z) & (y > 2 * z)]

    # without list comprehension
    # for x in L1:
    #     for y in L2:
    #         if x > y:
    #             for z in L3:
    #                 if (x > z) & (y > 2 * z):
    #                     print (x , y , z)

    return get_a_trio

if __name__ == '__main__':
    l1 = [4, 5]
    l2 = [2, 3]
    l3 = [3, 1]

    print("Start coding")
    print(f8_2(l1, l2, l3))