num_pattern = int(input("Enter the size of the pattern: "))

b = 1
while b <= num_pattern:
    for d in range(1, num_pattern + 1):
        print("*", end="")
    print("\n")
    b+= 1