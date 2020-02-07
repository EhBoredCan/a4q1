#  Jesse Selin jps496 11223887 CMPT145-02-L10

def checkrow(main, n):
    latin = True
    for row in main:
        check = [True] * n
        for value in row:
            if value > n or value <= 0:
                latin = False
                break
            check[value-1] = False
        if True in check:
            latin = False
            break
    return latin
