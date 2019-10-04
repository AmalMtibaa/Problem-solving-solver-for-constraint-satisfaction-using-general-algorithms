def AffichageSudoku(a, le):
    for i in range(0, le):
        if i % 3 == 0:
            print("===================================")
        for j in range(0, le):
            if j % 3 == 0:
                print("||", end="")
            print("", a[i * le + j], "", end="")
            if j == 8:
                print("||", end="")
        print()


def AffichageNqueens(a, le):
    for i in range(0, le):
        for j in range(0, le):
            print("", a[i * le + j], "", end="")
        print()
