a = int(input())
b = int(input())
c = int(input())


def print_max_number(num_1, num_2, num_3):
    if num_1 > num_2 and num_1 > num_3:
        print(f"The maximum number is: {num_1}")
    elif num_2 > num_1 and num_2 > num_3:
        print(f"The maximum number is: {num_2}")
    else:
        print(f"The maximum number is: {num_3}")


print_max_number(a, b, c)
