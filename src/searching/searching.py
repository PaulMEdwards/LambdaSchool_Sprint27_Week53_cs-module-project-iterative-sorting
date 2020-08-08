def linear_search(arr, target):
    # Your code here
    # print(f"target = {target}\n{arr}")
    for i in range(0, len(arr)):
        # print(f"for {i} in range(0, {l}):\ta[{i}]({arr[i]}) == {target}?\t{arr[i] == target}")
        if arr[i] == target:
            # print(f"found at index: {i}!")
            return i
    # print("not found")
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    l = 0
    h = len(arr) - 1

    while l <= h:
        m = (l + h) // 2
        v = arr[m]

        if v == target: return m
        elif v > target: h = m - 1
        else: l = m + 1

    return -1  # not found
