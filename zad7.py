def is_prime(n: int) -> bool:
    if n < 2:
        return False
    else:
        prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                prime = False
                break
        return prime
