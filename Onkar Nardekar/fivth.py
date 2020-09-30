# TODO: Accept number from user and calculate the sum of all number between 1 and given number

sum1 = 0
n = int(input("Please enter number "))
for i in range(1, n + 1, 1):
    sum1 += i
print("\n")
print("Sum is: ", sum1)