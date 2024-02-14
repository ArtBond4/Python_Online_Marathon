def Cipher_Zeroes(N):
    one_point = ["069", "8"]
    total_points = 0
    for char in N:
        if char in one_point[0]:
            total_points += 1
        elif char in one_point[1]:
            total_points += 2

    if total_points == 0:
        return 0

    elif total_points % 2 == 0:
        return int(bin(total_points - 1)[2:])

    else:
        return int(bin(total_points + 1)[2:])
