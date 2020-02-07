# Jesse Selin jps496 11223887 CMPT145-02-L10

###############
# Test Driver #
###############

import a4q1 as a1

# Tests for checkrow

test = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
reason = 'Three N = 3 size sublists with correct row values'
result = a1.checkrow(test,3)
if result != True:
    print(reason, 'should return True returned', result)

test = [[1]]
reason = 'A list of 1'
result = a1.checkrow(test,1)
if result != True:
    print(reason, 'should return True returned', result)

test = [[1, 4, 3], [1, 2, 3], [3, 2, 1]]
reason = 'Incorrect sublist in the front and reversed value at the end'
result = a1.checkrow(test,3)
if result != False:
    print(reason, 'should return False returned', result)

test = [[3, 2, 1], [1, 4, 3], [1, 2, 3]]
reason = 'Incorrect sublist in the middle and reversed value in the front'
result = a1.checkrow(test,3)
if result != False:
    print(reason, 'should return False returned', result)

test = [[1, 2, 3], [3, 2, 1], [1, 4, 3]]
reason = 'Incorrect sublist at the end and reversed value in the middle'
result = a1.checkrow(test,3)
if result != False:
    print(reason, 'should return False returned', result)

test = [[]]
reason = 'An empty sublist, latin squares are not empty'
result = a1.checkrow(test,1)
if result != False:
    print(reason, 'should return True returned', result)

test = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 3, 4, -2, 1]]
reason = 'Middle sublist reversed values and end of list contains a negative and is randomly oriented'
result = a1.checkrow(test,5)
if result != False:
    print(reason, 'should return False returned', result)


# Tests for checkcol

test = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
reason = 'Three N = 3 size sublists with correct row values'
result = a1.checkcol(test,3)
if result != True:
    print(reason, 'should return True returned', result)

test = [[1]]
reason = 'A list of 1'
result = a1.checkcol(test,1)
if result != True:
    print(reason, 'should return True returned', result)

test = [[1, 4, 3], [2, 3, 2], [3, 2, 1]]
reason = 'Incorrect second column'
result = a1.checkcol(test,3)
if result != False:
    print(reason, 'should return False returned', result)

test = [[4, 2, 1], [1, 3, 3], [2, 1, 2]]
reason = 'Incorrect first column'
result = a1.checkcol(test,3)
if result != False:
    print(reason, 'should return False returned', result)

test = [[1, 2, 3], [3, 1, 1], [2, 3, 4]]
reason = 'Incorrect last column'
result = a1.checkcol(test,3)
if result != False:
    print(reason, 'should return False returned', result)

test = [[]]
reason = 'An empty sublist, latin squares are not empty'
result = a1.checkcol(test,1)
if result != False:
    print(reason, 'should return True returned', result)

test = [[1, 2, 4, 4, 5], [2, 3, 1, 5, 4], [3, 4, 2, 2, 3], [4, 1, 3, 3, 2], [5, 5, 5, 1, -1]]
reason = 'last column contains a negative'
result = a1.checkcol(test,5)
if result != False:
    print(reason, 'should return False returned', result)

print('Tests Complete')