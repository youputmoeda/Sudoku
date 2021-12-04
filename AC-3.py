from sudoku import Sudoku


def revise(board, x, y):

    #Make variable `x` arc consistent with variable `y`.
    #To do so, remove values from `domains[x]` for which there is no
    #possible corresponding value for `y` in `domains[y]`.
    #Return True if a revision was made to the domain of `x`; return
    #False if no revision was made.


    revised = False

    # Get x and y domains
    x_domain = Sudoku.domain[x]
    y_domain = Sudoku.domain[y]

    # Get all arc (x, y) constraints
    all_constraints = [
        constraint for constraint in Sudoku.constraints if constraint[0] == x and constraint[1] == y]

    for x_value in x_domain:
        satisfies = False
        for y_value in y_domain:
            for constraint in all_constraints:
                constraint_func = Sudoku.constraints[constraint]
                if constraint_func(x_value, y_value):
                    satisfies = True
        if not satisfies:
            x_domain.remove(x_value)
            revised = True

    return revised


def ac3():
    """
    Update `domains` such that each variable is arc consistent.
    """
    # Add all the arcs to a queue.
    queue = Sudoku.domain[:]

    # Repeat until the queue is empty
    while queue:
        # Take the first arc off the queue (dequeue)
        (x, y) = queue.pop(0)

        # Make x arc consistent with y
        revised = revise(x, y)

        # If the x domain has changed
        if revised:
            # Add all arcs of the form (k, x) to the queue (enqueue)
            Sudoku.neighbors[x] = [neighbor for neighbor in Sudoku.domain if neighbor[1] == x]
            queue = queue + Sudoku.neighbors[x]

def main():
    InputFile = open('sudoku.txt')
    game_board = list()
    for line in InputFile:
        game_board += [int(i) for i in line.split(' ')]
    # Close the text file
    InputFile.close
    # Create the sudoku object
    board = Sudoku(game_board)

if __name__ == "__main__":
    main()