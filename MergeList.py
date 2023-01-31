# 2 Lists
# merge two sorted lists
# return a new sorted list

class Solution:
    def MergeLists(self, List1, List2, x=0):
        if len(List1) == 0:
            return List2
        if len(List2) == 0:
            return List1

    def ListPop(self, List1, List2):
        MergedList = []
        x = 0
        y = 0
        while len(MergedList) != len(List1 + List2):
            if x < len(List1):
                MergedList.append(List1[x])
                x += 1
            if y < len(List2):
                MergedList.append(List2[y])
                y += 1
        return MergedList


if __name__ == "__main__":
    List1 = [1, 2, 3, 4, 5]
    List2 = [1, 2, 3, 4]
    print(Solution().ListPop(List1, List2))
