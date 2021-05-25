import copy
import state
from queue import Queue, LifoQueue

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

    def slideBlankLeft(self, arr, bIndex):
        arr[bIndex] = arr[bIndex - 1]
        arr[bIndex - 1] = 0
        return arr

    def slideBlankRight(self, arr, bIndex):
        arr[bIndex] = arr[bIndex + 1]
        arr[bIndex + 1] = 0
        return arr

    def slideBlankUp(self, arr, bIndex):
        arr[bIndex] = arr[bIndex - 3]
        arr[bIndex - 3] = 0
        return arr

    def slideBlankDown(self, arr, bIndex):
        arr[bIndex] = arr[bIndex + 3]
        arr[bIndex + 3] = 0
        return arr

    @property
    def successors(self):
        queue = Queue(maxsize = 0)
        stack = LifoQueue(maxsize = 0)
        if self.isGoal(self.array):
            stack.put(self.array)
            return stack
        else:
            queue.put(self.array)
            stack.put(self.array)
            while not queue.empty():
                pointer = queue.get()
                bIndex = 0
                for i in range(9):
                    if pointer[i] == 0:
                        bIndex = i
                if bIndex != 0 and bIndex != 3 and bIndex != 6:
                    temp = self.slideBlankLeft(pointer)
                    if self.isGoal(temp):
                        stack





