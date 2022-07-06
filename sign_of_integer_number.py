number = int(input())

def sign_of_integer(num):
    if num == 0:
        print(f"The number {num} is zero.")
    elif num > 0:
        print(f"The number {num} is positive.")
    else:
        print(f"The number {num} is negative.")

sign_of_integer(number)
