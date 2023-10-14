def get_sum(a, b):
    # good luck!

    length_of_difference = abs(a - b)
    final_equation = []

    if a == b:
        return 1
    elif a < b:
        for each in range(0, length_of_difference + 1):
            final_equation.append(a)
            a = a + 1
    else:
        for each in range(0, length_of_difference + 1):
            final_equation.append(b)
            b = b + 1

    return sum(final_equation)


get_sum(5, 3)
