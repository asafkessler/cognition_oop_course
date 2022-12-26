def even_number(user_data):
    counter_even = 0
    sum_even = 0
    for value in user_data:
        if isinstance(value, int):
            if value % 2 == 0:
                sum_even += value
                counter_even += 1

    answer = (counter_even, sum_even)
    return answer



if __name__ == "__main__":
    user_data = (1,[2],3,(4,),5,7)
    print(even_number(user_data))
