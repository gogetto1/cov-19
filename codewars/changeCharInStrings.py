"""
You've been given a list that states the daily revenue for each day of the week. Unfortunately, the list has been corrupted and contains extraneous characters. Rather than fix the source of the problem, your boss has asked you to create a program that removes any unneccessary characters and return the corrected list.

The expected characters are digits, ' $ ', and ' . ' All items in the returned list are expected to be strings.

For example:

a1 = ['$5.$6.6x.s4', '{$33ae.5(9', '$29..4e9', '%.$9|4d20', 'A$AA$4r R4.94']
remove_char(a1)
>>> ['$56.64', '$33.59', '$29.49', '$94.20', '$44.94']
"""

a1 = ['$5.$6.6x.s4', '{$33ae.5(9', '$29..4e9', '%.$9|4d20', 'A$AA$4r R4.94']


"""
res = list(map(lambda sub: int(''.join(
    [ele for ele in sub if ele.isnumeric()])), a1))
print(res1)
"""
a2 = a1.filter(str.isdigit, a1)
print(a2)
