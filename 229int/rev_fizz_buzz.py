import itertools


def rev_fizz_buzz(file):

    # Set the highest divisor to consider
    LARGEST_DIVISOR = 20
    MAX_SEARCH = 1000

    # Read data
    with open(file, 'r') as infile:
        goal = infile.read().split('\n')

    # Get length of combo
    n = ord(max([char for row in goal for char in row])) - 97 + 1

    # Generate the cartesian product of 1 through the largest divisor variable
    combos = [x for x in itertools.product(range(1, LARGEST_DIVISOR+1), repeat = n)]

    # Check every possible combination
    for combo in combos:

        # Populate this list with output and check until it matches the goal combo
        check = []

        # Just count
        for i in range(MAX_SEARCH):

            # Add rows to the check list
            row = ''
            for divisor in combo:
                if (i % int(divisor)) == 0 and i is not 0:
                    row += chr(combo.index(divisor) + 97)
            if row:
                check.append(row)

            # Stop searching if you hit the goal...
            if check == goal:
                break

            # ... or if the list gets longer than the goal
            if len(check) > len(goal):
                break

        # If this combo matches the goal, print it and quit
        if check == goal:
            print(str(' '.join([str(x) for x in combo])))
            break

# Try it out
rev_fizz_buzz('input1.txt')
rev_fizz_buzz('input2.txt')
rev_fizz_buzz('input3.txt')
