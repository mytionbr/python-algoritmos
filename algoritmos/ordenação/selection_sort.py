def sort(array):
    for index in range(0, len(array)):
        min_index = index

        for right in range(index + 1, len(array)):
            if array[right] < array[min_index]:
                min_index = right

        array[index], array[min_index] = array[min_index], array[index]


array = [10, 1, 34, 5, 65, 78, 2423, 23, 12, 4]
sort(array)
print(array)
