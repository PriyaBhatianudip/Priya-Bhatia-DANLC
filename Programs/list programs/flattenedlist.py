lst = [1, 2, 3, 4, 5]
k = 2

if lst:
    n = len(lst)
    k = k % n
    rotated_list = lst[-k:] + lst[:-k]
else:
    rotated_list = lst

print(rotated_list)