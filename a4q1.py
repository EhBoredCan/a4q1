#  Jesse Selin jps496 11223887 CMPT145-02-L10

def checkrow(main):
    latin = True
    n = len(main)
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


def checkcol(main):
    latin = True
    n = len(main)
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


def checker(main):
    if checkcol(main) and checkrow(main):
        print('Yes')
    else:
        print('No')


def read(filename):
    file = open(filename, 'r')
    unorganizedvalues = [x.split() for x in file]
    n = int(unorganizedvalues[0][0])
    main = []
    row = 1
    while row < n + 1:
        sublist = []
        for value in range(n):
            sublist.append(int(unorganizedvalues[row][value]))
        main.append(sublist)
        row += 1
    return main


def ask():
    value = str(input('Please enter a filename for your Latin Square test:'))
    return value

filename = ask()
checker(read(filename))
