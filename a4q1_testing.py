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
    print(reason, 'should return True returned ', result)

test = [[1]]
reason = 'A list of 1'
result = a1.checkrow(test,1)
if result != True:
    print(reason, 'should return True returned ', result)

test = [[1, 4, 3], [1, 2, 3], [3, 2, 1]]
reason = 'Incorrect sublist in the front and reversed value at the end'
result = a1.checkrow(test,3)
if result != False:
    print(reason, 'should return False returned ', result)

test = [[3, 2, 1], [1, 4, 3], [1, 2, 3]]
reason = 'Incorrect sublist in the middle and reversed value in the front'
result = a1.checkrow(test,3)
if result != False:
    print(reason, 'should return False returned ', result)

test = [[1, 2, 3], [3, 2, 1], [1, 4, 3]]
reason = 'Incorrect sublist at the end and reversed value in the middle'
result = a1.checkrow(test,3)
if result != False:
    print(reason, 'should return False returned ', result)

test = [[]]
reason = 'An empty sublist'
result = a1.checkrow(test,1)
if result != True:
    print(reason, 'should return True returned ', result)

print('Tests Complete')