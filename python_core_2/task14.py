def sum_primes(list_numbers):
    if not list_numbers:
        return None

    result = 0

    for num in list_numbers:
        divisors = 0

        for i in range(1, num):
            if num % i == 0:
                divisors += 1

        if divisors == 1:
            result += num

    return result


print(sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 17)
print(sum_primes([2, 3, 4, 11, 20, 50, 71]) == 87)
print(sum_primes([]) == None)
