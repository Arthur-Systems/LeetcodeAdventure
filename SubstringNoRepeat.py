class Solution:
    def SubstringNoRepeat(self, string: str) -> int:
        if len(string) == 0:
            return 0
        if len(string) == 1:
            return 1
        Max = 1
        for x in range(len(string)):
            for y in range(x + 1, len(string)):
                if string[y] not in string[x:y]:
                    Max = max(Max, y - x + 1)
                else:
                    break
        return Max


if __name__ == "__main__":
    string = "abcabcbb"
    print(Solution().SubstringNoRepeat(string))
