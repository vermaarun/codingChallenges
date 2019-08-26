def is_string_unique(s):
    if len(s) > 128:
        return False
    string_map = {}
    for c in s:
        if c in string_map:
            return False
        else:
            string_map[c] = True
    return True


if __name__ == "__main__":
    print is_string_unique("abcdef")
