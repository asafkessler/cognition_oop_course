
def f9_1(D):
    from collections.abc import Hashable
    new_D = {}

    for curr_key in D.keys():
        if(isinstance(curr_key, Hashable)) & (isinstance(D[curr_key], Hashable)):
            new_D[D[curr_key]] = curr_key

    return new_D
if __name__ == "__main__":
    D = {1:['a', 'b'], 'a':3, (1, 'a'):'b'}
    print(f9_1(D))
