
def odd_factory(user_numbers):
    answer = ()
    odds_set = {''}
    sum = 1
    for value in user_numbers:
        if isinstance(value, int):
            if value % 2 != 0:
                odds_set.add(value)

    odds_set.remove('')
    if len(odds_set) == 0:
        return ()
    else:
        for value in odds_set:
            sum *= value

        answer = (len(odds_set), sum)
        return answer



if __name__ == '__main__':
    user_numbers = (11, -23, [4], 51, 11, -23, 7, (6,), 51, 7, '9')
    odd_factory(user_numbers)