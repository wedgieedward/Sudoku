"""
Sudoku Generator Class DX
"""
import random
import time

class Puzzle(object):
	def __init__(self):
		self._complete = False
		self.avaliable_cells = []
		self.puzzle_attempts = 5

	def process(self):
		"""
		Creates and returns the generated puzzle for this object
		"""
		start_time = time.clock()
		retry_attempts = 0
		while self._complete == False or retry_attempts > self.puzzle_attempts:
			success = self.process_puzzle_attempt()
			if not success:
				self.reset_puzzle_attempt()
		

	def process_puzzle_attempt(self):
		"""
		Will try and produce a complete puzzle
		"""
		success_counter = 0
		for number in range(9):
			value_to_insert = self.get_unused_number()
			insert_success = self.process_current_number(value_to_insert)
			if insert_success:
				success_counter += 1

		if success_counter == 9:
			return True
		else:
			return False

	def process_current_number(self, number):
		"""
		Given a number, will try to randomly insert the number into the grid
		"""
		return True

	def reset_puzzle_attempt(self):
		pass


	def get_available_cells(self):
		"""
		Returns the co-ordinates of all the cells that are empty
		"""
		pass

	def get_unused_number(self):
		"""
		returns an unused number at random
		"""
		pass


def Build(self):

                if self.Reset_Build == True:  # If for what ever reason the grid needs to be reset all variables reset
                    self.Rows = [self.Blank_List(
                    ), self.Blank_List(
                    ), self.Blank_List(
                    ), self.Blank_List(),
                        self.Blank_List(), self.Blank_List(), self.Blank_List(), self.Blank_List(), self.Blank_List()]
                    self.Get_Avaliable_Cells()
                    temp_Counter = 0
                    if debug:
                        print 'BUILD RESET' * 10
                    self.Reset_Build = False
                    self.Unused_Numbers = range(1, 10)
            end_time = time.clock()
            if debug:
                print "COMPLETED IN", (end_time - start_time)
                print self.Rows
            self.PuzzleCreated = True
            self.Make_List()
                           # Creates an array of 9 lists that contain the 9
                           # numbers of each row

        # Function to place the current selected number into the grid randomly
        # 9 times
        def Complete_Current_Number(self):
            global locator
            if locator:
                print 'in Complete_Current_Number'
            global debug
            import random

            Current_Positions = []
            Fail_Count = 0
            while len(Current_Positions) != 9 and Fail_Count <= 5:  # While the current number has not been put in 9 positions,
                                                  # and it hasn't failed more
                                                  # than 3 times
                try:
                    # Works out if the number has to be placed in a single location
                    Single_Cell = self.Check_Single_Item()

                    if Single_Cell == None:  # If it doesn't have to be placed in a single location

                        Single_Cell = random.choice(
                            self.Avaliable_Cells)  # Place the number in a random avaliable cell
                        if debug:
                            print 'Random Cell, Placed in', Single_Cell

                        self.Update_Avaliable_List(Single_Cell / 10, Single_Cell %
                                                   10, self.Current_Number)  # Updates the list of avaliable locations
                        Current_Positions += [
                            Single_Cell]  # The location the number was just placed in is added to the array
                                                 # of positions where the cell
                                                 # has been placed
                    elif Single_Cell >= 0:  # If it does have to be placed into a single locatiion
                        if debug:
                            print 'Placed in Single Cell', Single_Cell
                        self.Update_Avaliable_List(Single_Cell / 10, Single_Cell %
                                                   10, self.Current_Number)  # Updates the list of avaliable locations
                        Current_Positions += [
                            Single_Cell]  # The Location the number was just placed in is added to the array
                                                # of positions where the cell
                                                # has been placed
                except IndexError:  # If it finds that there is no more locations that the number can be placed in, it starts the whole process again
                    if debug:
                        print 'Excepted Index Error, Trying This Number Again'
                        print 'Current Current_Positions', Current_Positions
                    # Resets the list of avaliable locations
                    Current_Positions = []
                    self.Get_Avaliable_Cells()
                    Fail_Count += 1
                    if debug:
                        print "Attempt", Fail_Count, "Failed"
            if Fail_Count >= 6:  # If it has failed to try and fit the numbers into correct locations 6 times
                self.Reset_Build = True  # Makes it so the whole sudoku has to be started again
            else:
                if debug:
                    print "Excepted This List Of Positions, Now Adding Them To Grid", Current_Positions

                for x in Current_Positions:
                    self.Change_Number(x % 10, x / 10, self.Current_Number)
                                       # formats the locations into a format
                                       # the game can interperate

        # Function to check if a number has to go in a particular cell
        def Check_Single_Item(self):
            global locator
            if locator:
                print 'in Check_Single_Item'
            global debug
            if debug:
                print 'in check single item'
            Blocks = self.Block_List()
            Variable = None
            # Checks through each block of 3*3 cells to see if there is only a
            # single avaliable location from the list of avaliable locations in
            # that block
            for Block in Blocks:
                temp = 0
                counter = 0
                for item in Block:
                    if item in self.Avaliable_Cells:
                        counter += 1
                        temp += item

                if counter == 1:
                    for item in Block:
                        if item in self.Avaliable_Cells:
                            Variable = item

            return Variable
            if Variable == True:
                return 0
            else:
                return 22

        # Updates the list of Avaliable cells
        def Update_Avaliable_List(self, row, column, new_number):
            global locator
            if locator:
                print 'in Update_Avaliable_List'
            self.Change_Number(column, row, new_number)
            Slots = self.Avaliable_Cells
            Slots.remove(int(str(row) + str(column)))
            Remove_Items = []
            for x in Slots:
                if x % 10 == column:
                    Remove_Items += [x]

                if int(x / 10) == row:
                    Remove_Items += [x]

            for y in Remove_Items:
                Slots.remove(y)

            Blocks = self.Block_List()
            XY = int(str(row) + str(column))
            for count in range(9):
                Current_Block = Blocks[count]
                if XY in Current_Block:
                    for xy in Current_Block:
                        if xy in Slots:
                            Slots.remove(xy)

            self.Avaliable_Cells = Slots

        # Function to find the current avaliable cells from self.Rows
        def Get_Avaliable_Cells(self):
            global locator
            if locator:
                print 'in Get_Avaliable_Cells'
            self.Avaliable_Cells = []
            row_counter = 0
            for row in self.Rows:
                row_counter += 1
                column_counter = 0
                for column in row:
                    column_counter += 1
                    if column == 0:
                        self.Avaliable_Cells += [
                            int(str(row_counter) + str(column_counter))]
