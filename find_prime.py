# Fastest way to find prime numbers
# a function that returns prime numbers till num

def allPrimesUpTo(num):                       # eg : num = 100
    primesFound = [2]                         # 2 is already included
    for n in range(3, num): 
        limit = int(n ** 0.5) + 1             # for n in 3 to 99: 
        for factor in primesFound:            #   for factor in [2,...]
            if factor < limit:                #      if factor < 11
                if n % factor == 0:
                    break
        else:
            primesFound.append(n)
    return primesFound
