#List Overlap Comprehensions

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 7]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 7 ]

a1 = []
b1 = []
dup1 = [a1.append(d1) for d1 in a if d1 not in a1]
dup2 = [b1.append(d2) for d2 in b if d2 not in b1]
c = [element for element in a1 for element2 in b1 if element == element2  ]
print c
