def studying_hours(a):
    total = 1
    total2 = 1
    for i in range(len(a)-1):

        if a[i] <= a[i+1]:
            total += 1
        else:
            if total > total2:
                total2 = total
            total = 1
        
    return max(total, total2)
