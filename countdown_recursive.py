def countdown(number: int):
    if number == 0:
        return
    print(number)
    countdown(number - 1)


countdown(10000000)
