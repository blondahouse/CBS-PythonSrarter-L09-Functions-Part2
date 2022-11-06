def mass_sum(m, n):
    if n == m:
        return m
    else:
        return mass_sum(m, n - 1) + n


def int_any(message):
    while True:
        c = input(message)
        try:
            int(c)
        except ValueError:
            print("\t\tError message: Wrong input, try again")
        else:
            return int(c)


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


while True:
    left_del = int_any('\tEnter left delimiter (any int number): ')
    right_del = int_more_than('\tEnter right delimiter (int number more than left delimiter): ', left_del)
    print(f'\t\tMass addition between {left_del} and {right_del} equals {mass_sum(left_del, right_del)}')
