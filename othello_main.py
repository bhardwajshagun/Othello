'''
Shagun Bhardwaj
CS 5001
Homework 7
November 20, 2018
'''

from board import Board
import turtle

def main():

    # initialize Board class variable named othello
    othello = Board()
    print("Player turn\n")
    print(othello)

    # pass Board clicked function when click in turtle
    turtle.onscreenclick(othello.clicked)
          
main()
