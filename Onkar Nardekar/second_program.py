# TODO: Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

for iter in range(7):
    if iter == 3 or iter == 6:
        continue
    print(iter)