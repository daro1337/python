#Fibonacci

def get_fib():
    return int(input("How many Fibonnaci numbers to generate?\n"))

def fibon():
    val = get_fib()
    fibseq=[]
    for x in range(0, val+1):
        if x == 0:
            fibseq=[0]
        elif x == 1:
            fibseq=[1]
        elif x == 2:
            fibseq=[1,1]
        else:
            fibseq.append((fibseq[x-2] + fibseq[x-3]))
    return fibseq

print(fibon())
