def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    d1 = {}
    for c in s1:
        if c in d1:
            d1[c] += 1
        else:
            d1[c] = 1

    for c in s2:
        if c in d1 and d1[c] > 0:
            d1[c] -= 1
        else:
            return False

    # for k in d1.keys():
    #     if d1[k] > 0:
    #         return False

    return True


if __name__ == "__main__":
    print check_permutation("aaaaaaa", "aaaaaaa")
