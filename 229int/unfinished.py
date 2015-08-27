import itertools


# Set the highest divisor to consider
LARGEST_DIVISOR = 20
MAX_SEARCH = 1000

# Read data
with open('/home/wes/Documents/github/daily/229int/input3.txt', 'r') as open_infile:
    goal = open_infile.read().split('\n')

# Get length of combo
max_letter = max({char for row in goal for char in row})

divisor_letters = [chr(x + 97) for x in range(ord(max_letter) - 97 + 1)]

n_divisors = len(divisor_letters)

LARGEST_DIVISOR = len(goal) + 1

initial_combo = [1] * n_divisors

for letter in divisor_letters:
    first = [goal.index(row) for row in goal if letter in row]
    if first:
        initial_combo[divisor_letters.index(letter)] = first[0]
    else:
        initial_combo[divisor_letters.index(letter)] = LARGEST_DIVISOR


# Generate the cartesian product of 1 through the largest divisor variable
combos = [x for x in itertools.product(range(1, LARGEST_DIVISOR+1), repeat = n_divisors)]

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

        # ... or if the list gets longer than the goal
        if len(check) > 0 and check != goal[:len(check)]:
            break

        # Stop searching if you hit the goal...
        if check == goal:
            break

    # If this combo matches the goal, print it and quit
    if check == goal:
        print(str(' '.join([str(x) for x in combo])))
        break
