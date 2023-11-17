#Missing Numbers  | HackerRank


n = 10
arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
m = 13
brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]


from collections import Counter


def missingNumbers(arr, brr):
    count_a = Counter(arr)
    count_b = Counter(brr)
    result = []
    for i in arr:
        if i in brr and count_a[i] == count_b[i]:
            print('YES, passed both!')
        elif i in brr and count_a[i] != count_b[i]:
            pass
        else:
            if i not in result:
                result.append(i)

    return sorted(result, reverse = False)

print(missingNumbers(arr,brr))

#Output should be 204 205 206