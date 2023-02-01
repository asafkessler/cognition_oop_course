if __name__ == '__main__':
    p = "SERLSITPLGPYIGAQISGADLTRPLSDNQFEQLYHA"
    s = set(['A', 'S', 'R', 'E', 'F'])


    d_dict = {}

    for i in s:
        d_dict[i] = []

    # for i in range(0, len(p), 1):
    #     if s.__contains__(p[i]):
    #         d_dict[p[i]].append(i)

    for i in range(0, len(p), 1):
        for j in s:
            if p[i] == j:
                d_dict[p[i]].append(i)
    # {'E': [1, 31], 'S': [0, 4, 17, 26], 'F': [30], 'A': [14, 19, 36], 'R': [2, 23]}
    print(d_dict)



    # Different slicing options
    # print("\nDifferent slicing options:")
    # print("-------------------------------")
    # L = [1, 2, 3, 4, 5]
    # print(L[:1:-1][0])
    #
    # Deep[2:3] = "Kessler"
    # print("Different slicing options:")
    # print(Deep)