def one_step_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    if len(s1) == len(s2):
        return one_replace_away(s1, s2)
    if len(s1) > len(s2):
        return one_edit_away(s1, s2)
    else:
        return one_edit_away(s2, s1)


def one_replace_away(s1, s2):
    replace = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if replace:
                return False
            replace = True
    return True


def one_edit_away(s1, s2):
    edits = i = j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edits == 1:
                return False
            i += 1
            edits += 1
        else:
            i += 1
            j += 1
    return True


if __name__ == "__main__":
    print one_step_away("abcd", "ab")
