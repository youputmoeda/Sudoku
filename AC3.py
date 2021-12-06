from sudoku import Sudoku


# takes board, current_arc[0](a) and current_arc[1](b) as parameters
# returns true iff domain b is revised
def revise(board, a, b):

    #Make variable `x` arc consistent with variable `y`.
    #To do so, remove values from `domains[x]` for which there is no
    #possible corresponding value for `y` in `domains[y]`.
    #Return True if a revision was made to the domain of `x`; return
    #False if no revision was made.

    revised = False
    print(a) #A1
    print(board.domain[a]) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(b) #A2
    print(board.domain[b])
    # check each value in the domain of x1
    for x in board.domain[a]:
        for y in board.domain[b]:
            if any [x != y]:
                revised = False
        else:
            board.domain[a].remove(x) # delete from domain if true
            revised = True

    return revised


def ac3(board):
    """
    Update `domains` such that each variable is arc consistent.
    """

    # Add all the arcs to a queue.
    queue = list(board.constraints)
    # Repeat until the queue is empty
    while queue:
        # Take the first arc off the queue (dequeue)
        Current_arc = queue.pop(0)
        # Make x arc consistent with y
        revised = revise(board, Current_arc[0], Current_arc[1])

        # If the x domain has changed
        if revised:
            # check if D1 is = 0, which means no solution
            if not board.domain(Current_arc[0]):
                return False
            # else for each neighbour of
            for neighbours in board.neighbours[Current_arc[0]]:
                # will skip if x2 is found as we do not need this value appended
                if neighbours == Current_arc[1]:
                    continue
                tmp_list = [neighbours, Current_arc[0]]
                queue.append(tmp_list)

def main():
    InputFile = open('sudoku.txt')
    game_board = list()
    for line in InputFile:
        if line.strip():
            game_board += [int(i) for i in line.split(' ')]
    # Close the text file
    InputFile.close
    # Create the sudoku object
    board = Sudoku(game_board)
    
    ac3(board)

if __name__ == "__main__":
    main()