def shallow_and_deep():
    '''
            Deep Copy & Shallow Copy
    '''
    L = [1, [2], 3, 4, 5]
    Deep = L[:]

    # Deep Printing the reg values
    print("Deep copy Printing the reg values:")
    print("-------------------------------")
    print("L:", L)
    print("Deep:", Deep, "\n")

    # Deep printing the memory ids
    print("Deep printing the memory ids:")
    print("-------------------------------")
    print("L:", id(L), "Deep:", id(Deep), "\n")

    Deep[2] = "ASAF"
    Deep[1][0] = "a"
    print("L:", L)
    print("Deep:", Deep, "\n")

    print("Deep printing the memory ids:")
    print("-------------------------------")
    print("L:", id(L), "Deep:", id(Deep), "\n")

    print("Shallow copy: printing the memory ids:")
    print("-------------------------------")
    print("L:", id(L[1]), "Deep:", id(Deep[1]), "\n")

    # just creating a reference
    Shallow = L
    Shallow[3] = "Kessler"
    print("Will change the value in L instad of 4 to Kessler:", "L", L, " Shallow", Shallow)

def zipping_lists():
    # zipping two lists
    X = [[0, 0, 0], [0, 0, 0], [1, 2, 1]]
    P = [0, 1, 2]
    # long way
    for index in range(0, len(P)):
        X[index].append(P[index])
    print(X)

    # short way
    for i in range(0, len(X)):
        X[i] = tuple(X[i])

    print(X)

if __name__ == "__main__":
    # shallow_and_deep()

    L = [1,2,3,4,5]
    print(L[4:1:-1])
    print(L[1:3:-1])
    print(L[3:1:-1])

    L = [1,2,3,4,5,6,7,8,9]
    print(L[9::-1])

    s = "asafkessler.com"
    print(s[s.find('.'):len(s):1])
    print(s[-4::])
    print(s[-1:-5:-1])

    print(L[4:6])
    print(L[4:-5:-1])