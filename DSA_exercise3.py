def print_diamond(n):
    if n % 2 == 0:
        return "Please provide an odd integer."
    
    # Calculate the middle of the diamond
    mid = n // 2
    
    # Loop to print the top half of the diamond (including middle row)
    for i in range(mid + 1):
        # Print spaces followed by stars
        print(' ' * (mid - i) + '*' * (2 * i + 1))
    
    # Loop to print the bottom half of the diamond
    for i in range(mid - 1, -1, -1):
        # Print spaces followed by stars
        print(' ' * (mid - i) + '*' * (2 * i + 1))

# Take user input and ensure it's an integer
try:
    n = int(input("Enter an odd integer: "))
    result = print_diamond(n)
    if result:
        print(result)
except ValueError:
    print("Please enter a valid integer.")
