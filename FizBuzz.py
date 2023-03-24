def FizzBuzz(n: int = 100) -> None:
    if n == 0:
        return
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
    FizzBuzz(n-1)


print(FizzBuzz(100))
