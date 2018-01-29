#Divisors yo

div = int(input("Give me a number!:\n"))
#  podzielne przez sama siebie i 2

x = list(range(1,div+1))
dividers = []

for i in x:
    if div % i == 0:
        dividers.append(i)

print(dividers)



