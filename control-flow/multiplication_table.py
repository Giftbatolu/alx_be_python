number = int(input("Enter a number to see its multiplication table: "))

for num in range(1, 11):
    num_mul = number * num
    print(f"{number} * {num} = {num_mul}")