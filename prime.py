def prime(nb):
    global primes
    primes=[]
    for i in range(2,nb+1):
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            primes.append(i)
    return primes

def nb_mersennes():
    global nb
    nb=[]
    for i in range(len(primes)):
        nb.append(2**primes[i]-1)
    return nb

