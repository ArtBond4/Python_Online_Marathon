def order(a):
    descending_list = a.copy()
    descending_list.sort(reverse=True)
    ascending_list = a.copy()
    ascending_list.sort(reverse=False)
    if a == descending_list:
        return "descending"
    elif a == ascending_list:
        return "ascending"
    else:
        return "not sorted"
