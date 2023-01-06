# 2 ve girilen "sayı" parametresine kadar olan asal sayıları döndürür.
def primes_up_to_1000(sayı):
    return [i for i in range(sayı) if all(i % j != 0 for j in range(2, int(i ** (0.5)) + 1))]
