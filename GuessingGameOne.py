import random

num = random.randint(1,9)
usrinput = 0
count=0
ext= 0
while usrinput != num and ext != "exit":

    #num = random.randint(0,9)
    #debug;)
    #print(num)
    while int(usrinput) != num:

        if int(usrinput) > num:
            print("Troszę mniejsza...")
            count += 1
            usrinput = input("Guess number from 0 to 9\n or type 'exit' to exit: \n")
            if usrinput == exit:
                break
        elif int(usrinput) < num:
            print("Ciut większa...")
            count += 1
            usrinput = input("Guess number from 0 to 9\n or type 'exit' to exit: \n")
            if usrinput == exit:
                break
    print("Brawo, zgadłeś za " + str(count) + " razem!!!")


    break