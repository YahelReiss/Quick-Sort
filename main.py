import random


def find_pivot(arr):
    candidates = random.sample(arr, min(5, len(arr)))
    candidates.sort()
    return candidates[len(candidates) // 2]


def quick_sort(left, right, arr):
    if right - left < 2:
        return
    new_left, new_right = left, left
    pivot = find_pivot(arr[left:right])
    spot = left
    eq_spot = left
    for i in range(left, right):
        if arr[i] < pivot:
            arr[i], arr[eq_spot], arr[spot] = arr[eq_spot], arr[spot], arr[i]
            spot += 1
            eq_spot += 1
            new_left += 1
            new_right += 1
        elif arr[i] == pivot:
            if spot == eq_spot:
                arr[i], arr[spot] = arr[spot], arr[i]
            else:
                arr[i], arr[spot], arr[eq_spot] = arr[eq_spot], arr[i], arr[spot]
            eq_spot += 1
            new_right += 1
    quick_sort(left, new_left, arr)
    quick_sort(new_right, right, arr)


if __name__ == "__main__":
    pass
