def mean(number):
    digits = list(str(number))
    digits_sum = 0

    for digit in digits:
        digits_sum += int(digit)

    return digits_sum // len(digits)


print(mean(42))
