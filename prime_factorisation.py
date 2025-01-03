# gives the prime factors of a number

def get_prime_factors(num):
    prime_factors = []
    fact = 2
    while fact <= num:
        if num % fact == 0:
            prime_factors.append(fact)
            num = num / fact
        else:
            fact += 1
    return prime_factors
  
# ----- test code ------
print(get_prime_factors(10))
