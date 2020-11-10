# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 21:32:18 2020

@author: Dan
"""


def print_board(board):
    
    for i in range(len(board)):
        if i %3==0 and i !=0:
            print('- - - - - - - - - - - -')
            
        for j in range(len(board[0])):
            if j%3==0 and j !=0:
                print(' | ', end="")
                    
            if j ==8:
                print(board[i][j])
            else:
                print(str(board[i][j])+" ",end="")

def find_empty(board):
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j) #row, column
    return None

def correct(board, number, position):
    #to check row
    for i in range(len(board[0])):
        if board[position[0]][i]== number and position[1] !=i:
            return False
        
    #check col
    for i in range(len(board[0])):
        if board[i][position[1]]== number and position[0] !=i:
            return False
        
    #check 3x3
    box_X= position[1]//3
    box_Y= position[0]//3
    
    for i in range(box_Y*3,box_Y*3 +3):
        for j in range(box_X*3,box_X*3 +3):
            if board[i][j]==number and (i,j) != position:
                return False
    return True

def solve(board):
    find=find_empty(board)
    if not find:
        return True
    
    else:
        row,col= find
        
    for i in range(1,10):
        if correct(board,i, (row,col)):
            board[row][col] = i
            
            if solve(board):
                return True
            board[row][col]=0
    return False

board = [
        [0, 0, 0, 4, 0, 0, 1, 0, 0],
        [6, 1, 0, 0, 2, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 2, 8],
        [0, 0, 2, 0, 4, 0, 7, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 2, 0, 3, 0, 0, 0, 1, 7],
        [1, 0, 6, 0, 0, 2, 4, 0, 0],
        [0, 4, 9, 7, 0, 6, 8, 0, 2]
    ]

print(solve(board))
print(print_board(board))
