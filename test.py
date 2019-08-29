if __name__ == "__main__":
    str = "abcdefgh"
    for i in range(len(str)-1):
        if i + 1 > len(str) or str[i] != str[i+1]:
            print str[i]
