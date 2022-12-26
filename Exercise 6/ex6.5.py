def local_peak_finder(numbers_list):
    list_length = len(numbers_list)
    index = 1
    peaks_list = []

    while index <= list_length - 2:
        if numbers_list[index] > numbers_list[index - 1] and \
            numbers_list[index] > numbers_list[index + 1]:
                peaks_list.append(numbers_list[index])
        index += 1
    answer = (len(peaks_list), peaks_list)
    return answer


if __name__ == '__main__':
    numbers = [1,2,3,2,5,7,6,4,9,8,6,7]
    print(local_peak_finder(numbers))