def print_pairs(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            print(lst[i], lst[j])
