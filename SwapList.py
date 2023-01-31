class Solution:
    def SwapList(self, FirstHalf, SecundHalf):
        FinalList = []
        x = 0
        y = 0
        while x < len(FirstHalf) and y < len(SecundHalf):
            FinalList.append(FirstHalf[x])
            FinalList.append(SecundHalf[y])
            x += 1
            y += 1

        return FinalList

    def SwapHelper(self, List):
        SwapList = []
        Half = self.HalfList(List)
        for _ in range(Half):
            SwapList.append(List.pop())
        print(List, SwapList)
        return self.SwapList(List, SwapList)

    def HalfList(self, List):
        Index1 = 0
        Index2 = 0
        while Index2 <= len(List):
            Index1 += 1
            Index2 += 2
        print(Index1, Index2)
        return Index1


if __name__ == "__main__":
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(Solution().SwapHelper(List))
