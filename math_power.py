number = float(input())
power = int(input())


def calculate_power(num, p):
    result = pow(num, p)
    return result


print(calculate_power(number, power))
