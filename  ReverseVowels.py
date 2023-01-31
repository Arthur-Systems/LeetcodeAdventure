class Solution:
    def reverseVowels(self, s: str) -> str:
        Converted = self.ConvertToList(s)
        Vowels = ["A", "E", "I", "O", "U"]
        FoundVowels = {}
        VowelPosReverse = []
        VowelPos = []
        for x in range(len(Converted)):
            if Converted[x].upper() in Vowels:
                FoundVowels[x] = Converted[x]
                VowelPos.append(x)
        print(FoundVowels)
        VowelPosReverse = VowelPos[::-1]
        print(VowelPos)
        for x in range(len(VowelPos)):
            Converted[VowelPos[x]] = FoundVowels[VowelPosReverse[x]]
        return self.ConvertToStr(Converted)

    def ConvertToList(self, s: str) -> list[str]:
        Converted = []
        for x in range(len(s)):
            Converted.append(s[x])
        return Converted

    def ConvertToStr(self, List):
        FinalStr = ""
        for x in range(len(List)):
            FinalStr += List[x]
        return FinalStr


if __name__ == "__main__":
    word = "owo"
    print(Solution().reverseVowels(word))
    assert Solution().reverseVowels(word) == "owo"
