# 보글 게임판에서 단어를 찾는 재귀 호출 알고리즘
import copy

dx = [-1, -1, -1, 0, 0,  1, 1, 1]
dy = [-1,  0, 1, -1, 1, -1, 0, 1]


def hasWord(x, y, word, board, mboard):
    myBoard = copy.deepcopy(mboard)
    if 0 > x or x >= len(board) or 0 > y or y >= len(board[0]):
        return False
    elif board[x][y] != word[0]:
        return False
    elif len(word) == 1:
        myBoard[x][y] = word[0]
        return myBoard
    for di in range(8):
        nx = x + dx[di]
        ny = y + dy[di]
        if k := hasWord(nx, ny, word[1:], board, myBoard):
            myBoard = k
            myBoard[x][y] = word[0]
            return myBoard
    return False


def draw(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print()


b = [['u', 'r', 'l', 'p', 'm'],
     ['x', 'p', 'r', 'e', 't'],
     ['g', 'i', 'a', 'e', 't'],
     ['x', 't', 'n', 'z', 'y'],
     ['x', 'o', 'q', 'r', 's']]

mb = [['*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*']]


for i in range(5):
    for j in range(5):
        if k := hasWord(i, j, "pretty", b, mb):
            draw(k)
            print("찾았당")
