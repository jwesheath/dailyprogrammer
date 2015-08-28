import itertools


def rev_fizz_buzz(file):

    # Set the highest divisor to consider
    LARGEST_DIVISOR = 12

    # Read data
    with open(file, 'r') as infile:
        goal = infile.read().split('\n')

    # Get length of combo
    n = ord(max({char for row in goal for char in row})) - 97 + 1

    # Generator for cartesian products of 1:largest divisor
    combos = (x for x in itertools.product(range(1, LARGEST_DIVISOR), repeat = n))

    # Check every possible combination
    while True:

        # Generate the next candidate combination
        combo = next(combos)

        # Populate check list with output and check until it matches the goal output
        check = []

        # Start counting
        counter = 0

        while True:

            # Get next number
            counter += 1

            # Add non-empty rows to the check list
            row = ''
            for divisor in combo:
                if (counter % divisor) == 0 and counter is not 0:
                    row += chr(combo.index(divisor) + 97)
            if row:
                check.append(row)

            # Stop searching as soon as the check list doesn't match the goal
            # or it becomes the same size
            if (len(check) > 0 and check != goal[:len(check)]) or len(check) == len(goal):
                break

        # If this combo matches the goal, print it and quit
        if check == goal:
            print(str(' '.join([str(x) for x in combo])))
            break

# Try it out
rev_fizz_buzz('input1.txt')
rev_fizz_buzz('input2.txt')
rev_fizz_buzz('input3.txt')
