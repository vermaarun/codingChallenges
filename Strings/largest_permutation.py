def largest_permutation(num):
    num_array = [0] * 10
    while num > 0:
        digit = num % 10
        num_array[digit] += 1
        num = num / 10
    print num_array
    largest_number = []
    for i in range(9, -1, -1):
        largest_number += num_array[i] * [i]
    print largest_number
    return int(''.join(list(map(str, largest_number))))


if __name__ == "__main__":
    largestNumber = largest_permutation(5467654)
    print "Largest Number is %d" % largestNumber
