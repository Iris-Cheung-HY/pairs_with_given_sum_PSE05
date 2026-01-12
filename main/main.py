
def pairs_with_given_sum(numbers, target):
    numbers.sort()
    n = len(numbers)
    l = 0
    r = n - 1
    pair = 0

    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            pair += 1
            l += 1
        if s > target:
            r -= 1
        if s < target:
            l += 1
    return pair

# Solution 2
#     pair_list = []
#     pair_count = 0

#     for num in numbers[:]:
#         diff = target - num
#         if diff in pair_list:
#             pair_count += 1
#             pair_list.remove(diff)
#             numbers.remove(num)
#         else:
#             pair_list.append(num)
#     return pair_count
