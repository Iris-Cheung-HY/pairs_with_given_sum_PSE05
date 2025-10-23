
def pairs_with_given_sum(numbers, target):
    pair_list = []
    pair_count = 0

    for num in numbers[:]:
        diff = target - num
        if diff in pair_list:
            pair_count += 1
            pair_list.remove(diff)
            numbers.remove(num)
        else:
            pair_list.append(num)
    return pair_count
