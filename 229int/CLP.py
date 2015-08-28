import Numberjack


def rev_fizz_buzz(textfile):

    # Read in input
    with open(textfile, 'r') as infile:
            lines = infile.read().split('\n')

    # Figure out number of variables
    n_variables = ord(max({char for row in lines for char in row})) - 97 + 1

    # Create Numberjack variables and model objects
    # Must define max divisor to consider
    MAX_DIVISOR = 5000
    variables = {}
    for asc in range(n_variables):
        variables[chr(asc + 97)] = Numberjack.Variable(MAX_DIVISOR, chr(asc + 97))
    model = Numberjack.Model()

    # Track whether or not a variable is found in the input
    encountered = set()

    # This dict will keep track of how many multiples, starting at 0,
    # have been encountered for each variable
    multiples = {chr(x + 97): 0 for x in range(n_variables)}

    # Loop over input lines
    for line in lines:

        # Get the letters found on this line
        letters = list(line)

        # Record that we've encountered each letter and increase it's multiple
        for letter in letters:
            encountered.add(letter)
            multiples[letter] += 1

        # Add constraints to the model. If variables are found on the same
        # line, their current multiples are equal. Otherwise, the current
        # multiples of variables on this line are greater than others
        for letter in letters:
            for var in multiples:
                if var in letters:
                    model.add(multiples[letter] * variables[letter] ==
                              multiples[var] * variables[var])
                else:
                    model.add(multiples[letter] * variables[letter] >
                              multiples[var] * variables[var])

    # Get variable letters and sort
    vs = variables.keys()
    vs.sort()

    # If we never saw a variable, it must be larger than last seen multiples
    for var in vs:
        if var not in encountered:
            for key in multiples:
                model.add(variables[var] > multiples[key] * variables[key])

    # Pass variables to the model with a solver (Mistral) and print solution
    solver = model.load('Mistral', [variables[key] for key in vs])
    print ' '.join([str(x) for x in solver.get_solution()])

# Try it
rev_fizz_buzz('input1.txt')
rev_fizz_buzz('input2.txt')
rev_fizz_buzz('input3.txt')
rev_fizz_buzz('challenge.txt')
