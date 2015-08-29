def rev_int(number):
    rev = 0
    while number > 0:
        rev *= 10
        rev += number % 10
        number //= 10
    return rev


def mod_seven_sum(e):
    result = 0
    for i in range(0, 10**e, 7):
        if rev_int(i) % 7 == 0:
            result += i
    print(result)
