import sys

ROMAN_VALUES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def roman_to_int(s: str) -> int:
    s = s.upper()
    n = len(s)
    total = 0
    i = 0
    while i < n:
        val = ROMAN_VALUES[s[i]]
        if i + 1 < n:
            next_val = ROMAN_VALUES[s[i + 1]]
            if val < next_val:
                total += next_val - val
                i += 2
                continue
        total += val
        i += 1
    return total


def int_to_roman(num: int) -> str:
    if num <= 0 or num > 3999:
        return ""
    ROMAN_VALUES_REVERSED = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    res = []
    for value, symbol in ROMAN_VALUES_REVERSED:
        while num >= value:
            num -= value
            res.append(symbol)
    return "".join(res)


def is_integer_string(s: str) -> bool:
    return s.isdigit()


def is_roman_string(s: str) -> bool:
    if not s:
        return False
    s = s.upper()
    for c in s:
        if c not in ROMAN_VALUES:
            return False
    return True


def main():
    for line in sys.stdin:  # read the command line
        s = line.strip()  # strip whitespaces
        if not s:
            continue
        if is_integer_string(s):
            val = int(s)  # convert to int
            roman = int_to_roman(val)
            if roman:
                print(roman)
        elif is_roman_string(s):
            print(roman_to_int(s))
        else:
            print("Nope, not valid")
            continue


if __name__ == "__main__":
    main()
