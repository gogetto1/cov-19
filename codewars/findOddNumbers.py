"""
test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1); 
test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
test.assert_equals(find_it([10]), 10);
test.assert_equals(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);
test.assert_equals(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1);
"""
from collections import Counter


def find_it(seq):
    seq1 = list(Counter(seq).items())
    for x in seq1:
        if x[1] % 2 != 0:
            return x[0]


# rozwiazanie1:
"""
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
            """