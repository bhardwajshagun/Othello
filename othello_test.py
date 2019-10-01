'''
Shagun Bhardwaj
CS 5001
Homework 7
November 20, 2018
'''

from board import Board
import unittest


class TestBoard(unittest.TestCase):
    
    def test_init(self):
        othello = Board()
        self.assertEqual(othello.turn, 1)
        self.assertEqual(othello.n, 8)
        self.assertEqual(othello.start, -200)
        self.assertEqual(othello.player_moves, True)
        self.assertEqual(othello.ai_moves, True)
        self.assertEqual(othello.total, 4)
        
        tile_lst = [[0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, -1, 0, 0, 0],
                    [0, 0, 0, -1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(othello.tile_lst, tile_lst)

    def test_str(self):
        othello = Board()
        expected_output = \
                    "[[0, 0, 0, 0, 0, 0, 0, 0], " + \
                    "[0, 0, 0, 0, 0, 0, 0, 0], " + \
                    "[0, 0, 0, 0, 0, 0, 0, 0], " + \
                    "[0, 0, 0, 1, -1, 0, 0, 0], " + \
                    "[0, 0, 0, -1, 1, 0, 0, 0], " + \
                    "[0, 0, 0, 0, 0, 0, 0, 0], " + \
                    "[0, 0, 0, 0, 0, 0, 0, 0], " + \
                    "[0, 0, 0, 0, 0, 0, 0, 0]]"
        self.assertEqual(othello.__str__(), expected_output)

    def test_eq(self):
        o1 = Board()
        o2 = Board()
        self.assertEqual(o1, o2)

    def test_starting_tiles(self):
        othello = Board()
        othello.starting_tiles()
        tile_lst = [[0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, -1, 0, 0, 0],
                    [0, 0, 0, -1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(othello.tile_lst, tile_lst)
        self.assertEqual(othello.turn, 1)

    def test_clicked(self):
        othello = Board()
        othello.clicked(0, 0)
        self.assertEqual(othello.turn, 1)
        othello.clicked(150, 25)
        self.assertEqual(othello.turn, 1)

    def test_play_human(self):
        othello = Board()
        othello.play_human(-100, 100)
        self.assertEqual(othello.total, 4)
        othello.play_human(-200, -200)
        self.assertEqual(othello.total, 4)
        othello.play_human(25, 72)
        self.assertEqual(othello.total, 6)

    def test_play_computer(self):
        othello = Board()
        othello.play_computer()
        self.assertEqual(othello.total, 5)
        othello.play_computer()
        self.assertEqual(othello.total, 6)
        othello.play_computer()
        self.assertEqual(othello.total, 7)
        othello.play_computer()
        self.assertEqual(othello.total, 8)
        othello.play_computer()
        self.assertEqual(othello.total, 9)
        othello.play_computer()
        self.assertEqual(othello.total, 10)

    def test_ai_move(self):
        othello = Board()
        test_input = othello.ai_move([[2, 4], [3, 5], [4, 2], [5, 3]])
        self.assertEqual(test_input, [2,4])
        
    def test_available_moves(self):
        othello = Board()
        expected_output = [[2, 4], [3, 5], [4, 2], [5, 3]]
        self.assertEqual(othello.available_moves(), expected_output)

    def test_legal_move(self):
        othello = Board()
        self.assertEqual(othello.legal_move(2, 4), [[3, 4]])
        self.assertEqual(othello.legal_move(3, 5), [[3, 4]])
        self.assertEqual(othello.legal_move(4, 2), [[4, 3]])
        self.assertEqual(othello.legal_move(5, 3), [[4, 3]])

    def test_change_tiles(self):
        othello = Board()
        expected_output = [[0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, -1, 0, 0, 0],
                            [0, 0, 0, 1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0]]
        othello.change_tiles([[3, 4]])
        self.assertEqual(othello.tile_lst, expected_output)
        othello.turn *= -1
        expected_output = [[0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, -1, 0, 0, 0],
                            [0, 0, 0, -1, -1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0]]
        othello.change_tiles([[3, 4], [4, 4]])
        self.assertEqual(othello.tile_lst, expected_output)
        othello.turn *= -1
        expected_output = [[0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 1, 0, 0, 0],
                            [0, 0, 0, 1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0]]
        othello.change_tiles([[4, 3], [4, 4], [3, 4]])
        self.assertEqual(othello.tile_lst, expected_output)
        othello.turn *= -1
        expected_output = [[0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, -1, -1, 0, 0, 0],
                            [0, 0, 0, -1, -1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0]]
        othello.change_tiles([[3, 3], [3, 4], [4, 3], [4, 4]])
        self.assertEqual(othello.tile_lst, expected_output)
        othello.turn *= -1
        expected_output = [[0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, -1, 0, 0, 0],
                            [0, 0, 0, -1, -1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0]]
        othello.change_tiles([[3, 3]])
        self.assertEqual(othello.tile_lst, expected_output)

    def test_on_board(self):
        othello = Board()
        self.assertTrue(othello.on_board(0, 0))
        self.assertTrue(othello.on_board(4, 3))
        self.assertTrue(othello.on_board(7, 7))
        self.assertTrue(othello.on_board(2, 0))
        self.assertTrue(othello.on_board(0, 3))
        self.assertFalse(othello.on_board(0, -1))
        self.assertFalse(othello.on_board(-6, 0))
        self.assertFalse(othello.on_board(8, 2))
        self.assertFalse(othello.on_board(12, 0))
        self.assertFalse(othello.on_board(6, -4))

    def test_get_sqx(self):
        othello = Board()
        self.assertEqual(othello.get_sqx(-94.2), 2)
        self.assertEqual(othello.get_sqx(-29.5), 3)
        self.assertEqual(othello.get_sqx(3.4), 4)
        self.assertEqual(othello.get_sqx(51.0), 5)
        self.assertEqual(othello.get_sqx("hi"), -1)
        self.assertEqual(othello.get_sqx(0.0), 4)
        self.assertEqual(othello.get_sqx([]), -1)
        self.assertEqual(othello.get_sqx(150.0), 7)
        self.assertEqual(othello.get_sqx(200.0), 8)
        self.assertEqual(othello.get_sqx(-100.0), 2)

    def test_get_sqx(self):
        othello = Board()
        self.assertEqual(othello.get_sqy(-71.5), 5)
        self.assertEqual(othello.get_sqy(-42.3), 4)
        self.assertEqual(othello.get_sqy(21.8), 3)
        self.assertEqual(othello.get_sqy(91.0), 2)
        self.assertEqual(othello.get_sqy("bye"), -1)
        self.assertEqual(othello.get_sqy(0.0), 4)
        self.assertEqual(othello.get_sqy([]), -1)
        self.assertEqual(othello.get_sqy(150.0), 1)
        self.assertEqual(othello.get_sqy(100.0), 2)
        self.assertEqual(othello.get_sqy(-50.0), 5)

    def test_open_file(self):
        othello = Board()
        dummy_files = ["dummy_scores1.txt", "dummy_scores2.txt",
                    "dummy_scores3.txt", "dummy_scores4.txt",
                    "dummy_scores5.txt", "dummy_scores6.txt",
                    "dummy_scores7.txt", "dummy_scores8.txt",
                    "dummy_scores9.txt", "dummy_scores10.txt"]
        expected_results = [["David 6", "Mathis 2", "Richard 3",
                            "Parsons 4", "Andrew 5", "Cameron 1",
                            "Rose 1", "Paterson 6", "Diane 1", "Lyman 1"],
                           ["Piers Smith 9"],
                           ["Kelly Bryant 9", "Jack Smith 7",
                            "Mitchell Anthony 2", "Anthony Lewis 1",
                            "Marvin Green 4", "Jake Ryan 4", "Kerr Steve 5"],
                           ["frank20 2", "henderson17 1",
                            "20matt 1", "17bailey 0"],
                           ["Cameron@ 4", "Springer# 4"],
                           ["ava 7", "scott 2", "paul 3",
                            "ogden 2", "sue 4", "butler 6"],
                           ["Christopher 7 6", "Murray 4 2", "Jane 6 4",
                            "Bell 2 3", "Luke 1 5", "Turner 2 1",
                            "Ryan 3 3", "Cornish 4 2"],
                           ["ju@lian 4", "mart%in 1", "b$lake 2"],
                           [], []]
        for i in range(len(dummy_files)):
            self.assertEqual(othello.open_file(dummy_files[i]),
                                               expected_results[i])

    def test_add_highscore(self):
        othello = Board()
        dummy_files = ["add_highscore1.txt", "add_highscore2.txt",
                           "add_highscore3.txt", "add_highscore4.txt",
                           "add_highscore5.txt", "add_highscore6.txt",
                           "add_highscore7.txt", "add_highscore8.txt",
                           "add_highscore9.txt", "add_highscore10.txt"]
        dummy_names = ["Fiona", "abby", "KALLIE",
                           "jeffe%ry", "SHANE", "Rhianna",
                           "Larissa Jackson", "Nathen 20",
                           "Theresa Smith", "Caleb"]
        dummy_scores = [7, 20, 34, 3, 8, 10, 9, 5, 2, 12]
        dummy_lines = [["David 6", "Mathis 2", "Richard 3",
                            "Parsons 4", "Andrew 5", "Cameron 1",
                            "Rose 1", "Paterson 6", "Diane 1", "Lyman 1"],
                           ["Piers Smith 9"],
                           ["Kelly Bryant 9", "Jack Smith 7",
                            "Mitchell Anthony 2", "Anthony Lewis 1",
                            "Marvin Green 4", "Jake Ryan 4", "Kerr Steve 5"],
                           ["frank20 2", "henderson17 1",
                            "20matt 1", "17bailey 0"],
                           ["Cameron@ 4", "Springer# 4"],
                           ["ava 7", "scott 2", "paul 3",
                            "ogden 2", "sue 4", "butler 6"],
                           ["Christopher 7 6", "Murray 4 2", "Jane 6 4",
                            "Bell 2 3", "Luke 1 5", "Turner 2 1",
                            "Ryan 3 3", "Cornish 4 2"],
                           ["ju@lian 4", "mart%in 1", "b$lake 2"],
                           ["rajesh 1", "rohit 1", "rahul 1"],
                            ["EMILY 9", "ALEX 5", "SARAH 6", "DYLAN 8"]]
        expected_results = ["Fiona 7", "abby 20", "KALLIE 34",
                              "jeffe%ry 3", "SHANE 8",
                              "Rhianna 10", "Larissa Jackson 9",
                              "Nathen 20 5", "Theresa Smith 2",
                              "Caleb 12"]
        for i in range(len(dummy_files)):
            othello.add_highscore(dummy_files[i], dummy_names[i],
                                  dummy_scores[i], dummy_lines[i])
            lines = othello.open_file(dummy_files[i])
            self.assertEqual(lines[0], expected_results[i])

    def test_add_score(self):
        othello = Board()
        dummy_files = ["add_score1.txt", "add_score2.txt",
                       "add_score3.txt", "add_score4.txt",
                       "add_score5.txt", "add_score6.txt",
                       "add_score7.txt", "add_score8.txt",
                       "add_score9.txt", "add_score10.txt"]
        dummy_names = ["Fiona", "abby", "KALLIE",
                       "jeffe%ry", "SHANE", "Rhianna",
                       "Larissa Jackson", "Nathen 20",
                       "Theresa Smith", "Caleb"]
        dummy_scores = [4, 8, 1, 45, 20, 300, 5, 0, 7, 2]
        expected_results = ["Fiona 4", "abby 8", "KALLIE 1",
                          "jeffe%ry 45", "SHANE 20",
                          "Rhianna 300", "Larissa Jackson 5",
                          "Nathen 20 0", "Theresa Smith 7",
                          "Caleb 2"]
        for i in range(len(dummy_files)):
            othello.add_score(dummy_files[i], dummy_names[i], dummy_scores[i])
            lines = othello.open_file(dummy_files[i])
            self.assertEqual(lines[-1], expected_results[i])

def main():
    
    unittest.main(verbosity = 3)
    
main()
