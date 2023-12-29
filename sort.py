def counting_sort(arr):
    max_val = max(arr) + 1
    count = [0] * max_val

    for num in arr:
        count[num] += 1

    index = 0
    for i in range(max_val):
        for _ in range(count[i]):
            arr[index] = i
            index += 1
    return arr

