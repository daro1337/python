#odd or even!

oddoreven = int(input("Type number:\n"))

if oddoreven % 4 == 0:
    print("Liczba jest wielokrotnoscia 4!")

if oddoreven == 0:
    print("Hard to say:(")
elif oddoreven % 2 == 0:
    print("Number is EVEN!\n")
else:
    print("Number is Odd\n")

print("exe2")
num = int(input("Num value:"))
check = int(input("Check value:"))
if num % check == 0:
    print(str(num) + "/" + str(check) + "dzieli się bez reszty" )
