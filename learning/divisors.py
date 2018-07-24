#Divisors yo

div = int(input("Give me a number!:\n"))

x = list(range(1,div+1))
dividers = []

for i in x:
    if div % i == 0:
        dividers.append(i)

print(dividers)



