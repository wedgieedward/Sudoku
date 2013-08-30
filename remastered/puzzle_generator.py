"""
Sudoku Generator Class DX
"""
import random
import time

class Puzzle:
    """
    Sudoku Puzzle Generator
    """
    def __init__(self):
        self._complete = False
        self._avaliable_cells = []
        self.max_puzzle_attempts = 5
        self._unused_numbers = []
        self.completion_time = 0
        self.retry_attempts = 0

    def process(self):
        """
        Creates and returns the generated puzzle for this object
        """
        start_time = time.clock()
        while (self._complete == False or self.retry_attempts > self.max_puzzle_attempts):
            success = self.process_puzzle_attempt()
            if (not success):
                self.retry_attempts += 1
                self.reset_puzzle_attempt()
            else:
                self._complete = True
                print("Done!!")
                return self._avaliable_cells
        
        end_time = time.clock()
        self.completion_time = end_time - start_time

        return self._avaliable_cells

    def process_puzzle_attempt(self):
        """
        Will try and produce a complete puzzle
        """
        self.reset_puzzle_attempt() # Start attempt fresh
        for number in range(9):
            value_to_insert = self.get_unused_number()
            insert_success = self.process_current_number(value_to_insert)
            if not insert_success:
                return False
        return True

    def process_current_number(self, number):
        """
        Given a number, will try to randomly insert the number into the grid
        """
        available_cells = self.get_available_cells()
        for row in range(9):
            insert = False
            number_of_positions = len(available_cells[row])
            for _insert_try in range(number_of_positions):
                col = random.choice(available_cells[row])
                available_cells[row].remove(col)
                valid = self.validate_position(number, row, col)
                if valid:
                    self.add_number_to_position(number, row, col)
                    insert = True
                    break
            if not insert:
                return False
        return True

    def validate_position(self, number, row, col):
        """
        Check that placing the number in the position is valid
        """
        # check if it is uniue to row
        if number in self._avaliable_cells[row]:
            return False

        # check if it is unique to column
        for this_row in self._avaliable_cells:
            if self._avaliable_cells[col] == number:
                return False

        # check if it is unique to block
        block_1 = [0, 1, 2]
        block_2 = [3, 4, 5]
        block_3 = [6, 7, 8]
        blocks = [block_1, block_2, block_3]

        col_block = None
        row_block = None

        for block in blocks:
            if row in block:
                row_block = block
            if col in block:
                col_block = block

        for b_row in row_block:
            for c_row in col_block:
                if self._avaliable_cells[b_row][c_row] == number:
                    return False

        return True

    def add_number_to_position(self, number, row, col):
        """
        Given a number, row and column
        inserts the number into that position
        """
        self._avaliable_cells[row][col] = number

    def reset_puzzle_attempt(self):
        """
        Will reset _avaliable_cells
        Will reset _unused_numbers
        """
        self._avaliable_cells = []
        self._unused_numbers = []
        self._puzzle = []
        for j in range(9):
            self._avaliable_cells += [self.generate_empty_row()]
            self._unused_numbers += [j+1]

    def generate_empty_row(self):
        """
        Returns an array of length 9 filled with 0's 
        """
        row = []
        for j in range(9):
            row += [0]
        return row

    def get_available_cells(self):
        """
        Returns the co-ordinates of all the cells that are empty
        """
        available_cells = []
        for row in range(9):
            row_cells_empty = []
            for col in range(9):
                if self._avaliable_cells[row][col] == 0:
                    row_cells_empty += [col]
            available_cells += [row_cells_empty]

        return available_cells

    def get_unused_number(self):
        """
        returns an unused number at random
        """
        number = random.choice(self._unused_numbers)
        self._unused_numbers.remove(number)
        return number


game = Puzzle()
print(game.process())
print("Completed in %s attempts" % (game.retry_attempts+1, ))


