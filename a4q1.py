#  Jesse Selin jps496 11223887 CMPT145-02-L10

def checkrow(main, n):
    latin = True
    for row in main:
        check = [True] * n
        for value in row:
            if value > n or value <= 0:
                latin = False
                break
            check[value - 1] = False
        if True in check:
            latin = False
            break
    return latin


def checkcol(main, n):
    latin = True
    for column in range(len(main)):
        check = [True] * n
        for row in range(n):
            if main[row] == [] or main[column][row] > n or main[row][column] <= 0:
                latin = False
                break
            check[main[row][column] - 1] = False
        if True in check:
            latin = False
            break
    return latin


def checker(main, n):
    if checkcol(main, n) and checkrow(main, n):
        print('Yes')
    else:
        print('No')
