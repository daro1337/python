#Check Primality Functions

def get_num():
    return int(input("Type numebr:\n"))

num = get_num()
def primary():
    x = list(range(1,num+1))
    dividers = []

    for i in x:
        if num % i == 0:
            dividers.append(i)
    return dividers

if len(primary()) == 2:
    print("Your number is prime number" + str(primary()))
else:
    print("Your number isn't prime number!" + str(primary()))
#print(len(dividers))
