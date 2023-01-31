
class Solution:
    def ispalindrome(self, word: str) -> bool:
        print(word)
        if len(word) == 0:
            return False
        if len(word) == 1:
            return True
        if word[0] != word[-1]:
            return False
        else:
            return self.ispalindrome(word[1:-1])


if __name__ == "__main__":
    word = "abcba"
    print(Solution().ispalindrome(word))
    assert Solution().ispalindrome(word) == True
