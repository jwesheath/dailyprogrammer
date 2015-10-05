import sys


def get_distinct_primes(n):
    primes = set()
    for i in range(2, n + 1):
        while n % i == 0:
            primes.add(i)
            n /= i
        if n == 1:
            break
    return primes if primes else set(n)


def main(input_text):
    with open(input_text, 'r') as infile:
        num_lines = int(infile.readline())
        for _ in range(num_lines):
            a, b = eval(infile.readline())
            valid = sum(get_distinct_primes(a)) == sum(get_distinct_primes(b))
            output = '(' + str(a) + ', ' + str(b) + ')'
            output += ' VALID' if valid else ' NOT VALID'
            print(output)

if __name__ == '__main__':
    main(sys.argv[1])
