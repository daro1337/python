#String List
while True:
    word = str(input("Enter word:\n"))
    lenght = int(len(word))
    #[begin:end:step]
    revers = word[::-1]
    if word == revers:
        print("Word " + word + " is a palindrom")
    else:
        print("Word is not a palindrom")