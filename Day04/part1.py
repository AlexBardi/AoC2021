import numpy as np

class BingoBoard:
    def __init__(self,board):
        self.board = board
        self.called = np.zeros((5,5))

    def show(self):
        print(self.board)   

    def update(self, number):
        for i in range(5):
            for j in range(5):
                if self.board[i,j] == number:
                    self.called[i,j] = 1 
                    return self.winCheck()
        return False
    
    def winCheck(self):
        for i in range(5):
            if np.array_equal(self.called[i,:],np.array([1,1,1,1,1])):
                return True

        for j in range(5):
            if np.array_equal(self.called[:,j],np.array([1,1,1,1,1])):
                return True

        if np.array_equal(self.called.diagonal(),np.array([1,1,1,1,1])):
            return True

        if np.array_equal(np.rot90(self.called).diagonal(),np.array([1,1,1,1,1])):
            return True

        return False
    
    def uncalledSum(self):
        sum = 0
        for i in range(5):
            for j in range(5):
                if self.called[i,j] == 0:
                    sum += self.board[i,j]
        return sum

file = open("input.txt")

nums = []
boards = []
temp = []
first = True
second = True

for line in file:
    if first:
        for num in line.split(','):
            nums.append(int(num))
        first = False
    elif second:
        second = False
    else:
        if line == "\n":
            newBoard = BingoBoard(np.array(temp))
            boards.append(newBoard)
            temp = []
        else:
            temp.append([int(n) for n in line.split()])


won = False
idx = 0
while not won:
    print(idx)
    for board in boards:
        won = board.update(nums[idx])
        if won:
            print(nums[idx] * board.uncalledSum())
            break
    idx += 1



def test():
    '''
    arr = [[9,9,9,9,9],
           [9,9,9,9,9],
           [9,9,9,9,9],
           [9,9,9,9,9],
           [9,9,9,9,9]]
    '''
    arr = [[9,9,9,9,1],
           [9,9,9,2,9],
           [9,9,3,9,9],
           [9,4,9,9,9],
           [5,9,9,9,9]]
    b = BingoBoard(np.array(arr))
    print(b.update(1))
    print(b.update(2))
    print(b.update(3))
    print(b.update(4))
    print(b.update(5))

