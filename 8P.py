import copy
import state

### An abstract class that other states will inherit from.
class State:

    def __init__(self):
        pass

    def isGoal(self):
        pass

    def successors(self):
        pass

    def __repr__(self):
        pass

class EightPuzzleState(State):
    def __init__(self, start):
        self.array = start

    def isGoal(self):
        for i in range (8) :
            if self.array[i] == i + 1:
                continue
            else:
                return False

        if self.array[8] == -1:
            return True
        else:
            return False

    # def isValidState

    def __repr__(self):
        res = ""
        for i in range(9):
            if i == 2 or i == 5:
                res += "%s\n" (self.array[i])
            else:
                if i == 8:
                    res += "%s" (self.array[8])
                else:
                    res += "%s " (self.array[i])
        return res

    # def successors(self):


    ### Helper:

    def slideBlankLeft(self):
        bIndex = 0
        for i in range(9):
            if self.array[i] == 0:
                bIndex = i
        if bIndex == 0 or bIndex == 3 or bIndex == 6:
            return -1
        else:
            self.array[bIndex] = self.array[bIndex - 1]
            self.array[bIndex - 1] = 0
            return bIndex - 1

    def slideBlankRight(self):
        bIndex = 0
        for i in range(9):
            if self.array[i] == 0:
                bIndex = i
        if bIndex == 2 or bIndex == 5 or bIndex == 8:
            return -1
        else:
            self.array[bIndex] = self.array[bIndex + 1]
            self.array[bIndex + 1] = 0
            return bIndex + 1

    def slideBlankUp(self):
        bIndex = 0
        for i in range(9):
            if self.array[i] == 0:
                bIndex = i
        if bIndex == 0 or bIndex == 1 or bIndex == 2:
            return -1
        else:
            self.array[bIndex] = self.array[bIndex - 3]
            self.array[bIndex - 3] = 0
            return bIndex - 3

    def slideBlankDown(self):
        bIndex = 0
        for i in range(9):
            if self.array[i] == 0:
                bIndex = i
        if bIndex == 6 or bIndex == 7 or bIndex == 8:
            return -1
        else:
            self.array[bIndex] = self.array[bIndex + 3]
            self.array[bIndex + 3] = 0
            return bIndex + 3

    def successors(self):
        successorsStates = []
        if ()


