####### Computing Sudoku Program
####### Created By Edward Thomason As Part Of His A-Level Computing Project
####### Designed And Created For Bill Manely and Hartlip CoE Primary School
####### Created and Tested in Python 2.6.1
### All modules needed come as a standard in Python 2.6.1


### Testing Variables
debug = 0 # Make 1 if you wish to debug
locator = 0 # Make 1 if you wish to know which functions are being called
testing = 0 # Make 1 if you wish to be in testing mode, this sets all hints to 200
folder = 'E:/HighScores.txt' # This must be the location of the HighScores.txt file, change if appropriate

### Compatability Validation
### Try statement to work out if the user has the correct Tkinter, Tkfont and random modules
### If the Program encounters an error, it will stop and an error message will be displayed
try:
    print ( 'This Sudoku Program Was Designed By Edward Thomason')
    print ('As Part Of His A Level Computing Project\n')
    try:
        import random
        from Tkinter import *
        import tkFont
        print ('This Version Of Python Is Compatible With The Sudoku Game')

    ### Appropriate Error If Modules Not Found
    except ImportError:
        print ('This Version Of Python Is Not Compatable With The Sudoku Game')
        print ('Was Designed For Version 2.6.1 and lower')
        errortrue = 1
        
    ### Try statement to see if it can find the highscores .txt file
    try:
        a = open ( folder,'r')
        a.close()
        print 'High Scores File Was Located\n'

    ### Appropriate error if file cannot be found, allows users to still use the program however.
    except IOError:
        print ('High Scores File Could Not Be Located, Scores Cannot Be Saved\n')
        
        

    ### Input statement to make user press enter to start program
    if debug:
        print 'Debug Is Turned On'
    if locator:
        print 'Locator Is Turned On'
    if testing:
        print 'In Test Mode'
    raw_input('\nPress Enter To Continue')

    
    from Tkinter import *
    import tkFont

    class Application():
        def __init__(self):
            global locator,testing, folder
            import random
            
            if locator:
                print 'in Application'
                
            self.Location_File = folder 
            
            ###Creates Frames###
            self.root = Tk()
            
            self.Reset_Variables()### Sets all Variables Needed to their default values
            
            self.GridFrame = Frame(self.root)
            self.GridFrame.grid(row = 1, column = 1)
            self.UnderFrame = Frame(self.root)
            #self.UnderFrame.grid(row = 2, column = 1)
            self.ButtonFrame = Frame(self.root)
            self.ButtonFrame.grid(row = 1, column = 2)
            self.root.grid()

            ##Under Frame Widgets
            self.Subtitle = Label(self.UnderFrame,text = "Created By Edward Thomason")
            self.Subtitle.grid(row = 0, column = 0)
            self.Stitle = Label(self.UnderFrame,text = "Final Build: Hartlip CoE Primary")
            self.Stitle.grid(row = 1, column = 0)

            #####Formatting Buttons
            self.Edward_Font = tkFont.Font(size = 10, weight = 'bold')
            self.Button_Width = 6
            self.Button_Height = 3
            self.Active_Background_Colour = 'red'
            self.Button_Background = 'white'
            ###################
            ###Name_Entry_Vars###
            self.text_var = StringVar(self.root)
            self.name_var = StringVar(self.root)
            self.Player_Name = None
            #####################
            ###Difficulty Vars###
            ##Must Be Even
            ##Edit Appropriatly
            ##This number is the total amount of numbers that are removed depending on each difficulty
            self.Easy_Remove_Total = 44
            self.Med_Remove_Total = 50
            self.Hard_Remove_Total = 56
            ##These numbers are the penalty depending on what difficulty they used
            self.Easy_Time_Penalty = 120
            self.Med_Time_Penalty = 60
            self.Hard_Time_Penalty = 0
            ##This is the penalty that is added on depending on how many hints they have used or
            ##if they incorrectly checked to see if they have finished
            self.Hint_Time_Penalty = 40
            self.Check_Time_Penalty = 40

            ## The Number of hints people are allowed depending on their difficulties
            self.Hints = 0 #Must remain 0
            self.Easy_Hints = 2
            self.Med_Hints = 4
            self.Hard_Hints = 6

            ##Sets hints all to 200 if testing is set to 1
            ## Reccomend that these numbers are set to be >= 81 (9*9 = 81)
            if testing:
                self.Easy_Hints = 200
                self.Med_Hints = 200
                self.Hard_Hints = 200
            #####################
    
                       
            ###Run_Code#######################################################################
            
            self.NewGame()

            ##################################################################################

        def NewGame(self):
            self.Build()
            self.Name_Entry_Window()

    ###############################################################################################

        ### Name Entry Screen Code And Functions#####################################
        def Name_Entry_Window(self):
            global locator
            if locator:
                print 'in Name_Entry_Window'
            
            self.Entry_Label = Label(self.GridFrame,text = "Please Enter Your Name (John, Smith)")
            self.Entry_Label.grid(row = 1, column = 0)

            self.Entry_Box = Entry(self.GridFrame, textvariable = self.text_var)
            self.Entry_Box.grid(row = 1, column =1)

            self.Enter_Button = Button(self.GridFrame, text = "Enter Name",
                               command = self.get_name)
            self.Enter_Button.grid(column = 1, row = 2)

            self.Update_Label = Label(self.GridFrame, textvariable = self.name_var,fg = 'red' )
            self.Update_Label.grid(row = 3, column = 0,columnspan = 2)

            self.Play_Button = Button(self.GridFrame, text = "Continue", command = self.clear_Entry_Window)
            self.Restart_Button = Button(self.GridFrame, text = 'Re-Enter Name', command =self.redo_name)
            
        def redo_name(self):
            global locator
            if locator:
                print 'in redo_name'
            
            self.Update_Label.grid_forget()
            self.Play_Button.grid_forget()
            self.Restart_Button.grid_forget()
            self.Name_Entry_Window()
            self.name_var.set('')
            self.text_var.set('')

        def clear_Entry_Window(self):
            global locator
            if locator:
                print 'in clear_Entry_Window'
            
            self.Update_Label.grid_forget()
            self.Play_Button.grid_forget()
            self.Restart_Button.grid_forget()
            self.Difficulty_Window()

            
        def get_name(self):
            global locator
            if locator:
                print 'in get_name'

            self.Player_Name = self.Entry_Box.get()
            
            if self.Player_Name == '':
                x = 'Invalid Name, Please Re-Enter'
                self.name_var.set(x)
            elif ' ' not in self.Player_Name or ',' not in self.Player_Name:
                x = 'Please Make Sure You Have Entered First And Second Names'
                self.name_var.set(x)
        
            else:
                self.Play_Button.grid(row = 4, column = 0)
                self.Restart_Button.grid(row = 4, column = 1)
                x = ('Name Has Been Set')
                self.name_var.set(x)
                self.Enter_Button.grid_forget()
                self.Entry_Label.grid_forget()
                self.Entry_Box.grid_forget()
                self.root.title(self.Player_Name)

    ###############################################################################################
        ### Difficulty Screen code and funtions####################################################
        def Difficulty_Window(self):
            global locator
            if locator:
                print 'in Difficulty_Window'
            name = str(self.Player_Name) + ': Please Select Difficulty'
            self.root.title(name)

            self.Label_Difficulty = Label(self.GridFrame, text = 'Please Select Difficulty:')
            self.Label_Difficulty.grid(row = 0, column = 0)

            self.Diff_Button_Easy = Button(self.GridFrame, text = 'Easy Puzzle',command = self.easy_puzzle)
            self.Diff_Button_Easy.grid(row = 1, column = 0, columnspan = 2,sticky = W)
            
            self.Diff_Button_Intermediate = Button(self.GridFrame, text = 'Intermediate Puzzle',command = self.med_puzzle)
            self.Diff_Button_Intermediate.grid(row = 2, column = 0, columnspan = 2, sticky = W)
            
            self.Diff_Button_Hard = Button(self.GridFrame, text = 'Hard Puzzle',command = self.hard_puzzle)
            self.Diff_Button_Hard.grid(row = 3, column = 0, columnspan = 2, sticky = W)

        def clear_Difficulty_Window(self):
            global locator
            if locator:
                print 'in clear_Difficulty_Window'
            
            self.Label_Difficulty.grid_forget()
            self.Diff_Button_Easy.grid_forget()
            self.Diff_Button_Intermediate.grid_forget()
            self.Diff_Button_Hard.grid_forget()

        def easy_puzzle(self):
            global locator
            import time
            self.Time_Penalty += self.Easy_Time_Penalty
            self.Difficulty_Used = 'Easy Puzzle'
            self.Start_Time = time.clock()
            if locator:
                print 'in easy_puzzle'
                
            self.clear_Difficulty_Window()
            self.Numbers = self.Create_Easy()
            title = self.Player_Name + ': Easy Puzzle'
            self.root.title(title)

            self.Hints = self.Easy_Hints
            self.Hint_Text.set(('Hints:'+str(self.Hints)))
            
            self.Sudoku_Window()
            self.Set_Grid()
            self.Reset_Cell_Colours()
            
        def med_puzzle(self):
            global locator
            import time
            self.Time_Penalty += self.Med_Time_Penalty
            self.Difficulty_Used = 'Intermediate Puzzle'
            self.Start_Time = time.clock()
            if locator:
                print 'in med_puzzle'
                
            self.clear_Difficulty_Window()
            self.Numbers = self.Create_Med()
            title = self.Player_Name + ': Intermediate Puzzle'
            self.root.title(title)

            self.Hints = self.Med_Hints
            
            self.Hint_Text.set(('Hints:'+str(self.Hints)))
            
            self.Sudoku_Window()
            self.Set_Grid()
            self.Reset_Cell_Colours()
            
        def hard_puzzle(self):
            global locator
            import time
            self.Time_Penalty += self.Hard_Time_Penalty
            self.Difficulty_Used = 'Hard Puzzle'
            self.Start_Time = time.clock()
            if locator:
                print 'in hard_puzzle'
                
            self.clear_Difficulty_Window()
            self.Numbers = self.Create_Hard()
            title = self.Player_Name + ': Hard Puzzle'
            self.root.title(title)

            self.Hints = self.Hard_Hints
            
            self.Hint_Text.set(('Hints:'+str(self.Hints)))
            
            self.Sudoku_Window()
            self.Set_Grid()
            self.Reset_Cell_Colours()

        def Set_Grid(self):## Sets the grid up with the correct numbers
            global locator
            if locator:
                print 'in Set_Grid'
            Number_List = self.Numbers
            for x in range (9):
                for y in range(9):
                    selection = Number_List[x][y]
                    if selection == 0:
                        selection = ''
                    else:
                        self.Btn_Change_List[x][y] = False
                        self.Buttons[x][y].config(activebackground = 'red')
                    if debug:
                        print selection
                    self.Button_Var[x][y].set(selection)
    ###############################################################################################
        def Reset_Cell_Colours(self):
            for j in range(9):
                for i in range(9):
                    self.Buttons[j][i].config(background = self.Button_Background)
                                      
    ###############################################################################################

        def Sudoku_Window(self):
            global locator
            if locator:
                print 'in Sudoku_Window'

            ###Active Number Buttons###
            ## Side Controll Buttons
            self.button1 = Button ( self.ButtonFrame, text='1',activebackground = 'yellow',background='black', fg = 'white', font = self.Edward_Font,
                            width = self.Button_Width, height = self.Button_Height,
                            command=self.Button_1_Press)      
            self.button1.grid(column = 0, row = 1)
            self.button2 = Button ( self.ButtonFrame, text='2',activebackground = 'yellow',background='black', fg = 'white', font = self.Edward_Font,
                            width = self.Button_Width, height = self.Button_Height,
                            command=self.Button_2_Press)      
            self.button2.grid(column = 0, row = 2)
            self.button3 = Button ( self.ButtonFrame, text='3',activebackground = 'yellow',background='black', fg = 'white', font = self.Edward_Font,
                            width = self.Button_Width, height = self.Button_Height,
                            command=self.Button_3_Press)      
            self.button3.grid(column = 0, row = 3)
            self.button4 = Button ( self.ButtonFrame, text='4',activebackground = 'yellow',background='black', fg = 'white', font = self.Edward_Font,
                            width = self.Button_Width, height = self.Button_Height,
                            command=self.Button_4_Press)      
            self.button4.grid(column = 0, row = 5)
            self.button5 = Button ( self.ButtonFrame, text='5',activebackground = 'yellow',background='black', fg = 'white', font = self.Edward_Font,
                            width = self.Button_Width, height = self.Button_Height,
                            command=self.Button_5_Press)      
            self.button5.grid(column = 0, row = 6)
            self.button6 = Button ( self.ButtonFrame, text='6',activebackground = 'yellow',background='black', fg = 'white', font = self.Edward_Font,
                            width = self.Button_Width, height = self.Button_Height,
                            command=self.Button_6_Press)      
            self.button6.grid(column = 0, row = 7)
            self.button7 = Button ( self.ButtonFrame, text='7',activebackground = 'yellow',background='black', fg = 'white', font = self.Edward_Font,
                            width = self.Button_Width, height = self.Button_Height,
                            command=self.Button_7_Press)      
            self.button7.grid(column = 0, row = 9)
            self.button8 = Button ( self.ButtonFrame, text='8',activebackground = 'yellow',background='black', fg = 'white', font = self.Edward_Font,
                            width = self.Button_Width, height = self.Button_Height,
                            command=self.Button_8_Press)      
            self.button8.grid(column = 0, row = 10)
            self.button9 = Button ( self.ButtonFrame, text='9',activebackground = 'yellow',background='black', fg = 'white', font = self.Edward_Font,
                            width = self.Button_Width, height = self.Button_Height,
                            command=self.Button_9_Press)      
            self.button9.grid(column = 0, row = 11)
            self.button0 = Button ( self.ButtonFrame, text='Clear',activebackground = 'yellow',background='black', fg = 'white', font = self.Edward_Font,
                            width =self.Button_Width,height = self.Button_Height,
                            command=self.Button_0_Press)      
            self.button0.grid(column = 1, row = 1)
            
            self.Check_Button = Button(self.ButtonFrame, text = 'Check',activebackground = 'green', background = 'black', fg = 'white', font = self.Edward_Font
                               ,width = self.Button_Width, height = self.Button_Height,
                               command = self.Check_Button_Press)
            self.Check_Button.grid(column = 1, row = 11)
            
            self.Hint_Button =Button(self.ButtonFrame, textvariable = self.Hint_Text, activebackground = 'green', background = 'black', fg = 'white', font = self.Edward_Font
                               ,width = self.Button_Width, height = self.Button_Height
                             ,command = self.Hint_Button_Press)
            self.Hint_Button.grid(column = 1, row = 9)

            self.Active_Buttons = [self.button0,self.button1,self.button2,self.button3
                             ,self.button4,self.button5,self.button6,self.button7
                             ,self.button8,self.button9,self.Hint_Button, self.Check_Button]
            ###End Active Buttons###

            ###Add Grid Buttons###
            ###
            self.button_11 = Button(self.GridFrame, width = self.Button_Width,height = self.Button_Height,font = self.Edward_Font ,textvariable = self.tv_11,text = self.tv_11, command = self.bp_11)
            self.button_11.grid(column = 1, row = 1)
            self.button_12 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height,font = self.Edward_Font ,textvariable = self.tv_12,text = self.tv_12, command = self.bp_12)
            self.button_12.grid(column = 1, row = 2)
            self.button_13 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height,font = self.Edward_Font ,textvariable = self.tv_13,text = self.tv_13, command = self.bp_13)
            self.button_13.grid(column = 1, row = 3)
            self.button_21 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height,font = self.Edward_Font ,textvariable = self.tv_21,text = self.tv_21, command = self.bp_21)
            self.button_21.grid(column = 2, row = 1)
            self.button_22 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height,font = self.Edward_Font ,textvariable = self.tv_22,text = self.tv_22, command = self.bp_22)
            self.button_22.grid(column = 2, row = 2)
            self.button_23 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height,font = self.Edward_Font ,textvariable = self.tv_23,text = self.tv_23, command = self.bp_23)
            self.button_23.grid(column = 2, row = 3)
            self.button_31 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height,font = self.Edward_Font ,textvariable = self.tv_31,text = self.tv_31, command = self.bp_31)
            self.button_31.grid(column = 3, row = 1)
            self.button_32 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height,font = self.Edward_Font ,textvariable = self.tv_32,text = self.tv_32, command = self.bp_32)
            self.button_32.grid(column = 3, row = 2)
            self.button_33 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height,font = self.Edward_Font ,textvariable = self.tv_33,text = self.tv_33, command = self.bp_33)
            self.button_33.grid(column = 3, row = 3)
            ###
            self.button_14 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_14,command = self.bp_14)
            self.button_14.grid(column = 1, row = 5)
            self.button_15 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_15,command = self.bp_15)
            self.button_15.grid(column = 1, row = 6)
            self.button_16 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_16,command = self.bp_16)
            self.button_16.grid(column = 1, row = 7)
            self.button_24 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_24,command = self.bp_24)
            self.button_24.grid(column = 2, row = 5)
            self.button_25 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_25,command = self.bp_25)
            self.button_25.grid(column = 2, row = 6)
            self.button_26 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_26,command = self.bp_26)
            self.button_26.grid(column = 2, row = 7)
            self.button_34 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_34,command = self.bp_34)
            self.button_34.grid(column = 3, row = 5)
            self.button_35 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_35,command = self.bp_35)
            self.button_35.grid(column = 3, row = 6)
            self.button_36 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_36,command = self.bp_36)
            self.button_36.grid(column = 3, row = 7)
            ###
            self.button_17 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_17,command = self.bp_17)
            self.button_17.grid(column = 1, row = 9)
            self.button_18 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_18,command = self.bp_18)
            self.button_18.grid(column = 1, row = 10)
            self.button_19 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_19,command = self.bp_19)
            self.button_19.grid(column = 1, row = 11)
            self.button_27 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_27,command = self.bp_27)
            self.button_27.grid(column = 2, row = 9)
            self.button_28 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_28,command = self.bp_28)
            self.button_28.grid(column = 2, row = 10)
            self.button_29 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_29,command = self.bp_29)
            self.button_29.grid(column = 2, row = 11)
            self.button_37 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_37,command = self.bp_37)
            self.button_37.grid(column = 3, row = 9)
            self.button_38 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_38,command = self.bp_38)
            self.button_38.grid(column = 3, row = 10)
            self.button_39 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_39,command = self.bp_39)
            self.button_39.grid(column = 3, row = 11)
            ###
            self.button_41 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_41,command = self.bp_41)
            self.button_41.grid(column = 5, row = 1)
            self.button_42 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_42,command = self.bp_42)
            self.button_42.grid(column = 5, row = 2)
            self.button_43 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_43,command = self.bp_43)
            self.button_43.grid(column = 5, row = 3)
            self.button_51 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_51,command = self.bp_51)
            self.button_51.grid(column = 6, row = 1)
            self.button_52 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_52,command = self.bp_52)
            self.button_52.grid(column = 6, row = 2)
            self.button_53 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_53,command = self.bp_53)
            self.button_53.grid(column = 6, row = 3)
            self.button_61 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_61,command = self.bp_61)
            self.button_61.grid(column = 7, row = 1)
            self.button_62 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_62,command = self.bp_62)
            self.button_62.grid(column = 7, row = 2)
            self.button_63 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_63,command = self.bp_63)
            self.button_63.grid(column = 7, row = 3)
            ###
            self.button_44 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_44, command = self.bp_44)
            self.button_44.grid(column = 5, row = 5)
            self.button_45 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_45, command = self.bp_45)
            self.button_45.grid(column = 5, row = 6)
            self.button_46 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_46, command = self.bp_46)
            self.button_46.grid(column = 5, row = 7)
            self.button_54 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_54, command = self.bp_54)
            self.button_54.grid(column = 6, row = 5)
            self.button_55 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_55, command = self.bp_55)
            self.button_55.grid(column = 6, row = 6)
            self.button_56 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_56, command = self.bp_56)
            self.button_56.grid(column = 6, row = 7)
            self.button_64 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_64, command = self.bp_64)
            self.button_64.grid(column = 7, row = 5)
            self.button_65 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_65, command = self.bp_65)
            self.button_65.grid(column = 7, row = 6)
            self.button_66 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_66, command = self.bp_66)
            self.button_66.grid(column = 7, row = 7)
            ###
            self.button_47 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_47, command = self.bp_47)
            self.button_47.grid(column = 5, row = 9)
            self.button_48 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_48, command = self.bp_48)
            self.button_48.grid(column = 5, row = 10)
            self.button_49 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_49, command = self.bp_49)
            self.button_49.grid(column = 5, row = 11)
            self.button_57 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_57, command = self.bp_57)
            self.button_57.grid(column = 6, row = 9)
            self.button_58 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_58, command = self.bp_58)
            self.button_58.grid(column = 6, row = 10)
            self.button_59 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_59, command = self.bp_59)
            self.button_59.grid(column = 6, row = 11)
            self.button_67 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_67, command = self.bp_67)
            self.button_67.grid(column = 7, row = 9)
            self.button_68 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_68, command = self.bp_68)
            self.button_68.grid(column = 7, row = 10)
            self.button_69 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_69, command = self.bp_69)
            self.button_69.grid(column = 7, row = 11)
            ###
            self.button_71 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_71, command = self.bp_71)
            self.button_71.grid(column = 9, row = 1)
            self.button_72 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_72, command = self.bp_72)
            self.button_72.grid(column = 9, row = 2)
            self.button_73 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_73, command = self.bp_73)
            self.button_73.grid(column = 9, row = 3)
            self.button_81 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_81, command = self.bp_81)
            self.button_81.grid(column = 10, row = 1)
            self.button_82 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_82, command = self.bp_82)
            self.button_82.grid(column = 10, row = 2)
            self.button_83 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_83, command = self.bp_83)
            self.button_83.grid(column = 10, row = 3)
            self.button_91 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_91, command = self.bp_91)
            self.button_91.grid(column = 11, row = 1)
            self.button_92 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_92, command = self.bp_92)
            self.button_92.grid(column = 11, row = 2)
            self.button_93 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_93, command = self.bp_93)
            self.button_93.grid(column = 11, row = 3)
            ###
            self.button_74 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_74, command = self.bp_74)
            self.button_74.grid(column = 9, row = 5)
            self.button_75 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_75, command = self.bp_75)
            self.button_75.grid(column = 9, row = 6)
            self.button_76 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_76, command = self.bp_76)
            self.button_76.grid(column = 9, row = 7)
            self.button_84 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_84, command = self.bp_84)
            self.button_84.grid(column = 10, row = 5)
            self.button_85 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_85, command = self.bp_85)
            self.button_85.grid(column = 10, row = 6)
            self.button_86 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_86, command = self.bp_86)
            self.button_86.grid(column = 10, row = 7)
            self.button_94 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_94, command = self.bp_94)
            self.button_94.grid(column = 11, row = 5)
            self.button_95 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_95, command = self.bp_95)
            self.button_95.grid(column = 11, row = 6)
            self.button_96 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_96, command = self.bp_96)
            self.button_96.grid(column = 11, row = 7)
            ###
            self.button_77 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_77, command = self.bp_77)
            self.button_77.grid(column = 9, row = 9)
            self.button_78 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_78, command = self.bp_78)
            self.button_78.grid(column = 9, row = 10)
            self.button_79 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_79, command = self.bp_79)
            self.button_79.grid(column = 9, row = 11)
            self.button_87 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_87, command = self.bp_87)
            self.button_87.grid(column = 10, row = 9)
            self.button_88 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_88, command = self.bp_88)
            self.button_88.grid(column = 10, row = 10)
            self.button_89 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_89, command = self.bp_89)
            self.button_89.grid(column = 10, row = 11)
            self.button_97 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_97, command = self.bp_97)
            self.button_97.grid(column = 11, row = 9)
            self.button_98 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_98, command = self.bp_98)
            self.button_98.grid(column = 11, row = 10)
            self.button_99 = Button(self.GridFrame, width = self.Button_Width, height = self.Button_Height ,font = self.Edward_Font ,textvariable = self.tv_99, command = self.bp_99)
            self.button_99.grid(column = 11, row = 11)

            self.Buttons = [[self.button_11,self.button_12,self.button_13,self.button_14,self.button_15,self.button_16,self.button_17,self.button_18,self.button_19],
                        [self.button_21,self.button_22,self.button_23,self.button_24,self.button_25,self.button_26,self.button_27,self.button_28,self.button_29],
                        [self.button_31,self.button_32,self.button_33,self.button_34,self.button_35,self.button_36,self.button_37,self.button_38,self.button_39],
                        [self.button_41,self.button_42,self.button_43,self.button_44,self.button_45,self.button_46,self.button_47,self.button_48,self.button_49],
                        [self.button_51,self.button_52,self.button_53,self.button_54,self.button_55,self.button_56,self.button_57,self.button_58,self.button_59],
                        [self.button_61,self.button_62,self.button_63,self.button_64,self.button_65,self.button_66,self.button_67,self.button_68,self.button_69],
                        [self.button_71,self.button_72,self.button_73,self.button_74,self.button_75,self.button_76,self.button_77,self.button_78,self.button_79],
                        [self.button_81,self.button_82,self.button_83,self.button_84,self.button_85,self.button_86,self.button_87,self.button_88,self.button_89],
                        [self.button_91,self.button_92,self.button_93,self.button_94,self.button_95,self.button_96,self.button_97,self.button_98,self.button_99]]
            ###
            ###This puts space inbetween each 3*3 block of buttons
            ###Causes problems in Mac and UNIX versions of python
            ### to fix this use self.GridFrame.columnconfigure(columnnumber, weight = value) and GridFrame.rowconfigure(rownumber, weight = value)
            self.fill_1 = Button(self.GridFrame,width = 0, height = 0, borderwidth = 0,)
            self.fill_1.grid(row =4, column =1)
            self.fill_2 = Button(self.GridFrame,width = 0, height  = 0, borderwidth = 0,)
            self.fill_2.grid(row =8, column =1)
            self.fill_3 = Button(self.GridFrame,width = 0, height  = 0, borderwidth = 0,)
            self.fill_3.grid(row =4, column =12)
            self.fill_4 = Button(self.GridFrame,width  = 0, height  = 0, borderwidth = 0)
            self.fill_4.grid(row =1, column =4)
            self.fill_5 = Button(self.GridFrame,width  = 0, height  = 0, borderwidth = 0)
            self.fill_5.grid(row =1, column =8)
            self.fill_6 = Button(self.GridFrame,width  = 0, height  = 0, borderwidth = 0)
            self.fill_6.grid(row =12, column =8)
            self.fill_7 = Button(self.GridFrame,width = 0, height  = 0, borderwidth = 0,)
            self.fill_7.grid(row =0, column =0)
            
            ###End Buttons###

        #Function to change the clicked grid button to the active number
        def update_cell(self,position): 
            global locator
            if locator:
                print 'in update_cell'
            New_Number = str(self.Active_Number)
            string_position = str(position)
            x_pos = (int(string_position[0])-1)
            y_pos = (int(string_position[1])-1)
            self.Buttons[x_pos][y_pos].config(background = self.Button_Background)
                
            if New_Number == 'H' and self.Hints != 0 and self.Btn_Change_List[x_pos][y_pos] == True:
                self.Hints -= 1
                self.Hints_Used += 1
                self.Hint_Text.set(('Hints:'+str(self.Hints)))
                
                New_Number = self.ANSWERS[x_pos][y_pos]
                    
                if self.Btn_Change_List[x_pos][y_pos] == True:
                        self.Button_Var[x_pos][y_pos].set(New_Number)
                        
                        self.Btn_Change_List[x_pos][y_pos] = False
                        self.Buttons[x_pos][y_pos].config(activebackground = 'red')
                if debug:
                        print "Cannot Clear"
            elif New_Number == 'H':
                self.Buttons[x_pos][y_pos].config(background = self.Button_Background)
            else:
                if New_Number == '0':
                    New_Number = ''
                if debug:
                    print self.Btn_Change_List[x_pos][y_pos]
                if self.Btn_Change_List[x_pos][y_pos] == True:
                    self.Button_Var[x_pos][y_pos].set(New_Number)
                if debug:
                    print "Cannot Clear"
                    
        ###Button Press functions for all 81 buttons
        def bp_11(self):
            self.update_cell(11)
        def bp_12(self):
            self.update_cell(12)
        def bp_13(self):
            self.update_cell(13)
        def bp_14(self):
            self.update_cell(14)
        def bp_15(self):
            self.update_cell(15)
        def bp_16(self):
            self.update_cell(16)
        def bp_17(self):
            self.update_cell(17)
        def bp_18(self):
            self.update_cell(18)
        def bp_19(self):
            self.update_cell(19)
        def bp_21(self):
            self.update_cell(21)
        def bp_22(self):
            self.update_cell(22)
        def bp_23(self):
            self.update_cell(23)
        def bp_24(self):
            self.update_cell(24)
        def bp_25(self):
            self.update_cell(25)
        def bp_26(self):
            self.update_cell(26)
        def bp_27(self):
            self.update_cell(27)
        def bp_28(self):
            self.update_cell(28)
        def bp_29(self):
            self.update_cell(29)
        def bp_31(self):
            self.update_cell(31)
        def bp_32(self):
            self.update_cell(32)
        def bp_33(self):
            self.update_cell(33)
        def bp_34(self):
            self.update_cell(34)
        def bp_35(self):
            self.update_cell(35)
        def bp_36(self):
            self.update_cell(36)
        def bp_37(self):
            self.update_cell(37)
        def bp_38(self):
            self.update_cell(38)
        def bp_39(self):
            self.update_cell(39)
        def bp_41(self):
            self.update_cell(41)
        def bp_42(self):
            self.update_cell(42)
        def bp_43(self):
            self.update_cell(43)
        def bp_44(self):
            self.update_cell(44)
        def bp_45(self):
            self.update_cell(45)
        def bp_46(self):
            self.update_cell(46)
        def bp_47(self):
            self.update_cell(47)
        def bp_48(self):
            self.update_cell(48)
        def bp_49(self):
            self.update_cell(49)
        def bp_51(self):
            self.update_cell(51)
        def bp_52(self):
            self.update_cell(52)
        def bp_53(self):
            self.update_cell(53)
        def bp_54(self):
            self.update_cell(54)
        def bp_55(self):
            self.update_cell(55)
        def bp_56(self):
            self.update_cell(56)
        def bp_57(self):
            self.update_cell(57)
        def bp_58(self):
            self.update_cell(58)
        def bp_59(self):
            self.update_cell(59)
        def bp_61(self):
            self.update_cell(61)
        def bp_62(self):
            self.update_cell(62)
        def bp_63(self):
            self.update_cell(63)
        def bp_64(self):
            self.update_cell(64)
        def bp_65(self):
            self.update_cell(65)
        def bp_66(self):
            self.update_cell(66)
        def bp_67(self):
            self.update_cell(67)
        def bp_68(self):
            self.update_cell(68)
        def bp_69(self):
            self.update_cell(69)
        def bp_71(self):
            self.update_cell(71)
        def bp_72(self):
            self.update_cell(72)
        def bp_73(self):
            self.update_cell(73)
        def bp_74(self):
            self.update_cell(74)
        def bp_75(self):
            self.update_cell(75)
        def bp_76(self):
            self.update_cell(76)
        def bp_77(self):
            self.update_cell(77)
        def bp_78(self):
            self.update_cell(78)
        def bp_79(self):
            self.update_cell(79)
        def bp_81(self):
            self.update_cell(81)
        def bp_82(self):
            self.update_cell(82)
        def bp_83(self):
            self.update_cell(83)
        def bp_84(self):
            self.update_cell(84)
        def bp_85(self):
            self.update_cell(85)
        def bp_86(self):
            self.update_cell(86)
        def bp_87(self):
            self.update_cell(87)
        def bp_88(self):
            self.update_cell(88)
        def bp_89(self):
            self.update_cell(89)
        def bp_91(self):
            self.update_cell(91)
        def bp_92(self):
            self.update_cell(92)
        def bp_93(self):
            self.update_cell(93)
        def bp_94(self):
            self.update_cell(94)
        def bp_95(self):
            self.update_cell(95)
        def bp_96(self):
            self.update_cell(96)
        def bp_97(self):
            self.update_cell(97)
        def bp_98(self):
            self.update_cell(98)
        def bp_99(self):
            self.update_cell(99)

        ### Changes the current active button to be sunken and 'un sinks' the previously sunk button
        def Change_Sunken(self, button_number):
            global locator
            if locator:
                print 'in Change_Sunken'
            for x in range(11):
                self.Active_Buttons[x].config(bg = 'black')
            self.Active_Buttons[button_number].config(bg = self.Active_Background_Colour)

        ###Active Button press functions
        def Button_1_Press(self):
            self.Active_Number = '1'
            self.Change_Sunken(1)
            if debug:
                print 'Button_1_Press'
                print 'self.Active_Number Changed to:', self.Active_Number
        def Button_2_Press(self):
            self.Active_Number = '2'
            self.Change_Sunken(2)
            if debug:
                print 'Button_2_Press'
                print 'self.Active_Number Changed to:', self.Active_Number
        def Button_3_Press(self):
            self.Active_Number = '3'
            self.Change_Sunken(3)
            if debug:
                print 'Button_3_Press'
                print 'self.Active_Number Changed to:', self.Active_Number
        def Button_4_Press(self):
            self.Active_Number = '4'
            self.Change_Sunken(4)
            if debug:
                print 'Button_4_Press'
                print 'self.Active_Number Changed to:', self.Active_Number
        def Button_5_Press(self):
            self.Active_Number = '5'
            self.Change_Sunken(5)
            if debug:
                print 'Button_5_Press'
                print 'self.Active_Number Changed to:', self.Active_Number
        def Button_6_Press(self):
            self.Active_Number = '6'
            self.Change_Sunken(6)
            if debug:
                print 'Button_6_Press'
                print 'self.Active_Number Changed to:', self.Active_Number
        def Button_7_Press(self):
            self.Active_Number = '7'
            self.Change_Sunken(7)
            if debug:
                print 'Button_7_Press'
                print 'self.Active_Number Changed to:', self.Active_Number
        def Button_8_Press(self):
            self.Active_Number = '8'
            self.Change_Sunken(8)
            if debug:
                print 'Button_8_Press'
                print 'self.Active_Number Changed to:', self.Active_Number
        def Button_9_Press(self):
            self.Active_Number = '9'
            self.Change_Sunken(9)
            if debug:
                print 'Button_9_Press'
                print 'self.Active_Number Changed to:', self.Active_Number
        def Button_0_Press(self):
            self.Active_Number = '0'
            self.Change_Sunken(0)
            if debug:
                print 'Button_0_Press'
                print 'self.Active_Number Changed to:', self.Active_Number

        def Hint_Button_Press(self):
            self.Active_Number = 'H'
            self.Change_Sunken(10)

        ###Funtion to check each of the currently inputted numbers against the actual answer
        ### If all 81 numbers check correctly againt their correct answer it runs the End_Game() function
        def Check_Button_Press(self):
            Counter = 0
            for i in range(9):
                for j in range(9):
                    a = self.Button_Var[i][j].get()
                    if debug:
                        print str(self.ANSWERS[i][j]) + str(a)
                    if str(a) != str(self.ANSWERS[i][j]) and str(a) != '':
                        self.Buttons[i][j].config(background = 'red')
                        self.Checks_Used += 1
                    elif str(a) != str(self.ANSWERS[i][j]):
                        Counter = 0
                    else:
                        self.Buttons[i][j].config(background = self.Button_Background)
                        Counter += 1
            if Counter == 81:
                self.End_Game()
                         
        ###Code that runs when grid is completed and correct      
        def End_Game(self):
            import time
            self.End_Time = time.clock()
            for x in range(9):
                for y in range(9):
                    self.Buttons[x][y].grid_forget()
            for x in range(12):
                self.Active_Buttons[x].grid_forget()

            self.fill_1.grid_forget()
            self.fill_2.grid_forget()
            self.fill_3.grid_forget()
            self.fill_4.grid_forget()
            self.fill_5.grid_forget()
            self.fill_6.grid_forget()
            self.fill_7.grid_forget()

            self.TopLevel = Toplevel()
            self.TopLevel.title('Your Score')

            self.Time_Taken = self.End_Time - self.Start_Time
            tt = self.Time_Taken

            ### Calculates the person's score
            difficulty_penalty = self.Time_Penalty
            hint_penalty = self.Hints_Used * self.Hint_Time_Penalty
            check_penalty = self.Checks_Used * self.Check_Time_Penalty
            self.Time_Penalty += hint_penalty + check_penalty
            
            total_time = int(tt) + self.Time_Penalty
            
            Time_Taken_Text = str(int(self.Time_Taken)) + ' Seconds'

            #Displays the person's score
            self.Label_Time_Taken = Label(self.TopLevel, text = 'Time Taken: ')
            self.Display_Time_Taken = Label(self.TopLevel, text= Time_Taken_Text)
            self.Label_Difficulty_Penalty = Label(self.TopLevel, text = 'Difficulty Penalty: ')
            self.Display_Difficulty_Penalty = Label(self.TopLevel, text = str(difficulty_penalty))
            self.Label_Hints_Used = Label(self.TopLevel, text = 'Hints Used: ')
            self.Display_Hints_Used = Label(self.TopLevel, text = str(self.Hints_Used))
            self.Label_Hint_Penalty = Label(self.TopLevel, text = 'Hint Penalty: ')
            self.Display_Hint_Penalty = Label(self.TopLevel, text = str(hint_penalty))
            self.Label_Checks_Used = Label(self.TopLevel, text = 'Incorrect Checks: ')
            self.Display_Checks_Used = Label(self.TopLevel, text = str(self.Checks_Used))
            self.Label_Check_Penalty = Label(self.TopLevel, text = 'Check Penalty: ')
            self.Display_Check_Penalty = Label(self.TopLevel, text = str(check_penalty))
            self.Label_Total_Penalty = Label(self.TopLevel, text = 'Total_Penalty: ')
            self.Display_Total_Penalty = Label(self.TopLevel, text = str(self.Time_Penalty))
            self.Label_Total_Time = Label(self.TopLevel, text = 'Total Score: ')
            self.Display_Total_Time = Label(self.TopLevel, text = str(total_time))
            self.Label_Time_Taken.grid(row = 0, column = 0)
            self.Display_Time_Taken.grid(row = 0, column = 1)
            self.Label_Difficulty_Penalty.grid(row = 1, column = 0)
            self.Display_Difficulty_Penalty.grid(row = 1, column = 1)
            self.Label_Hints_Used.grid(row = 2, column = 0)
            self.Display_Hints_Used.grid(row = 2, column = 1)
            self.Label_Hint_Penalty.grid(row = 3, column = 0)
            self.Display_Hint_Penalty.grid(row = 3, column = 1)
            self.Label_Total_Penalty.grid(row = 6, column = 0)
            self.Display_Total_Penalty.grid(row = 6, column = 1)
            self.Label_Total_Time.grid(row = 7, column = 0)
            self.Display_Total_Time.grid(row = 7, column = 1)
                        
            ###Appends Score to High Scores File
            try:
                q = open(self.Location_File,'a')
                tag = self.Player_Name +','+self.Difficulty_Used+','+str(int(tt))+','+str(self.Hints_Used)+','+ str(total_time)+'\n'
                q.write(tag)
                q.close()
                
            except IOError:
                print 'High Score File Is Not Valid'
                print 'Please Note Down Your High Score'
                print 'It is:',total_time

            #Gives option to play again
            self.Play_Again_Button = Button(self.GridFrame, text = 'Play Again?', command = self.PlayAgain)
            self.Play_Again_Button.grid()

        ### Funtion for the play again button press
        def PlayAgain(self):
            self.Play_Again_Button.grid_forget()
            self.Reset_Variables()
            self.NewGame()
        
        ### Sets all variables needed to their default values
        def Reset_Variables(self): 
            self.root.title('Enter Name')
            self.root["padx"] = 10
            self.root["pady"] = 5

            ###Name_Entry_Vars###
            self.text_var = StringVar(self.root)
            self.name_var = StringVar(self.root)
            self.Player_Name = None
            #####################
            self.Hints_Used = 0
            self.Checks_Used = 0
            self.Time_Penalty = 0
            self.Difficuly_Used = None
            #####################

            ###Puzzle_Vars###
            
            self.Active_Number = '0'
            
            self.Numbers = None
            self.Rows = [self.Blank_List(),self.Blank_List()\
                     ,self.Blank_List(),self.Blank_List()\
                     ,self.Blank_List(),self.Blank_List()\
                     ,self.Blank_List(),self.Blank_List()\
                     ,self.Blank_List()]
            self.ANSWERS = [self.Blank_List(),self.Blank_List()\
                     ,self.Blank_List(),self.Blank_List()\
                     ,self.Blank_List(),self.Blank_List()\
                     ,self.Blank_List(),self.Blank_List()\
                     ,self.Blank_List()]

            self.Avaliable_Cells = []
            self.Current_Number = None
            self.Lone_Number = None
            self.Unused_Numbers = [1,2,3,4,5,6,7,8,9]
            self.Locked_Numbers = None
            self.Complete_Grid = False
            self.Reset_Build = False
            self.PuzzleCreated = False
            
            self.PuzzleList = []
            
            self.Easy = []
            self.Med = []
            self.Hard = []

            self.Btn_11_Change = True
            self.Btn_12_Change = True
            self.Btn_13_Change = True
            self.Btn_14_Change = True
            self.Btn_15_Change = True
            self.Btn_16_Change = True
            self.Btn_17_Change = True
            self.Btn_18_Change = True
            self.Btn_19_Change = True
            self.Btn_21_Change = True
            self.Btn_22_Change = True
            self.Btn_23_Change = True
            self.Btn_24_Change = True
            self.Btn_25_Change = True
            self.Btn_26_Change = True
            self.Btn_27_Change = True
            self.Btn_28_Change = True
            self.Btn_29_Change = True
            self.Btn_31_Change = True
            self.Btn_32_Change = True
            self.Btn_33_Change = True
            self.Btn_34_Change = True
            self.Btn_35_Change = True
            self.Btn_36_Change = True
            self.Btn_37_Change = True
            self.Btn_38_Change = True
            self.Btn_39_Change = True
            self.Btn_41_Change = True
            self.Btn_42_Change = True
            self.Btn_43_Change = True
            self.Btn_44_Change = True
            self.Btn_45_Change = True
            self.Btn_46_Change = True
            self.Btn_47_Change = True
            self.Btn_48_Change = True
            self.Btn_49_Change = True
            self.Btn_51_Change = True
            self.Btn_52_Change = True
            self.Btn_53_Change = True
            self.Btn_54_Change = True
            self.Btn_55_Change = True
            self.Btn_56_Change = True
            self.Btn_57_Change = True
            self.Btn_58_Change = True
            self.Btn_59_Change = True
            self.Btn_61_Change = True
            self.Btn_62_Change = True
            self.Btn_63_Change = True
            self.Btn_64_Change = True
            self.Btn_65_Change = True
            self.Btn_66_Change = True
            self.Btn_67_Change = True
            self.Btn_68_Change = True
            self.Btn_69_Change = True
            self.Btn_71_Change = True
            self.Btn_72_Change = True
            self.Btn_73_Change = True
            self.Btn_74_Change = True
            self.Btn_75_Change = True
            self.Btn_76_Change = True
            self.Btn_77_Change = True
            self.Btn_78_Change = True
            self.Btn_79_Change = True
            self.Btn_81_Change = True
            self.Btn_82_Change = True
            self.Btn_83_Change = True
            self.Btn_84_Change = True
            self.Btn_85_Change = True
            self.Btn_86_Change = True
            self.Btn_87_Change = True
            self.Btn_88_Change = True
            self.Btn_89_Change = True
            self.Btn_91_Change = True
            self.Btn_92_Change = True
            self.Btn_93_Change = True
            self.Btn_94_Change = True
            self.Btn_95_Change = True
            self.Btn_96_Change = True
            self.Btn_97_Change = True
            self.Btn_98_Change = True
            self.Btn_99_Change = True
            self.Btn_Change_List = [[self.Btn_11_Change, self.Btn_12_Change, self.Btn_13_Change, self.Btn_14_Change,  self.Btn_15_Change,  self.Btn_16_Change,  self.Btn_17_Change,  self.Btn_18_Change,  self.Btn_19_Change],
                            [self.Btn_21_Change,  self.Btn_22_Change,  self.Btn_23_Change,  self.Btn_24_Change,  self.Btn_25_Change,  self.Btn_26_Change,  self.Btn_27_Change,  self.Btn_28_Change,  self.Btn_29_Change],
                            [self.Btn_31_Change,  self.Btn_32_Change,  self.Btn_33_Change,  self.Btn_34_Change,  self.Btn_35_Change,  self.Btn_36_Change,  self.Btn_37_Change,  self.Btn_38_Change,  self.Btn_39_Change],
                            [self.Btn_41_Change,  self.Btn_42_Change,  self.Btn_43_Change,  self.Btn_44_Change,  self.Btn_45_Change,  self.Btn_46_Change,  self.Btn_47_Change,  self.Btn_48_Change,  self.Btn_49_Change],
                            [self.Btn_51_Change,  self.Btn_52_Change,  self.Btn_53_Change,  self.Btn_54_Change,  self.Btn_55_Change,  self.Btn_56_Change,  self.Btn_57_Change,  self.Btn_58_Change,  self.Btn_59_Change],
                            [self.Btn_61_Change,  self.Btn_62_Change,  self.Btn_63_Change,  self.Btn_64_Change,  self.Btn_65_Change,  self.Btn_66_Change,  self.Btn_67_Change,  self.Btn_68_Change,  self.Btn_69_Change],
                            [self.Btn_71_Change,  self.Btn_72_Change,  self.Btn_73_Change,  self.Btn_74_Change,  self.Btn_75_Change,  self.Btn_76_Change,  self.Btn_77_Change,  self.Btn_78_Change,  self.Btn_79_Change],
                            [self.Btn_81_Change,  self.Btn_82_Change,  self.Btn_83_Change,  self.Btn_84_Change,  self.Btn_85_Change,  self.Btn_86_Change,  self.Btn_87_Change,  self.Btn_88_Change,  self.Btn_89_Change],
                            [self.Btn_91_Change,  self.Btn_92_Change,  self.Btn_93_Change,  self.Btn_94_Change,  self.Btn_95_Change,  self.Btn_96_Change,  self.Btn_97_Change,  self.Btn_98_Change,  self.Btn_99_Change]]
            self.tv_11 = StringVar()
            self.tv_12 = StringVar()
            self.tv_13 = StringVar()
            self.tv_14 = StringVar()
            self.tv_15 = StringVar()
            self.tv_16 = StringVar()
            self.tv_17 = StringVar()
            self.tv_18 = StringVar()
            self.tv_19 = StringVar()
            self.tv_21 = StringVar()
            self.tv_22 = StringVar()
            self.tv_23 = StringVar()
            self.tv_24 = StringVar()
            self.tv_25 = StringVar()
            self.tv_26 = StringVar()
            self.tv_27 = StringVar()
            self.tv_28 = StringVar()
            self.tv_29 = StringVar()
            self.tv_31 = StringVar()
            self.tv_32 = StringVar()
            self.tv_33 = StringVar()
            self.tv_34 = StringVar()
            self.tv_35 = StringVar()
            self.tv_36 = StringVar()
            self.tv_37 = StringVar()
            self.tv_38 = StringVar()
            self.tv_39 = StringVar()
            self.tv_41 = StringVar()
            self.tv_42 = StringVar()
            self.tv_43 = StringVar()
            self.tv_44 = StringVar()
            self.tv_45 = StringVar()
            self.tv_46 = StringVar()
            self.tv_47 = StringVar()
            self.tv_48 = StringVar()
            self.tv_49 = StringVar()
            self.tv_51 = StringVar()
            self.tv_52 = StringVar()
            self.tv_53 = StringVar()
            self.tv_54 = StringVar()
            self.tv_55 = StringVar()
            self.tv_56 = StringVar()
            self.tv_57 = StringVar()
            self.tv_58 = StringVar()
            self.tv_59 = StringVar()
            self.tv_61 = StringVar()
            self.tv_62 = StringVar()
            self.tv_63 = StringVar()
            self.tv_64 = StringVar()
            self.tv_65 = StringVar()
            self.tv_66 = StringVar()
            self.tv_67 = StringVar()
            self.tv_68 = StringVar()
            self.tv_69 = StringVar()
            self.tv_71 = StringVar()
            self.tv_72 = StringVar()
            self.tv_73 = StringVar()
            self.tv_74 = StringVar()
            self.tv_75 = StringVar()
            self.tv_76 = StringVar()
            self.tv_77 = StringVar()
            self.tv_78 = StringVar()
            self.tv_79 = StringVar()
            self.tv_81 = StringVar()
            self.tv_82 = StringVar()
            self.tv_83 = StringVar()
            self.tv_84 = StringVar()
            self.tv_85 = StringVar()
            self.tv_86 = StringVar()
            self.tv_87 = StringVar()
            self.tv_88 = StringVar()
            self.tv_89 = StringVar()
            self.tv_91 = StringVar()
            self.tv_92 = StringVar()
            self.tv_93 = StringVar()
            self.tv_94 = StringVar()
            self.tv_95 = StringVar()
            self.tv_96 = StringVar()
            self.tv_97 = StringVar()
            self.tv_98 = StringVar()
            self.tv_99 = StringVar()
            self.Button_Var = [
                         [self.tv_11,self.tv_12,self.tv_13,self.tv_14,self.tv_15,self.tv_16,self.tv_17,self.tv_18,self.tv_19],
                         [self.tv_21,self.tv_22,self.tv_23,self.tv_24,self.tv_25,self.tv_26,self.tv_27,self.tv_28,self.tv_29],
                         [self.tv_31,self.tv_32,self.tv_33,self.tv_34,self.tv_35,self.tv_36,self.tv_37,self.tv_38,self.tv_39],
                         [self.tv_41,self.tv_42,self.tv_43,self.tv_44,self.tv_45,self.tv_46,self.tv_47,self.tv_48,self.tv_49],
                         [self.tv_51,self.tv_52,self.tv_53,self.tv_54,self.tv_55,self.tv_56,self.tv_57,self.tv_58,self.tv_59],
                         [self.tv_61,self.tv_62,self.tv_63,self.tv_64,self.tv_65,self.tv_66,self.tv_67,self.tv_68,self.tv_69],
                         [self.tv_71,self.tv_72,self.tv_73,self.tv_74,self.tv_75,self.tv_76,self.tv_77,self.tv_78,self.tv_79],
                         [self.tv_81,self.tv_82,self.tv_83,self.tv_84,self.tv_85,self.tv_86,self.tv_87,self.tv_88,self.tv_89],
                         [self.tv_91,self.tv_92,self.tv_93,self.tv_94,self.tv_95,self.tv_96,self.tv_97,self.tv_98,self.tv_99]]

            self.Hint_Text = StringVar()
            
    ###Sudoku Generator Module####################################################################################################################################
        ### Converts A Full Sudoku into a easy Sudoku by removing a set amount of numbers
        def Create_Easy(self):
            global locator
            import random
            if locator:
                print 'in Create_Easy'
            Limiter = self.Easy_Remove_Total
            z = range(9)
            self.Puzzle = self.Rows
            ### Sets up the answer array
            for x in z:
                for y in z:
                    self.ANSWERS[x][y] = self.Rows[x][y] 
            remove_total = 0
            ### Code that removes the set amount of numbers from complete sudoku
            while remove_total != Limiter:
                j = random.choice(z)
                k = random.choice(z)
                if self.Puzzle[j][k] != 0:
                    self.Puzzle[j][k] = 0
                    self.Puzzle[8-j][8-k] = 0
                    remove_total += 2   
            return self.Puzzle
        
        ### Converts A Full Sudoku into a medium Sudoku by removing a set amount of numbers
        def Create_Med(self):
            global locator
            import random
            if locator:
                print 'in Create_Med'
            Limiter = self.Med_Remove_Total
            z = range(9)
            self.Puzzle = self.Rows
            ### Sets up the answer array
            for x in z:
                for y in z:
                    self.ANSWERS[x][y] = self.Rows[x][y]     
            remove_total = 0
            ### Code that removes the set amount of numbers from complete sudoku
            while remove_total != Limiter:
                j = random.choice(z)
                k = random.choice(z)
                if self.Puzzle[j][k] != 0:
                    self.Puzzle[j][k] = 0
                    self.Puzzle[8-j][8-k] = 0
                    remove_total += 2     
            return self.Puzzle

        ### Converts A Full Sudoku into a hard Sudoku by removing a set amount of numbers
        def Create_Hard(self):
            global locator
            import random
            if locator:
                print 'in Create_Hard'
            Limiter = self.Hard_Remove_Total
            z = range(9)
            self.Puzzle = self.Rows
            ### Sets up the answer array
            for x in z:
                for y in z:
                    self.ANSWERS[x][y] = self.Rows[x][y]
                    
            remove_total = 0
            ### Code that removes the set amount of numbers from complete sudoku
            while remove_total != Limiter:
                j = random.choice(z)
                k = random.choice(z)
                if self.Puzzle[j][k] != 0:
                    self.Puzzle[j][k] = 0
                    self.Puzzle[8-j][8-k] = 0
                    remove_total += 2        
            return self.Puzzle

        ### Returns a list of blank locations
        def Blank_List(self):
            global locator
            if locator:
                print 'in Blank_List'
            return [0,0,0,0,0,0,0,0,0]

        ### Creates a list of formatted blank location postions
        def Make_List(self):
            global locator
            if locator:
                print 'in Make_List'
            for i in range(9):
                for j in range(9):
                    self.PuzzleList += str(self.Rows[i][j])

                    
        ###Funtion That Builds A Correct Random Sudoku       
        def Build(self):
            global locator
            if locator:
                print 'in Build'
            
            global debug
            import random
            import time
            #Used in debug to test how long it took to create a complete sudoku
            start_time = time.clock()
            temp_Counter = 0
            while self.Complete_Grid == False: #While the grid is not complete
                self.Get_Avaliable_Cells() #Works out the locations of empty cells
                if debug:
                    print self.Avaliable_Cells
                    
                self.Current_Number = self.Get_Number() #Randomly gets a number to start inputting into the grid
                if debug:
                    print 'CURRENT NUMBER', self.Current_Number
                    
                self.Complete_Current_Number() #Tries to put the number into the grid 9 times
                temp_Counter += 1
                if temp_Counter == 9: # If all 9 numbers have been fully inputted into correct positions
                    self.Complete_Grid = True # The Grid Is Complete
                if self.Reset_Build == True: # If for what ever reason the grid needs to be reset all variables reset
                    self.Rows = [self.Blank_List(),self.Blank_List()\
                     ,self.Blank_List(),self.Blank_List()\
                     ,self.Blank_List(),self.Blank_List()\
                     ,self.Blank_List(),self.Blank_List()\
                     ,self.Blank_List()]
                    self.Get_Avaliable_Cells()
                    temp_Counter = 0
                    if debug:
                        print 'BUILD RESET' *10
                    self.Reset_Build = False
                    self.Unused_Numbers = range(1,10)
            end_time = time.clock()
            if debug:
                print "COMPLETED IN",(end_time - start_time)
                print self.Rows
            self.PuzzleCreated = True
            self.Make_List()# Creates an array of 9 lists that contain the 9 numbers of each row
                   
        ### Function to place the current selected number into the grid randomly 9 times
        def Complete_Current_Number(self):
            global locator
            if locator:
                print 'in Complete_Current_Number'
            global debug
            import random
            
            Current_Positions = []
            Fail_Count = 0
            while len(Current_Positions) != 9 and Fail_Count <= 5 : #While the current number has not been put in 9 positions,
                                                  #and it hasn't failed more than 3 times
                try:
                    Single_Cell = self.Check_Single_Item() #Works out if the number has to be placed in a single location
                    
                    if Single_Cell == None: ## If it doesn't have to be placed in a single location
                        
                        Single_Cell = random.choice(self.Avaliable_Cells) #Place the number in a random avaliable cell
                        if debug:
                            print 'Random Cell, Placed in',Single_Cell
                            
                        self.Update_Avaliable_List(Single_Cell / 10,Single_Cell % 10,self.Current_Number)#Updates the list of avaliable locations
                        Current_Positions += [Single_Cell] # The location the number was just placed in is added to the array
                                                 # of positions where the cell has been placed
                    elif Single_Cell >= 0: #If it does have to be placed into a single locatiion
                        if debug:
                            print 'Placed in Single Cell', Single_Cell
                        self.Update_Avaliable_List(Single_Cell / 10,Single_Cell % 10,self.Current_Number)#Updates the list of avaliable locations
                        Current_Positions += [Single_Cell]# The Location the number was just placed in is added to the array
                                                # of positions where the cell has been placed
                except IndexError: #If it finds that there is no more locations that the number can be placed in, it starts the whole process again
                    if debug:
                        print 'Excepted Index Error, Trying This Number Again'
                        print 'Current Current_Positions', Current_Positions
                    #Resets the list of avaliable locations
                    Current_Positions = []
                    self.Get_Avaliable_Cells()
                    Fail_Count += 1
                    if debug:
                        print "Attempt",Fail_Count,"Failed"
            if Fail_Count >= 6: # If it has failed to try and fit the numbers into correct locations 6 times
                self.Reset_Build = True # Makes it so the whole sudoku has to be started again
            else:
                if debug:
                    print "Excepted This List Of Positions, Now Adding Them To Grid", Current_Positions
                
                for x in Current_Positions:
                    self.Change_Number(x % 10, x / 10,self.Current_Number)# formats the locations into a format the game can interperate
                
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
            ###Checks through each block of 3*3 cells to see if there is only a single avaliable location from the list of avaliable locations in that block
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
                    
        ### Updates the list of Avaliable cells
        def Update_Avaliable_List(self,row,column,new_number):
            global locator
            if locator:
                print 'in Update_Avaliable_List'
            self.Change_Number(column,row,new_number)
            Slots = self.Avaliable_Cells
            Slots.remove(int(str(row)+str(column)))
            Remove_Items = []
            for x in Slots:
                if x % 10 == column:
                    Remove_Items += [x]    

                if int(x / 10) == row:
                    Remove_Items += [x]

            for y in Remove_Items:
                Slots.remove(y)
 
            Blocks = self.Block_List()
            XY = int(str(row)+str(column))
            for count in range(9):
                Current_Block = Blocks[count]
                if XY in Current_Block:
                    for xy in Current_Block:
                        if xy in Slots:
                            Slots.remove(xy)
                            
            self.Avaliable_Cells = Slots
                
        #Function to find the current avaliable cells from self.Rows
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
                        self.Avaliable_Cells += [int(str(row_counter)+str(column_counter))]
        
        ### Returns a list of formatted positions in an array
        def Block_List(self):
            global locator
            if locator:
                print 'in Block_List'
            return [[11,12,13,21,22,23,31,32,33],[14,15,16,24,25,26,34,35,36],[17,18,19,27,28,29,37,38,39],\
                  [41,42,43,51,52,53,61,62,63],[44,45,46,54,55,56,64,65,66],[47,48,49,57,58,59,67,68,69],\
                  [71,72,73,81,82,83,91,92,93],[74,75,76,84,85,86,94,95,96],[77,78,79,87,88,89,97,98,99]]

        ### Places a number into a specified location
        def Change_Number(self,Column,Row,New_Number):
            global locator
            if locator:
                print 'in Change_Number'
            row = self.Rows[Row-1]
            row[Column - 1] = New_Number
            self.Rows[Row-1] = row
            
        # Returns a Randomly selected number from the list of unused numbers (Numbers 1-9)
        # to be inputted into the grid
        def Get_Number(self):
            global locator
            if locator:
                print 'in Get_Number'
            import random
            temp = random.choice(self.Unused_Numbers)
            self.Unused_Numbers.remove(temp)
            return temp
        
        # Returns the entire list of numbers as it currently is
        def Get_Answers(self):
            global locator
            if locator:
                print 'in Get_Answers'
            return self.Rows
                    
             

    a =Application()
    a.root.mainloop()

# If the current version of python is wrong or they do not have the correct modules.
except:
    input('This Program Is Not Compatible For Versions Of Python Other Than 2.6.1,\n Press Enter To Quit')
