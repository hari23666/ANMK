import math

def is_strong_number(num):
    return sum(math.factorial(int(digit)) for digit in str(num)) == num

def print_strong_numbers_in_range(start, end):
    print(f"Strong numbers between {start} and {end}:")
    strong_numbers = [i for i in range(start, end + 1) if is_strong_number(i)]
    if strong_numbers:
        for num in strong_numbers:
            print(num)
    else:
        print("No strong numbers found in this range.")

print_strong_numbers_in_range(1, 5000)