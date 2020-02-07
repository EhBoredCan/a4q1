# Jesse Selin jps496 11223887 CMPT145-02-L10

###############
# Test Driver #
###############

import a4q1 as a1

# Tests for checkrow

test = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
reason = 'Three N = 3 size sublists with correct row values'
result = a1.checkrow(test)
if result != True:
    print(reason, 'should return True returned', result)

test = [[1]]
reason = 'A list of 1'
result = a1.checkrow(test)
if result != True:
    print(reason, 'should return True returned', result)

test = [[1, 4, 3], [1, 2, 3], [3, 2, 1]]
reason = 'Incorrect sublist in the front and reversed value at the end'
result = a1.checkrow(test)
if result != False:
    print(reason, 'should return False returned', result)

test = [[3, 2, 1], [1, 4, 3], [1, 2, 3]]
reason = 'Incorrect sublist in the middle and reversed value in the front'
result = a1.checkrow(test)
if result != False:
    print(reason, 'should return False returned', result)

test = [[1, 2, 3], [3, 2, 1], [1, 4, 3]]
reason = 'Incorrect sublist at the end and reversed value in the middle'
result = a1.checkrow(test)
if result != False:
    print(reason, 'should return False returned', result)

test = [[]]
reason = 'An empty sublist, latin squares are not empty'
result = a1.checkrow(test)
if result != False:
    print(reason, 'should return False returned', result)

test = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 3, 4, -2, 1]]
reason = 'Middle sublist reversed values and end of list contains a negative and is randomly oriented'
result = a1.checkrow(test)
if result != False:
    print(reason, 'should return False returned', result)


# Tests for checkcol

test = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
reason = 'Three N = 3 size sublists with correct row values'
result = a1.checkcol(test)
if result != True:
    print(reason, 'should return True returned', result)

test = [[1]]
reason = 'A list of 1'
result = a1.checkcol(test)
if result != True:
    print(reason, 'should return True returned', result)

test = [[1, 4, 3], [2, 3, 2], [3, 2, 1]]
reason = 'Incorrect second column'
result = a1.checkcol(test)
if result != False:
    print(reason, 'should return False returned', result)

test = [[4, 2, 1], [1, 3, 3], [2, 1, 2]]
reason = 'Incorrect first column'
result = a1.checkcol(test)
if result != False:
    print(reason, 'should return False returned', result)

test = [[1, 2, 3], [3, 1, 1], [2, 3, 4]]
reason = 'Incorrect last column'
result = a1.checkcol(test)
if result != False:
    print(reason, 'should return False returned', result)

test = [[]]
reason = 'An empty sublist, latin squares are not empty'
result = a1.checkcol(test)
if result != False:
    print(reason, 'should return False returned', result)

test = [[1, 2, 4, 4, 5], [2, 3, 1, 5, 4], [3, 4, 2, 2, 3], [4, 1, 3, 3, 2], [5, 5, 5, 1, -1]]
reason = 'last column contains a negative'
result = a1.checkcol(test)
if result != False:
    print(reason, 'should return False returned', result)


# Tests for Checker

test = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
reason = 'Correct Latin Square'
# a1.checker(test)
# Visual Inspection: Should print Yes
# Correct output

test = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2], [4, 5, 1, 2, 3], [5, 1, 2, 3, 4]]
reason = 'Correct Latin Square'
# a1.checker(test)
# Visual Inspection: Should print Yes
# Correct output

test = [[], [], [], [], []]
reason = 'Incorrect Latin Square, list of empty lists'
# a1.checker(test)
# Visual Inspection: Should print No
# Correct output

test = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2], [4, 5, 1, 2, 3], [5, 1, 2, 3, -4]]
reason = 'Incorrect Latin Square, last value is negative'
# a1.checker(test)
# Visual Inspection: Should print No
# Correct output

test = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 6, 1, 2], [4, 5, 1, 2, 3], [5, 1, 2, 3, 4]]
reason = 'Incorrect Latin Square, middle value is wrong (value > n)'
# a1.checker(test)
# Visual Inspection: Should print No
# Correct output


# Test for read

test = [[2, 3, 1], [3, 1, 1], [1, 2, 3]]
reason = 'Compare output with known correct square'
result = (a1.read('no_3.3.txt'))
if result != test:
    print('Correct output but result =', result)

reason = 'Check value for large square for Latin Square'
# a1.checker(a1.read('yes_100.2.txt'))
# Visual Inspection: Should print Yes
# Correct output

reason = 'Check value for large square for non-Latin Square'
# a1.checker(a1.read('no_50.3.txt'))
# Visual Inspection: Should print No
# Correct output

# Test entire script for latin square.
# Manual Testing

# Test for no_100.3.txt
# Result = No
# Correct

# Test for yes.10.2.txt
# Result = Yes
# Correct

# Test for no_3.4.txt
# Result = No
# Correct

# Test for yes_50.1.txt
# Result = Yes
# Correct

print('Test Complete')