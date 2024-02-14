def kthTerm(number, k):
    num_list = [number**0]
    loops = k    # i =
    # print(num_list)
    for step in range(1, loops + 1):
        # print(f"step(i) = {step}")                            # number of loop
        sum_num = number**step
        # print(f"add to list {number}**{step} = {sum_num}")          # number in ** loop 3**0, 3**1, 3**2, 3**3
        num_list.append(sum_num)
        # print(num_list)
        len_list = len(num_list)
        for i in range(1, len_list):
            # print(f"add {number}**{step} + {num_list[i-1]}")
            num_list.append(sum_num + num_list[i-1])
        # print("______" * 10)
        if len(num_list) > k+1:
            break
    return num_list[k-1]
