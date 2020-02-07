#  Jesse Selin jps496 11223887 CMPT145-02-L10

def checkrow(main):
    '''
    Purpose: To check each row in the list of lists to see if its a latin square.
    Pre-conditions: A list of lists with N sublists of N length.
    Return: True if Latin SQ, False otherwise.
    '''
    # considered a latin square until proven otherwise
    latin = True
    n = len(main)
    for row in main:
        # Used and altered for each row, if a True values remains after the row is iterated through then a value between
        # 1 and n did not appear
        check = [True] * n
        for value in row:
            # checks if incorrect values exist that cannot be in a latin square
            if value > n or value <= 0:
                latin = False
                break
            check[value - 1] = False
        if True in check:
            latin = False
            break
    return latin


def checkcol(main):
    '''
    Purpose: To check each column in the list of lists to see if its a latin square.
    Pre-conditions: A list of lists with N sublists of N length.
    Return: True if Latin SQ, False otherwise.
    '''
    # considered a latin square until proven otherwise
    latin = True
    n = len(main)
    for column in range(len(main)):
        # Used and altered for each column, if a True values remains after the column is iterated through then a value
        # between 1 and n did not appear
        check = [True] * n
        for row in range(n):
            # checks if incorrect values exist that cannot be in a latin square
            if main[row] == [] or main[column][row] > n or main[row][column] <= 0:
                latin = False
                break
            # column is held while each each row in that column is iterated through
            check[main[row][column] - 1] = False
        if True in check:
            latin = False
            break
    return latin


def checker(main):
    '''
    Purpose: To check the square is a latin square with checkrow/checkcol.
    Pre-conditions: A list of lists with N sublists of N length. Function checkrow and checkcol exist.
    Post-conditons: Return values from checkrow and checkcol.
    Return: Prints Yes if Latin SQ, No if not.
    '''
    if checkcol(main) and checkrow(main):
        print('Yes')
    else:
        print('No')


def read(filename):
    '''
    Purpose: To open the file with the filename
    Pre-conditions: A filename as a string
    Post-conditons: File is read and creates a list of lists of integers.
    Return: A list of lists with N sublists of N length.
    '''
    file = open(filename, 'r')
    unorganizedvalues = [x.split() for x in file]
    n = int(unorganizedvalues[0][0])
    # a main list is created then the unorganized values from line 2 to N is set into sublists appended to the main list
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
    '''
    Purpose: Asks for the name of a file from console using input.
    Pre-conditions: The filename is written correctly.
    Post-conditons: The filename is a string.
    Return: A filename set as a string.
    '''
    value = str(input('Please enter a filename for your Latin Square test:'))
    return value

filename = ask()
checker(read(filename))
