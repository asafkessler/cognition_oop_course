
def range_attributes():
    """
    exploring the range attributes
    exploring the string cutting attributes
    :return:
    """
    liz = list(range(6, 0, -1))
    a = "English cake"
    liz[6:0:-2] = a[6:0:-2]
    print(liz)

if __name__ == "__main__":
    range_attributes()
