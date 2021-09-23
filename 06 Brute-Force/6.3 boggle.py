# 보글 게임판에서 단어를 찾는 재귀 호출 알고리즘

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]


def hasWord(x, y, word, board):
    if 0 > x or x >= len(board) or 0 > y or y >= len(board[0]):
        return False
    elif board[x][y] != word[0]:
        return False
    elif len(word) == 1:
        return True
    for di in range(8):
        nx = x + dx[di]
        ny = y + dy[di]
        if hasWord(nx, ny, word[1:], board):
            return True
    return False


b = [['u', 'r', 'l', 'p', 'm'],
     ['x', 'p', 'r', 'e', 't'],
     ['g', 'i', 'a', 'e', 't'],
     ['x', 't', 'n', 'z', 'y'],
     ['x', 'o', 'q', 'r', 's']]


for i in range(5):
    for j in range(5):
        if hasWord(i, j, "pretty", b):
            print("찾았당")
