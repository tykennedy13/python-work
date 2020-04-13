for num in range(3, 11):
    print(num)

    def isPrime(n):
    n_p = "prime"
    for num in range(2,n):
        if(n % num ==0):
            n_p = "not prime"
            break
    return n_p
print(isPrime(13))