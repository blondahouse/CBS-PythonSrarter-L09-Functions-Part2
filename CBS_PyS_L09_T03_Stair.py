# from CBS_PyS_L09_T04_RecursiveSum import int_more_than
def int_more_than(message, start_number):
    while True:
        c = input(message)
        try:
            if int(c) <= start_number:
                raise ValueError
        except ValueError:
            print("\t\tError message: Wrong input, try again")
        else:
            return int(c)


def step_fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return step_fib(n - 1) + step_fib(n - 2)


while True:
    step = int_more_than('\tEnter step number (int number more than zero): ', 0)
    print(f'\t\tthere are {step_fib(step)} options to get the {step} step')
