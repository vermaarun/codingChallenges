def compressed_string(org_string):
    print "Original String is %s" % org_string
    if len(org_string) < 1:
        return org_string

    # if original length less than compressed length, return original string
    if len(org_string) <= compressed_string_length(org_string):
        return org_string

    compressed_str = ""
    count = 0
    for i in xrange(len(org_string)):
        if i != 0 and org_string[i] != org_string[i - 1]:
            compressed_str += org_string[i - 1] + str(count)
            count = 0
        count += 1

    # to add last character
    compressed_str += org_string[-1] + str(count)

    return compressed_str


def compressed_string_length(org_str):
    compressed_str_length = 0
    count = 0
    for i in xrange(len(org_str)):
        if i != 0 and org_str[i] != org_str[i - 1]:
            compressed_str_length += 1 + len(str(count))
            count = 0
        count += 1

    # add length of last character
    compressed_str_length += 1 + len(str(count))
    # print compressed_str_length
    return compressed_str_length


if __name__ == "__main__":
    print "Compressed String is %s " % compressed_string("aaa")
