
def contains(word: str, search: str) -> bool:
    if len(search) > len(word):
        return False
    for i in range(len(word) - (len(search) - 1)):
        for j in range(len(search)):
            # print(search[j], word[i+j])
            if search[j] != word[i+j]:
                break
            if j == len(search)-1:
                return True
    return False


def native(word: str, search: str) -> bool:
    for i in range(len(word) - (len(search) - 1)):
        for j in range(len(search)):
            if word[i+j] == search[j]:
                if j == len(search) - 1:
                    return True
            else:
                break
    return False


def RabinHelper(word: str, search: str) -> bool:
    print(search, int(''.join(str(ord(x)) for x in search)))
    return Rabin(word, search, len(search), int(''.join(str(ord(x)) for x in search)))


def Rabin(word: str, search: str, length: int, processed: str) -> bool:
    processed = processed % 36  # 9
    if len(search) > len(word):
        return False
    for i in range(len(word) - (len(search) - 1)):
        for x in range(length):
            return False


if __name__ == "__main__":
    word = "abcdefabcdefgabcdefghiabcdefabcgdef"
    search = "abcdefghi"
    print(contains(word, search), native(
        word, search), RabinHelper(word, search))

    # assert contains(word, search) and native(
    #     word, search) and RabinHelper(word, search) == search in word
