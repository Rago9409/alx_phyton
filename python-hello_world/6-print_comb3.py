for i in range(100):
    for j in range(i+1, 100):
        if i < 99:
            print("{:d}{:d}, ".format(i, j), end="")
        else:
            print("{:d}{:d}".format(i, j))