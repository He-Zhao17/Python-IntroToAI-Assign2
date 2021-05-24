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

        if (self.array[8] == -1):
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





