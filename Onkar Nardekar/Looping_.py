# TODO: Printing Tables using FOR LOOP in Python
try:
    num = int(input('Type Any Number : '))
except:
    print('Type Only Integers')
else:
    for iter in range(1, 11):
        print(f'{num} * {iter} = {num * iter}')