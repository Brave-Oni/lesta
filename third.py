# coding=utf-8
"""
Сортировка массива (самая быстрая по процессорным тикам).

Сложность O(n * log(n)) в худшем случае.
"""


def merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge(left)
        merge(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        arr[k:] = left[i:]
        k += len(left) - i

        arr[k:] = right[j:]
        k += len(right) - j


if __name__ == '__main__':
    arr = [10, 6, 8, 7, 9, 5, 4, 3, 2, 1]
    merge(arr)

    print " ".join(map(str, arr))
