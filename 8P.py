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


class Node:
    def __init__(self, arr):
        self.array = arr
        self.parent = None


class EightPuzzleState(State):
    def __init__(self, start):
        self.array = start

    def isGoal(self, arr):
        for i in range(8):
            if arr[i] == i + 1:
                continue
            else:
                return False

        if arr[8] == 0:
            return True
        else:
            return False

    # def isValidState

    def __repr__(self):
        res = ""
        for i in range(9):
            if i == 2 or i == 5:
                res += "%s\n" % (self.array[i])
            else:
                if i == 8:
                    res += "%s" % (self.array[8])
                else:
                    res += "%s " % (self.array[i])
        return res

    # def successors(self):

    def slideBlankLeft(self, array, bIndex):
        arr = copy.copy(array)
        arr[bIndex] = arr[bIndex - 1]
        arr[bIndex - 1] = 0
        return arr

    def slideBlankRight(self, array, bIndex):
        arr = copy.copy(array)
        arr[bIndex] = arr[bIndex + 1]
        arr[bIndex + 1] = 0
        return arr

    def slideBlankUp(self, array, bIndex):
        arr = copy.copy(array)
        arr[bIndex] = arr[bIndex - 3]
        arr[bIndex - 3] = 0
        return arr

    def slideBlankDown(self, array, bIndex):
        arr = copy.copy(array)
        arr[bIndex] = arr[bIndex + 3]
        arr[bIndex + 3] = 0
        return arr

    @property
    def successors(self):
        queue = Queue(maxsize=0)
        res = None
        rootNode = Node(self.array)
        if self.isGoal(self.array):
            res = rootNode
        else:
            queue.put(rootNode)
            closedList = {0: [rootNode.array]}
            while not queue.empty():
                pointer = queue.get()
                bIndex = 0
                for i in range(9):
                    if pointer.array[i] == 0:
                        bIndex = i


                if bIndex != 0 and bIndex != 3 and bIndex != 6:
                    temp = self.slideBlankLeft(pointer.array, bIndex)
                    if self.clSearch(closedList.get(bIndex - 1), temp) == False:
                        tempNode = Node(temp)
                        tempNode.parent = pointer
                        if self.isGoal(temp):
                            res = tempNode
                            break
                        else:
                            queue.put(tempNode)
                            if closedList.get(bIndex - 1) is None:
                                closedList[bIndex - 1] = [temp]
                            else:
                                closedList[bIndex - 1].append(temp)



                if bIndex != 2 and bIndex != 5 and bIndex != 8:
                    temp = self.slideBlankRight(pointer.array, bIndex)
                    if self.clSearch(closedList.get(bIndex + 1), temp) == False:
                        tempNode = Node(temp)
                        tempNode.parent = pointer
                        if self.isGoal(temp):
                            res = tempNode
                            break
                        else:
                            queue.put(tempNode)
                            if closedList.get(bIndex + 1) is None:
                                closedList[bIndex + 1] = [temp]
                            else:
                                closedList[bIndex + 1].append(temp)

                if bIndex != 0 and bIndex != 1 and bIndex != 2:
                    temp = self.slideBlankUp(pointer.array, bIndex)
                    if self.clSearch(closedList.get(bIndex - 3), temp) == False:
                        tempNode = Node(temp)
                        tempNode.parent = pointer
                        if self.isGoal(temp):
                            res = tempNode
                            break
                        else:
                            queue.put(tempNode)
                            if closedList.get(bIndex - 3) is None:
                                closedList[bIndex - 3] = [temp]
                            else:
                                closedList[bIndex - 3].append(temp)

                if bIndex != 6 and bIndex != 7 and bIndex != 8:
                    temp = self.slideBlankDown(pointer.array, bIndex)
                    if self.clSearch(closedList.get(bIndex + 3), temp) == False:
                        tempNode = Node(temp)
                        tempNode.parent = pointer
                        if self.isGoal(temp):
                            res = tempNode
                            break
                        else:
                            queue.put(tempNode)
                            if closedList.get(bIndex + 3) is None:
                                closedList[bIndex + 3] = [temp]
                            else:
                                closedList[bIndex + 3].append(temp)

        pointer = res
        sta = LifoQueue(0)
        while not pointer:
            sta.put(pointer.array)
            pointer = pointer.parent
        result = []
        while not sta.empty():
            result.append(sta.get())
        return result

    def clSearch(self, clist, arr):
        if not clist is None:
            for i in clist:
                flag = True
                for k in range(9):
                    if i[k] == arr[k]:
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    return True
            return False

        else:
            return False


start = [0, 1, 2, 3, 4, 5, 6, 7, 8]
test = EightPuzzleState(start)
res = test.successors
print(res)