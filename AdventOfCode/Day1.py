def main():
    filename = "/Users/arthur/Documents/GitHub/LeetcodeAdventure/AdventOfCode/input.txt"
    File_object = open(filename, "r")

    numberlist = []
    for line in File_object:
        linenumber = ""
        for char in line:
            if char.isdigit():
                linenumber += char
        numberlist.append(int(linenumber[0] + linenumber[len(linenumber) - 1]))
    print(numberlist)
    print(sum(numberlist))


def mainfindtext():
    filename = "/Users/arthur/Documents/GitHub/LeetcodeAdventure/AdventOfCode/input.txt"
    File_object = open(filename, "r")

    substrings = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    NumberList = []

    for line in File_object:
        linenumber = ""
        for i in range(len(line)):
            if line[i].isdigit():
                linenumber += line[i]
            for key in substrings:
                if line[i : i + len(key)] == key:
                    linenumber += str(substrings[key])

        NumberList.append(int(NumberList[0] + NumberList[len(NumberList) - 1]))
    print(NumberList)
    print(sum(NumberList))


if __name__ == "__main__":
    mainfindtext()
