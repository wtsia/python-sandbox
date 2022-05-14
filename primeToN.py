def primeToN(n):
    for i in range (5, n):
        prime_num = {2, 3}
        for i in range (1, len(prime_num)):
            if n % prime_num[i] == 0:
                return
            else:
                prime_num.append(n)
                print(n)

primeToN(100)
