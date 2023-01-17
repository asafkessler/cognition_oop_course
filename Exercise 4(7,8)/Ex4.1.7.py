from math import sqrt
def quad_eq(a, b, c):
    sr_list = []
    first = (-b + sqrt(pow(b, 2) - 4 * a * c)) / 2 * a # use **0.5 instead of sprt
    second = (-b - sqrt(pow(b, 2) - 4 * a * c)) / 2 * a
    sr_list.append(first)
    sr_list.append(second)

    return sr_list

if __name__ == "__main__":

    print(quad_eq(1, 11, 18))