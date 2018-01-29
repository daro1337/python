#List Less Than Ten

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

v1 = int(input("Enter your value: \n"))
new_x = []

for elements in a:
    if elements < v1:
        new_x.append(elements)
        print (new_x)