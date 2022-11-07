def float_non_zero(message):
    while True:
        c = input(message)
        try:
            1 / float(c)
        except ValueError:
            print("\t\tError message: Wrong input, try again")
        else:
            return float(c)


def float_any(message):
    while True:
        c = input(message)
        try:
            float(c)
        except ValueError:
            print("\t\tError message: Wrong input, try again")
        else:
            return float(c)


def quadratic_equation(a, b, c):
    def calc_result():
        d = b ** 2 - 4 * a * c
        nonlocal x1, x2
        if d < 0:
            return
        elif d > 0:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
        else:
            x1 = (-b) / (2 * a)
            x2 = (-b) / (2 * a)

    x1 = None
    x2 = None
    calc_result()
    return x1, x2


quadratic_coefficient = float_non_zero('Enter quadratic coefficient \'a\' (a != 0): ')
linear_coefficient = float_any('Enter linear coefficient \'b\': ')
free_term = float_any('Enter free term \'c\': ')
xi1, xi2 = quadratic_equation(quadratic_coefficient, linear_coefficient, free_term)
print(xi1, xi2)
