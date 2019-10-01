'''
Shagun Bhardwaj
CS 5001
Homework 7
November 20, 2018
'''

import turtle
import sys
import time

SQUARE = 50
SCORES_FILE = "scores.txt"

class Board:
    '''
    Class: Board
    Attributes: turn, n, start, tile_lst, full
        turn: starting player, 1 for black, -1 for white (int)
        n: number of squares on side of board (int)
        start: the starting number for calculations (float)
        tile_lst: list of tiles that holds which tiles
            belong to which player and which are empty (list of ints)
        full: number of total tiles filled (int)
    Methods: starting_tiles, clicked, play_human, play_computer, ai_move,
            available_moves, legal_move, change_tiles, on_board, get_sqx,
            get_sqy, check_game_over, game_over, open_file, add_highscore,
            add_score, draw_circle, draw_board, draw_lines,
            __init__, __str__ and __eq__
    '''

    def __init__(self):
        '''
        Function: __init__
        Parameters: none
        Returns: nothing
        Does: initializes all attributes of game,
                and creates starting game state
        '''

        # set turn and n
        turn = 1
        n = 8
        
        # draw board with 8 squares on side
        # and black tiles player going first
        self.draw_board(n)
        self.turn = turn
        self.n = n
        self.start = -n * SQUARE / 2

        # generate a nested list for tiles
        self.tile_lst = [[0] * n for i in range(n)]

        # generate starting 4 tiles
        self.starting_tiles()

        # initialize moves possible boolean
        self.player_moves = True
        self.ai_moves = True
        
        # initialize total tile counters
        self.total = 4

    def __str__(self):
        '''
        Function: __str__
        Parameters: none
        Returns: printable(string)
        Does: prints out tile list for game
        '''
        printable = str(self.tile_lst)
        return printable

    def __eq__(self, other):
        '''
        Function: __eq__
        Parameters: self, other
        Returns: if two games' tile lists are equal (boolean)
        Does: checks if tile list of two games are equal
        '''
        return self.tile_lst == other.tile_lst

    def starting_tiles(self):
        '''
        Function: starting_tiles
        Parameters: none
        Returns: nothing
        Does: creates 4 starting tiles at
            beginning of game
        '''
        n = self.n
        # formula to choose numbers for 4 starter tiles
        start_tile = int((n / 2) - 1)
        end_tile = start_tile + 1

        # put 2 black and 2 white tiles in 4 starter tiles
        self.tile_lst[start_tile][start_tile] = 1
        self.tile_lst[end_tile][end_tile] = 1
        self.tile_lst[start_tile][end_tile] = -1
        self.tile_lst[end_tile][start_tile] = -1

        # draw 2 player starting tiles
        self.draw_circle(start_tile, start_tile)
        self.draw_circle(end_tile, end_tile)

        # switch color, and draw other 2 starting tiles
        self.turn *= -1
        self.draw_circle(start_tile, end_tile)
        self.draw_circle(end_tile, start_tile)

        # switch to player turn (because player goes first)
        self.turn *= -1
    
    def clicked(self, x, y):
        '''
        Function: clicked
        Parameters: x, y, coordinates of click on turtle
        Returns: nothing
        Does: runs play depending on who's turn it is
        '''
        if self.turn == 1:
            self.play_human(x, y)
        else:
            self.play_computer()


    def play_human(self, x, y):
        '''
        Function: play_human
        Parameters: x, y, coordinates of click on turtle
        Returns: nothing
        Does: let's player choose a move and flip the
            correct tiles; if player cannot move or
            chooses an illegal move, prompts action
        '''
        # find all available moves
        all_moves = self.available_moves()

        # if there are available moves, allow play
        if all_moves != []:
            
            self.player_moves = True
            n = self.n

            # calculate x and y coordinates of square
            sq_x = self.get_sqx(x)
            sq_y = self.get_sqy(y)

            # get if legal move
            legal_move = self.legal_move(sq_x, sq_y)

            # if not legal move, ask player to try again
            if legal_move == []:
                print("Not legal move, try again.")

            # if legal move, execute code block
            else:

                # turn off onscreenclick
                turtle.onscreenclick(None)

                # assign x and y tile
                x_tile = sq_y
                y_tile = sq_x

                # draw tile
                self.draw_circle(sq_x, sq_y)

                # fill tile list with color of tile
                self.tile_lst[x_tile][y_tile] = self.turn

                # change all tiles that should be flipped
                self.change_tiles(legal_move)

                # append to total counter
                self.total += 1

                # check if game is over
                self.check_game_over()

                # change turn and play computer
                self.turn *= -1
                print("\nComputer turn")
                self.play_computer()

        # if no available moves, execute code block
        else:
            print("No legal moves for player.")
            
            # turn off onscreenclick
            turtle.onscreenclick(None)

            # turn player moves to False
            self.player_moves = False
            
            # check if game is over
            self.check_game_over()

            # change turns and play computer
            self.turn *= -1
            print("\nComputer turn")
            self.play_computer()

    def play_computer(self):
        '''
        Function: play_computer
        Parameters: none
        Returns: nothing
        Does: let's AI choose a move and flip the
            correct tiles; if there are no legal moves
            available, prompts apporpriate action
        '''
        # pause half a second
        time.sleep(0.5)
        
        # find all available moves
        all_moves = self.available_moves()

        # if there are available moves, play computer
        if all_moves != []:
            self.ai_moves = True

            # find best move
            best_move = self.ai_move(all_moves)

            # set x and y square for best move
            sq_x = best_move[0]
            sq_y = best_move[1]
            x_tile = sq_y
            y_tile = sq_x

            # find all tiles that will be flipped
            legal_move = self.legal_move(sq_x, sq_y)

            # draw circle in empty square
            self.draw_circle(sq_x, sq_y)
            
            #fill tile list with color of tile
            self.tile_lst[x_tile][y_tile] = self.turn

            # change all tiles that are flipped
            self.change_tiles(legal_move)

            # append to total counter
            self.total += 1

            # check if game is over
            self.check_game_over()

            # change turn and turn onscreenclick on
            self.turn *= -1
            print("\nPlayer turn")
            turtle.onscreenclick(self.clicked)

        # if no available moves, execute code block
        else:
            print("No legal moves for computer.")
            
            # turn computer moves to False
            self.ai_moves = False

            # check if game is over
            self.check_game_over()

            # change turn and turn onscreenclick on
            self.turn *= -1
            print("\nPlayer turn")
            turtle.onscreenclick(self.clicked)

    def ai_move(self, all_moves):
        '''
        Function: ai_move
        Parameters: all_moves, a list of coordinates
                        that contains all legal moves possible
                        (nested list of ints)
        Returns: all_moves[pos], the move that flips
                    the most tiles (list with 2 ints
        Does: loops through all possible legal moves
                and chooses move that flips most tiles;
                returns that tile to play_computer
        '''
        # initialize tiles and counter list
        current_tile = self.turn
        other_tile = self.turn * -1
        counter_lst = []
        
        # loop through all legal moves
        for m in range(len(all_moves)):

            # assign x and y squares from a legal move
            sq_x = all_moves[m][0]
            sq_y = all_moves[m][1]

            # set tiles flipped counter to 0
            tile_counter = 0

            # loop through all 8 directions to find all tiles flipped
            for i, j in [[-1, -1], [-1, 0], [-1, 1], [0, -1],
                     [0, 1], [1, -1], [1, 0], [1, 1]]:
                x = sq_x
                y = sq_y

                # move in that direction 1 step
                x += i
                y += j

                # while the square has opponent tile, move one more square
                while self.on_board(x, y) == True and \
                      self.tile_lst[y][x] == other_tile:
                    x += i
                    y += j

                    # if the tile is turn tile, run code block
                    if self.on_board(x, y) == True and \
                       self.tile_lst[y][x] == current_tile:

                        # move back to starting square, and count tiles flipped
                        while True:
                            x -= i
                            y -= j

                            # when you reach starting tile, break out of loop
                            if x == sq_x and y == sq_y:
                                break

                            # append tile counter
                            tile_counter += 1
                            
            # add tiles flipped to counter list
            counter_lst.append(tile_counter)

        # find index of move that flips most tiles
        pos = counter_lst.index(max(counter_lst))

        # return square for move that flips most tiles
        return all_moves[pos]
        
    def available_moves(self):
        '''
        Function: available_moves
        Parameters: none
        Returns: all_moves, list of all legal moves
                    (nested list of ints)
        Does: finds every legal move available
                by looping through every square on
                board and checking if it is a
                legal move, and adding it to all_moves list
        '''
        n = self.n

        # initialize all moves list
        all_moves = []

        # loop through every square on board
        for i in range(n):
            for j in range(n):

                # check if square is a legal move
                move = self.legal_move(i, j)

                # if it is a legal move, add to all_moves list
                if move != []:
                    all_moves.append([i, j])
        return all_moves
    
    def legal_move(self, sq_x, sq_y):
        '''
        Function: legal_move
        Parameters: sq_x, sq_y, containing square coordinates
                    (2 ints)
        Returns: tiles_flip, list of flipped tiles;
                    empty list if not a legal move
                    (nested list ints)
        Does: checks if move is legal by looping through
                all directions and finding all flipped tiles;
                if not a legal move, returns empty list
        '''

        # if square is not on board or tile is already full,
        # it is not a legal move, and return empty list
        n = self.n
        if sq_x < 0 or sq_x >= n or sq_y < 0 or sq_y >= n:
            return []
        if self.tile_lst[sq_y][sq_x] != 0:
            return []

        # initialize tiles flipped list and tiles turn
        tiles_flip = []
        current_tile = self.turn
        other_tile = self.turn * -1

        # loop through all 8 directions to find all tiles flipped 
        for i, j in [[-1, -1], [-1, 0], [-1, 1], [0, -1],
                     [0, 1], [1, -1], [1, 0], [1, 1]]:
            x = sq_x
            y = sq_y

            # move in that direction 1 step
            x += i
            y += j

            # while the square has opponent tile, move one more square
            while self.on_board(x, y) == True and \
                  self.tile_lst[y][x] == other_tile:
                x += i
                y += j

                # if the tile is turn tile, run code block
                if self.on_board(x, y) == True and \
                   self.tile_lst[y][x] == current_tile:
                    
                    # move back to starting square, and count tiles flipped
                    while True:
                        x -= i
                        y -= j

                        # when you reach starting tile, break out of loop
                        if x == sq_x and y == sq_y:
                            break

                        # append tiles flipped list
                        tiles_flip.append([x, y])

        # if not tiles would be flipped, it means it's not a legal move
        # return empty list
        if len(tiles_flip) == 0:
            return []
        
        return tiles_flip

    def change_tiles(self, tiles_flip):
        '''
        Function: change_tiles
        Parameters: tiles_flips, list of coordinates
                    of tiles to be changed
                    (nested list of ints)
        Returns: nothing
        Does: loops through tiles flip list, and changes
                the tile in tile_lst, and draws the new
                tile on the board
        '''
        for i in range(len(tiles_flip)):
            self.tile_lst[tiles_flip[i][1]][tiles_flip[i][0]] = self.turn
            self.draw_circle(tiles_flip[i][0], tiles_flip[i][1])

    def on_board(self, sq_x, sq_y):
        '''
        Function: on_board
        Parameters: sq_x, sq_y, containing square coordinates
                    (2 ints)
        Returns: boolean, if square is on board
        Does: checks if square is outside board,
                and returns boolean
        '''
        n = self.n
        if sq_x < 0 or sq_x >= n or sq_y < 0 or sq_y >= n:
            return False
        return True
    
    def get_sqx(self, x):
        '''
        Function: get_sqx
        Parameters: x, the x coordinate of click (float)
        Returns: sq_x, the x square clicked on (int)
        Does: calculates the x square clicked on
            using formula
        '''
        try:
            start = self.start
            sq_x = int((x + -start) // SQUARE)
            return sq_x
        except TypeError:
            return -1

    def get_sqy(self, y):
        '''
        Function: get_sqy
        Parameters: y, the y coordinate of click (float)
        Returns: sq_y, the y square clicked on (int)
        Does: calculates the y square clicked on
            using formula
        '''
        try:
            start = self.start
            sq_y = int((-y + -start) // SQUARE)
            return sq_y
        except TypeError:
            return -1

    def check_game_over(self):
        '''
        Function: check_game_over
        Parameters: none
        Returns: nothing
        Does: checks if game is over, by checking if there
                are no legal moves for both players,
                or if all squares are full
        '''
        n = self.n
        if self.player_moves == False and self.ai_moves == False:
            self.game_over()
        elif self.total == n * n:
            self.game_over()
        
    def game_over(self):
        '''
        Function: game_over
        Parameters: none
        Returns: nothing
        Does: calculates number of tiles each player has,
                prints winner of game, asks for name, calls
                type_of_score function, and exits game
        '''
        black_tiles = 0
        white_tiles = 0
        for i in range(len(self.tile_lst)):
            for j in range(len(self.tile_lst[i])):
                if self.tile_lst[i][j] == 1:
                    black_tiles += 1
                elif self.tile_lst[i][j] == -1:
                    white_tiles += 1
        if black_tiles >= white_tiles:
            print("You won! You got", black_tiles, "tiles!")
        else:
            print("Computer won. Computer got", white_tiles, "tiles.")
        name = input("Enter your name.\n")
        self.type_of_score(SCORES_FILE, name, black_tiles)
        sys.exit()

    def open_file(self, filename):
        '''
        Function: open_file
        Parameters: filename, a file containing words (string)
        Returns: lines, all the lines in file (list of strings)
        Does: opens file for reading, returns lines list;
                if there's an OSError, returns empty list
        '''
        try:
            infile = open(filename, "r")
            all_data = infile.read()
            infile.close()
            lines = all_data.splitlines()
            return lines
        except OSError:
            return []
        
    def type_of_score(self, filename, name, score):
        '''
        Function: type_of_score
        Parameters: filename, contains txt file address (string),
                    name (string),
                    score (int)
        Returns: nothing
        Does: determines how to save score;
            if there are no other scores, calls add_score function;
            if the user score is higher than the highscore, adds score
            using add_highscore function;
            if not, appends score using add_score function
        '''
        lines = self.open_file(SCORES_FILE)
        if lines != []:
            split_line = lines[0].split(" ")
        if lines == []:
            self.add_score(filename, name, score)
        elif score > int(split_line[-1]):
            self.add_highscore(filename, name, score, lines)
        else:
            self.add_score(filename, name, score)

    def add_highscore(self, filename, name, score, lines):
        '''
        Function: add_highscore
        Parameters: filename, contains txt file address (string),
                    name (string),
                    score (int),
                    lines, list of all lines in scores file
                        (list of strings)
        Returns: nothing
        Does: opens file to add highscore,
            places high score and name in first position of list,
            then adds rest of names and scores after;
            saves this in the format of names + space + score + \n
            in file
        '''
        try:
            new_lines = [name + " " + str(score)]
            for i in range(len(lines)):
                new_lines.append(lines[i])
            outfile = open(filename, "w")
            for i in range(len(new_lines)):
                outfile.write(new_lines[i] + "\n")
            outfile.close()
        except OSError:
            print("Could not write to scores file.")
            
    def add_score(self, filename, name, score):
        '''
        Function: add_score
        Parameters: filename, contains txt file address (string),
                name (string),
                score (int)
        Returns: nothing
        Does: opens file to add score,
            append name and score using correct formatting;
            if OSError, print message that you could not append
        '''
        try:
            outfile = open(filename, "a")
            outfile.write(name + " " + str(score) + "\n")
            outfile.close()
        except OSError:
            print("Could not append to scores file.")
            
    def draw_circle(self, sq_x, sq_y):
        '''
        Function: draw_circle
        Parameters: sq_x, the x coordinate of square (int)
                    sq_y, the y coordinate of square (int)
        Returns: nothing
        Does: takes x and y coordinate of square, and
                calculates where to move turtle to
                start drawing the circle for turn player
        '''
        start = self.start
        turtle.speed(0)
        turtle.hideturtle()

        # set circle color to turn player color
        if self.turn == 1:
            turtle.fillcolor("black")
        elif self.turn == -1:
            turtle.fillcolor("white")
        turtle.penup()

        # calculate starting coordinates to draw circle
        draw_x = (sq_x * SQUARE) + start + (SQUARE / 2)
        draw_y = -((sq_y * SQUARE) + start + SQUARE)
        turtle.setposition(draw_x, draw_y)

        # draw circle with apporpriate color
        turtle.begin_fill()
        turtle.circle((SQUARE / 2) - 1)
        turtle.end_fill()
        
    def draw_board(self, n):
        '''
        Function: draw_board
        Parameters: n, an int for # of squares
        Returns: nothing
        Does: Draws an nxn board with a green background
        '''

        turtle.setup(n * SQUARE + SQUARE, n * SQUARE + SQUARE)
        turtle.screensize(n * SQUARE, n * SQUARE)
        turtle.bgcolor('white')

        # Create the turtle to draw the board
        othello = turtle.Turtle()
        othello.penup()
        othello.speed(0)
        othello.hideturtle()
        # Line color is black, fill color is green
        othello.color("black", "forest green")
        
        # Move the turtle to the upper left corner
        corner = -n * SQUARE / 2
        othello.setposition(corner, corner)
      
        # Draw the green background
        othello.begin_fill()
        for i in range(4):
            othello.pendown()
            othello.forward(SQUARE * n)
            othello.left(90)
        othello.end_fill()

        # Draw the horizontal lines
        for i in range(n + 1):
            othello.setposition(corner, SQUARE * i + corner)
            self.draw_lines(othello, n)

        # Draw the vertical lines
        othello.left(90)
        for i in range(n + 1):
            othello.setposition(SQUARE * i + corner, corner)
            self.draw_lines(othello, n)

    def draw_lines(self, turt, n):
        '''
        Function: draw_lines
        Parameters: turt, a turtle object
                    n, an int for # of squares
        Returns: nothing
        Does: Draws lines with number of squares
        '''
        turt.pendown()
        turt.forward(SQUARE * n)
        turt.penup()
