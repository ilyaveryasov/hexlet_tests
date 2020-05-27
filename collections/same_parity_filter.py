def same_parity_filter(chek_list):
    result = []
    for item in chek_list:
        if item % 2 == chek_list[0] % 2:
            result.append(item)
    return result

print(same_parity_filter([5, 0, 1, -3, 10]))
