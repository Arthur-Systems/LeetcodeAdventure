def calculate(s: str) -> int:
    s = s.replace(" ", "")
    stack = []
    num = 0
    last_operation = "+"

    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num * 10 + int(ch)
        if ch in "*+-/" or i == len(s) - 1:
            if last_operation == "+":
                stack.append(num)
            if last_operation == "-":
                stack.append(-num)
            if last_operation == "*":
                stack.append(stack.pop() * num)
            if last_operation == "/":
                stack.append(stack.pop() / num)
            last_operation = ch
            num = 0
    return sum(stack)


if __name__ == "__main__":
    expr = "3+5 / 2 "
    print(calculate(expr))  # should be 5.5
