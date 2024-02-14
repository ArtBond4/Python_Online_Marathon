def isPalindrome(str):
    total = 0
    # print(set(str))
    for i in set(str):
        if (str.count(i)) % 2 == 1:
            # print(f"char - {i}, count - {str.count(i)}")
            total += 1
    return not total > 1
